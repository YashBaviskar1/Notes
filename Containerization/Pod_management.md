# Kubernetes Pod Management - Quick Notes

## Pod Creation & Management Commands

### 1. Create Nginx Pod
```bash
kubectl run nginx --image=nginx
```
- **Purpose**: Create a pod running nginx container
- **Syntax**: `kubectl run <pod-name> --image=<container-image>`
- **Output**: `pod/nginx created` - Pod created successfully
- **What happens**: Kubernetes pulls nginx image and creates pod

### 2. Monitor Pod Status
```bash
kubectl get pods
```
- **Multiple executions show pod lifecycle**:
  - `ContainerCreating` → Pod being initialized
  - `Running` → Pod successfully started
- **READY column**: `1/1` means 1 container ready out of 1 total

### 3. Detailed Pod Information
```bash
kubectl describe pod nginx
```
- **Purpose**: Get comprehensive pod details
- **Key information revealed**:
  - **Node assignment**: `minikube/192.168.49.2`
  - **Pod IP**: `10.244.0.3` (internal cluster IP)
  - **Container status**: Running, restarts, image details
  - **Events timeline**: Scheduling → Pulling image → Creating → Starting
  - **Labels**: `run=nginx` (auto-assigned by `kubectl run`)

### 4. SSH into Minikube & Container Inspection
```bash
minikube ssh
docker ps | grep nginx
```
- **Findings**: Two containers for the pod:
  - **nginx container**: Main application container
  - **pause container**: Infrastructure container for networking namespace

### 5. Exec into Container
```bash
docker exec -it ec27f94634d4 sh
```
- **Commands inside container**:
  - `hostname` → Shows pod name "nginx"
  - `hostname -i` → Shows internal IP `10.244.0.3`
  - `curl 10.244.0.3` → Success! Nginx responds with welcome page
- **Demonstrates**: Pod networking works internally

### 6. Pod Networking Discovery
```bash
kubectl get pods -o wide
```
- **Option**: `-o wide` shows additional details including IP and node
- **Output**: Confirms pod IP `10.244.0.3` on minikube node
- **External access test**: `curl 10.244.0.3` fails from host
- **Reason**: Pod IPs are internal to cluster, not accessible from outside

### 7. Pod Deletion
```bash
kubectl delete pod nginx
```
- **Purpose**: Remove the nginx pod
- **Output**: Pod deleted from default namespace
- **Verification**: `kubectl get pods` shows no resources

### 8. Create Alias for Efficiency
```bash
alias k="kubectl"
```
- **Purpose**: Shorten frequently used command
- **Usage**: `k get pods` instead of `kubectl get pods`

## Key Concepts Demonstrated

### Pod Lifecycle States
1. **ContainerCreating** → Kubernetes setting up the pod
2. **Running** → Pod successfully operational
3. **Terminating** → When deletion initiated

### Container Architecture in Pods
- **Main container**: Runs the actual application (nginx)
- **Pause container**: Manages networking namespace and shared resources
- **Each pod gets unique IP** within cluster network

### Networking Isolation
- **Pod IPs (10.244.0.0/16)**: Internal cluster network only
- **External access**: Requires Service (LoadBalancer/NodePort) or Ingress
- **Internal connectivity**: Containers can communicate via pod IPs

## Quick Command Reference Table

| Command | Purpose | Key Options | Important Output |
|---------|---------|-------------|------------------|
| `kubectl run nginx --image=nginx` | Create pod | `--image` specifies container | Pod creation status |
| `kubectl get pods` | List pods | None | Pod status & readiness |
| `kubectl describe pod <name>` | Pod details | None | IP, events, conditions |
| `kubectl get pods -o wide` | Extended pod info | `-o wide` | IP, node, more columns |
| `kubectl delete pod <name>` | Remove pod | None | Deletion confirmation |
| `minikube ssh` | Access node | None | Direct node access |
| `docker exec -it <id> sh` | Container shell | None | Interactive container access |

## Troubleshooting Insights
- **Pod IP inaccessible externally**: Normal behavior, requires Service
- **ContainerCreating state**: Image pulling phase
- **Multiple containers per pod**: Infrastructure + application containers
- **Events section in describe**: Chronological troubleshooting timeline

## Next Steps for External Access
To make nginx accessible from outside the cluster, you would need to create a Service:
```bash
kubectl expose pod nginx --type=NodePort --port=80
```
Or use LoadBalancer service type for cloud environments.