
# Kubernetes Installation on Fedora Using kubeadm

## Deep Explanation of Concepts and Troubleshooting

---

# 1. Objective

The goal was to:

* Install a **standard kubeadm-based Kubernetes cluster**
* Enable **etcd visibility** for practicing cluster recovery
* Understand **control plane internals**

Unlike k3s (which bundles components into a single binary), kubeadm installs a production-style Kubernetes control plane where:

* etcd runs as a **static pod**
* API server runs independently
* Certificates are explicitly generated
* Control plane components are visible and debuggable

This setup closely resembles real-world Kubernetes deployments.

---

# 2. Installing containerd

Kubernetes does not run containers directly.

Architecture flow:

```
kubectl
→ API Server
→ kubelet
→ Container Runtime
→ Linux kernel (namespaces + cgroups)
```

The container runtime used here is **containerd**.

### Why containerd is required

* Kubernetes communicates with runtimes via **CRI (Container Runtime Interface)**
* containerd implements CRI
* kubelet requires a CRI endpoint to launch pods

### Installation (Fedora)

```bash
sudo dnf install -y containerd
```

Start and enable it:

```bash
sudo systemctl enable --now containerd
```

---

# 3. Configuring containerd (SystemdCgroup = true)

By default, containerd may use the `cgroupfs` driver.

Fedora uses **systemd** for cgroup management.
Kubelet also defaults to using `systemd` as the cgroup driver.

If kubelet and containerd use different cgroup drivers:

* kubelet fails to start
* Node remains `NotReady`
* Resource enforcement breaks

### Generate default config

```bash
sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml
```

Edit the config:

```bash
sudo nano /etc/containerd/config.toml
```

Set:

```toml
SystemdCgroup = true
```

Restart containerd:

```bash
sudo systemctl restart containerd
```

### Why this matters

Cgroups are Linux kernel features that enforce CPU and memory limits.
Kubernetes depends on them for resource guarantees.

Both kubelet and containerd must operate within the same resource hierarchy.

---

# 4. Loading Required Kernel Modules

Enable required modules:

```bash
sudo modprobe overlay
sudo modprobe br_netfilter
```

Make them persistent:

```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
```

### Why `overlay` is required

Container images are layered filesystems.
OverlayFS merges layers into a unified filesystem view.

Without it, container images cannot mount correctly.

### Why `br_netfilter` is required

Kubernetes networking relies on `iptables`.

Pods communicate via Linux bridges (like `cni0`).
By default, bridged traffic bypasses iptables.

`br_netfilter` ensures:

* iptables rules apply to bridged traffic
* Services (ClusterIP) function
* Network policies work

Without this module, service routing fails.

---

# 5. Enabling Required sysctl Settings

Create configuration:

```bash
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```

Apply settings:

```bash
sudo sysctl --system
```

### Why `ip_forward` is required

Nodes act as routers between:

* Pod network
* Service network
* Node network

If IP forwarding is disabled, packets cannot traverse interfaces.

### Why `bridge-nf-call-iptables` is required

Ensures bridged traffic is processed by iptables, which `kube-proxy` depends on.

Without these, `kubeadm` fails preflight checks.

---

# 6. Installing kubeadm, kubelet, kubectl

Add Kubernetes repository (Fedora-compatible method):

```bash
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.29/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.29/rpm/repodata/repomd.xml.key
EOF
```

Install components:

```bash
sudo dnf install -y kubelet kubeadm kubectl
```

Enable kubelet:

```bash
sudo systemctl enable --now kubelet
```

### Component Roles

* **kubeadm** – Bootstraps the control plane (runs once, then exits)
* **kubelet** – Long-running node agent
* **kubectl** – Command-line client

---

# 7. Major Issue: Swap

Running:

```bash
sudo kubeadm init
```

Resulted in:

```
running with swap on is not supported
```

### Why Kubernetes disables swap

* Kubernetes enforces strict memory guarantees
* Swap introduces unpredictability
* Pods may be swapped instead of OOMKilled
* Scheduler assumptions break

Fedora uses **zram-based swap** (`/dev/zram0`) by default.

Even after:

```bash
sudo swapoff -a
```

Swap reappeared because systemd recreated it.

### Permanent Solution

Disable zram service:

```bash
sudo systemctl disable --now systemd-zram-setup@zram0.service
sudo systemctl mask systemd-zram-setup@zram0.service
```

Verify:

```bash
free -h
```

Swap should show:

```
Swap: 0B 0B 0B
```

This was the primary installation blocker.

---

# 8. Understanding kubelet Failure

`kubeadm init` creates static pod manifests in:

```
/etc/kubernetes/manifests
```

Includes:

* `etcd.yaml`
* `kube-apiserver.yaml`
* `kube-controller-manager.yaml`
* `kube-scheduler.yaml`

kubelet:

* Watches that directory
* Launches components via containerd

If kubelet crashes (e.g., due to swap), the control plane never starts.

Symptoms:

* Port `6443` not listening
* `kubectl` shows connection refused

The root cause was kubelet failing early.

---

# 9. Successful Initialization

After permanently disabling swap:

```bash
sudo kubeadm init
```

This generated:

* Certificates in `/etc/kubernetes/pki`
* Admin kubeconfig
* Static pod manifests
* Bootstrap tokens
* CoreDNS and kube-proxy

Control plane became healthy.

---

# 10. TLS Certificate Error

After initialization:

```
x509: certificate signed by unknown authority
```

### Cause

Earlier failed attempts regenerated certificates.

But local kubeconfig still referenced an older CA.

Client could not verify API server certificate.

### Fix

Replace kubeconfig:

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

After this, `kubectl` authenticated successfully.

---

# 11. Why `sudo kubectl` Failed

Running:

```bash
sudo kubectl get nodes
```

kubectl searched for:

```
/root/.kube/config
```

Since it didn’t exist, it defaulted to:

```
http://localhost:8080
```

Modern clusters do not expose that endpoint.

Correct usage: run `kubectl` as your normal user.

---

# 12. Node NotReady → Ready Transition

Immediately after initialization:

```
NotReady
```

Expected because:

* CNI plugin not yet initialized
* Node conditions still updating

Once networking stabilized:

```
Ready
```

This confirms:

* etcd healthy
* API server reachable
* kubelet running
* control plane components active
* networking functional

---

# 13. Final System State

You now have a full **kubeadm-based cluster** with:

* Static pod control plane
* Embedded etcd
* Certificate authority hierarchy
* Real etcd data directory
* Recoverable control plane

This enables:

* etcd snapshot and restore practice
* Control plane recovery drills
* Certificate renewal practice
* Disaster simulation

---

# 14. Key Lessons

1. Fedora’s zram swap conflicts with kubelet defaults.
2. Swap must be permanently disabled before `kubeadm init`.
3. Cgroup driver alignment is mandatory.
4. Kernel modules are essential for container networking.
5. Static pods are managed entirely by kubelet.
6. TLS errors often indicate kubeconfig mismatch.
7. Most kubeadm failures originate from system-level configuration.

---

# Conclusion

The Kubernetes cluster is now correctly installed using kubeadm on Fedora.

All encountered issues stemmed from:

* Default swap configuration
* Client-side kubeconfig mismatch
* Kernel and networking prerequisites

This installation process exposed how Kubernetes interacts with:

* The Linux kernel
* The container runtime
* The networking stack
* The certificate authority system

The system is now ready for advanced etcd recovery and control plane troubleshooting practice.
