

# Cluster Recvory 



## Background checks 

```bash
kubectl cluster-info
```

output : 
```
Kubernetes control plane is running at https://127.0.0.1:6443
CoreDNS is running at https://127.0.0.1:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://127.0.0.1:6443/api/v1/namespaces/kube-system/services/https:metrics-server:https/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```





### Check etcd Manifests 

```bash
 sudo cat /etc/kubernetes/manifests/etcd.yaml
```

look at Volume & Volume Mounts Section 
```bash
    volumeMounts:
    - mountPath: /var/lib/etcd
      name: etcd-data
    - mountPath: /etc/kubernetes/pki/etcd
      name: etcd-certs

  - hostPath:
      path: /etc/kubernetes/pki/etcd
      type: DirectoryOrCreate
    name: etcd-certs
  - hostPath:
      path: /var/lib/etcd
      type: DirectoryOrCreate
    name: etcd-data
```




understanding etcd pod 
```bash
kubectl get po -n kube-system
```

to look for `etcd-localhost.localdomain`



Exec and check if etcdctl exists
```bash
yash@localhost:~$ kubectl exec -n kube-system -it etcd-localhost.localdomain -- sh
sh-5.2# etcdctl version
etcdctl version: 3.5.16
API version: 3.5
sh-5.2#
```




snapshot : 
```bash
kubectl exec -n kube-system etcd-localhost.localdomain -- sh -c '
ETCDCTL_API=3 etcdctl \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /var/lib/etcd/snapshot.db
'
```



check if it exists :

```bash
yash@localhost:~$ sudo ls -lh /var/lib/etcd/snapshot.db
-rw-------. 1 root root 3.3M Feb 20 13:17 /var/lib/etcd/snapshot.db
yash@localhost:~$
```



copying snapshot to a safe location 

```bash
sudo cp /var/lib/etcd/snapshot.db /home/yash/etcd-backup/snapshot.db
```

changing its ownership 

```
sudo chown yash:yash /home/yash/etcd-backup/snapshot.db
```



CRASH THE NODE :
```
sudo rm -rf /var/lib/etcd
```





Restoring with etcd pacakge 
```bash
sudo dnf install etcd -y
```


etcd should not exist 
```bash
sudo crictl ps | grep etcd
```

kubelet and containerd service should be stopped 
```bash
sudo systemctl stop containerd
 sudo systemctl stop kubelet
```

delete old data  :
```bash
sudo rm -rf /var/lib/etcd
```

get the urls  :
```bash
sudo grep -E "name=|initial-cluster=|initial-advertise-peer-urls=" /etc/kubernetes/manifests/etcd.yaml
```

fix permissions : 
```bash
sudo chown -R root:root /var/lib/etcd
```

start services :
```
 sudo systemctl start containerd kubelet
 ```
restore SELINUX policy  :
```bash
sudo restorecon -Rv /var/lib/etcd
```

restore 
```bash
 sudo ETCDCTL_API=3 etcdctl snapshot restore /home/yash/etcd-backup/snapshot.db   --name=localhost.localdomain   --initial-cluster=localhost.localdomain=https://192.168.0.106:2380   --initial-advertise-peer-urls=https://192.168.0.106:2380   --initial-cluster-token=etcd-cluster-1   --data-dir=/var/lib/etcd
```






















```bash
yash@localhost:~/etcd-backup$ sudo systemctl stop kubelet containerd
sudo rm -rf /var/lib/etcd
yash@localhost:~/etcd-backup$ sudo grep -E "name=|initial-cluster=|initial-advertise-peer-urls=" /etc/kubernetes/manifests/etcd.yaml
    - --initial-advertise-peer-urls=https://192.168.0.106:2380
    - --initial-cluster=localhost.localdomain=https://192.168.0.106:2380
    - --name=localhost.localdomain
yash@localhost:~/etcd-backup$ sudo ETCDCTL_API=3 etcdctl snapshot restore /home/yash/etcd-backup/snapshot.db \
  --name=localhost.localdomain \
  --initial-cluster=localhost.localdomain=https://192.168.0.106:2380 \
  --initial-advertise-peer-urls=https://192.168.0.106:2380 \
  --initial-cluster-token=etcd-cluster-1 \
  --data-dir=/var/lib/etcd
Deprecated: Use `etcdutl snapshot restore` instead.

2026-02-20T13:39:16+05:30       info    snapshot/v3_snapshot.go:260     restoring snapshot      {"path": "/home/yash/etcd-backup/snapshot.db", "wal-dir": "/var/lib/etcd/member/wal", "data-dir": "/var/lib/etcd", "snap-dir": "/var/lib/etcd/member/snap"}
2026-02-20T13:39:16+05:30       info    membership/store.go:141 Trimming membership information from the backend...
2026-02-20T13:39:16+05:30       info    membership/cluster.go:421       added member    {"cluster-id": "a6e86a414d937467", "local-member-id": "0", "added-peer-id": "75707fc4b2417a53", "added-peer-peer-urls": ["https://192.168.0.106:2380"]}
2026-02-20T13:39:16+05:30       info    snapshot/v3_snapshot.go:287     restored snapshot       {"path": "/home/yash/etcd-backup/snapshot.db", "wal-dir": "/var/lib/etcd/member/wal", "data-dir": "/var/lib/etcd", "snap-dir": "/var/lib/etcd/member/snap"}
yash@localhost:~/etcd-backup$ sudo chown -R root:root /var/lib/etcd
sudo restorecon -Rv /var/lib/etcd
yash@localhost:~/etcd-backup$ sudo systemctl start containerd kubelet
yash@localhost:~/etcd-backup$ kubectl get nodes
Unable to connect to the server: stream error: stream ID 1; INTERNAL_ERROR; received from peer
yash@localhost:~/etcd-backup$ kubectl get nodes
NAME                    STATUS   ROLES           AGE   VERSION
localhost.localdomain   Ready    control-plane   49m   v1.29.15
yash@localhost:~/etcd-backup$ kubectl get ns
NAME              STATUS   AGE
default           Active   49m
kube-node-lease   Active   49m
kube-public       Active   49m
kube-system       Active   49m
redis             Active   34m
yash@localhost:~/etcd-backup$ kubectl get po -n redis
NAME                            READY   STATUS    RESTARTS        AGE
redis-deploy-67df7dd58b-4564f   1/1     Running   1 (9m21s ago)   34m
yash@localhost:~/etcd-backup$
```


