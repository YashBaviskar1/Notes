

## Services 



---

##  **Introduction to Services in Kubernetes**

###  Why Do We Need Services?

In Kubernetes, **Pods are ephemeral** — they can be created, destroyed, rescheduled, or replaced at any time. Each time a Pod is (re)created, it gets a **new IP address**.

So, if you have applications that need to communicate reliably, you **can’t use Pod IPs directly** — they’re **unstable**.

 **Solution:** Use a **Service**
A Service gives you a **stable network endpoint**, even when the underlying Pods change.

---

###  What is a Kubernetes Service?

A **Service** is an abstraction that:

* Exposes a logical **set of Pods**
* Uses **selectors** (labels) to identify the Pods
* Provides a **stable IP** and **DNS name**
* Handles **load balancing** between multiple Pods

---

###  How Does It Work?

* You define a Service with a `selector`, like:

  ```yaml
  selector:
    app: nginx
  ```

* Kubernetes automatically finds all Pods with that label.

* Anytime Pods come or go (scale up/down), the Service updates and routes traffic accordingly.

So, even if Pods get replaced, **the Service stays the same**.

---

###  Basic Types of Services

| Service Type     | Used For                          | Accessible From           |
| ---------------- | --------------------------------- | ------------------------- |
| **ClusterIP**    | Internal access only              | Within the cluster        |
| **NodePort**     | Exposes a port on each node       | From outside, via node IP |
| **LoadBalancer** | Exposes service externally, cloud | Internet (via cloud LB)   |
| **ExternalName** | Maps service to external DNS name | Anywhere                  |

 Default: `ClusterIP`
❗ In Minikube, `LoadBalancer` works via built-in tricks (like `minikube service`).

---

###  Real-Life Example

You deployed `nginx` on 3 Pods. To make it accessible outside the Pod network, you might create a Service:

```bash
kubectl expose deployment nginx-deployment --type=NodePort --port=80
```

Now Kubernetes makes sure **all traffic hitting the Service** is passed to one of the nginx Pods — even if one dies or gets replaced.

---

###  Why Services Matter

* Decouple your **app's identity** from its **dynamic underlying Pods**
* Enable **stable access** to apps or microservices
* Support **load balancing** out of the box
* Provide **DNS discovery** (e.g. `my-service.default.svc.cluster.local`)

---

###  In Summary

Pods  → Temporary, dynamic
Services  → Permanent, stable entry point

**Services are like the receptionist at a hotel** — even if rooms (Pods) change, the receptionist (Service) always knows where to direct you.

---

## 🔧 You Exposed Your Deployment as a Service

```bash
k expose deployment nginx-deployment --port=8080 --target-port=80
```

### ✅ What This Command Does

* Creates a **Service** named `nginx-deployment`
* Exposes it **inside the cluster** (because default type = `ClusterIP`)
* Maps:

  * **Service port 8080** → exposed to other Pods
  * **Target port 80** → actual port inside nginx container

That means:
Any Pod inside the cluster can reach nginx at:

```
http://<service-name>:8080
```

Example:

```bash
curl http://nginx-deployment:8080
```

---

## 🔍 List All Services

```bash
k get services
```

Output:

```
NAME               TYPE        CLUSTER-IP       PORT(S)
nginx-deployment   ClusterIP   10.106.68.184    8080/TCP
```

✅ A ClusterIP Service was created
✅ It was assigned a stable internal IP (10.106.68.184)
✅ Port 8080 is how other Pods will reach port 80 on your nginx containers

---

## 🧠 What Is a ClusterIP Service?

A **ClusterIP Service**:

* Is the **default Service type** in Kubernetes
* Exposes the app **only inside the cluster**
* Gives you a **virtual IP address** and a **DNS name**
* Load-balances traffic across all matching Pods (using labels)

---

### 🔄 How It Works

```
                  [ Pod: nginx ]   (10.244.0.4)
                       ^
                       |
                  [ Pod: nginx ]   (10.244.0.7)   <- backend Pods
                       ^
                       |
                +----------------+
                |   ClusterIP    |  <-- stable virtual 'front door'
                | 10.106.68.184  |
                | Port: 8080     |
                +----------------+
                       |
                Accessible only within cluster
```

Any Pod can access the nginx app using:

* Service DNS name: `nginx-deployment.default.svc.cluster.local:8080`
* Or ClusterIP: `10.106.68.184:8080`

---

### 🛑 Access to ClusterIP **from outside** the cluster?

Not possible.
If you try to access this Service from your host machine (outside Kubernetes), it **won't work** — it's internal only.

To expose it outside the cluster, you'd need a **NodePort**, **LoadBalancer**, or **Ingress**.

---

## 🎯 Summary

| Feature              | ClusterIP                  |
| -------------------- | -------------------------- |
| Default?             | ✅ Yes (most basic type)    |
| External access?     | ❌ No (inside cluster only) |
| Use case             | Pod-to-Pod communication   |
| Load balancing       | ✅ Kubernetes handles it    |
| Stable IP + DNS name | ✅ Yes                      |

---



---

##  `kubectl describe svc nginx-deployment` Explained

You ran:

```bash
k describe svc nginx-deployment
```

This gives a detailed view of the **Service** you created for your nginx Deployment.

---

### 🔧 Basic Info

```
Name:                     nginx-deployment
Namespace:                default
Labels:                   app=nginx-deployment
Selector:                 app=nginx-deployment
Type:                     ClusterIP
IP:                       10.106.68.184
Port:                     <unset> 8080/TCP
TargetPort:               80/TCP
```

| Field          | Meaning                                                                |
| -------------- | ---------------------------------------------------------------------- |
| **Name**       | Name of the Service (`nginx-deployment`)                               |
| **Namespace**  | It's in the `default` namespace                                        |
| **Labels**     | Help Kubernetes identify this object (e.g., for searching or grouping) |
| **Selector**   | Matches Pods with `app=nginx-deployment` (links Service 👉 Pods)       |
| **Type**       | `ClusterIP` – only reachable inside the cluster                        |
| **IP**         | Stable **virtual IP** of the Service: `10.106.68.184`                  |
| **Port**       | Clients will use `8080` to talk to this Service                        |
| **TargetPort** | Traffic is forwarded to container port `80` (nginx's port)             |

---

### 🔁 How Does Traffic Flow?

```
Service IP (10.106.68.184):8080  ----->  Pod IPs (x.x.x.x):80
```

* Traffic to `10.106.68.184:8080` is forwarded by Kubernetes to one of the matching Pods' port 80.

---

### 🔗 Endpoints

```
Endpoints:  10.244.0.4:80, 10.244.0.5:80, 10.244.0.7:80
```

This means the Service is currently routing to **three Pods**, each listening on port **80**:

| Pod Name | Pod IP     | Container Port |
| -------- | ---------- | -------------- |
| ...hx2ll | 10.244.0.4 | 80             |
| ...w7t7p | 10.244.0.5 | 80             |
| ...774bs | 10.244.0.7 | 80             |

These IPs come from your `nginx-deployment` Pods — which were scaled to 3 replicas.

**Load Balancing:**
The Service automatically load-balances traffic across these Pods.

---

### ✅ Other Fields

| Field                                | Meaning                                                |
| ------------------------------------ | ------------------------------------------------------ |
| **Session Affinity: None**           | Traffic is not sticky — each request may go to any Pod |
| **IP Families: IPv4**                | Uses traditional IPv4 networking                       |
| **IP Family Policy: SingleStack**    | Only one IP family (no IPv6)                           |
| **Internal Traffic Policy: Cluster** | Any node in the cluster can route to these pods        |

---

## 🧠 Summary

Your `nginx-deployment` Service:

* Is accessible via **ClusterIP:** `10.106.68.184`
* Exposes **port 8080** inside the cluster
* Routes to 3 **nginx Pods** on **port 80**
* Handles traffic **automatically** even if Pods are added, removed, or restarted

---

