
---

## **1. SSH, VPN, and Remote Access**

**Basic**

1. What’s the difference between `ssh user@ip` and `ssh -i key.pem user@ip`?
2. How can you copy a file from your local machine to a remote server using SSH?
3. What port does SSH use by default? How would you connect if it’s running on a different port?
4. How do you keep an SSH session alive if it keeps timing out?

**Intermediate**

5. You want to log in without entering a password each time. How would you set up SSH key-based authentication?
6. What is an SSH tunnel and when might you use one in production?
7. You’re connected over SSH and your network dies — how can you prevent losing long-running commands?

**Advanced**

8. How would you securely restrict SSH access to specific users or IP addresses?
9. What’s the difference between a VPN and SSH tunneling for remote access?
10. Your SSH connection is slow or laggy — what steps would you take to debug latency issues?

---

##  **2. File System Navigation & File Operations**

**Basic**

1. What does `pwd` do?
2. What’s the difference between `mv file1 /dir/` and `mv /dir/file1 .`?
3. How do you recursively copy a directory from one location to another?
4. What’s the purpose of `.` and `..`?

**Intermediate**

5. How do you find all `.log` files modified in the last 24 hours?
6. How can you delete all files larger than 500MB in `/var/log` safely?
7. What’s the difference between `>` and `>>` in file redirection?

**Advanced**

8. How can you find which directory is taking the most space on a Linux server?
9. Explain what happens internally when you execute `cat file.txt | grep "error" | sort | uniq -c`.
10. How can you copy files between two remote servers without downloading them locally?

---

##  **3. Package Management (yum/dnf)**

**Basic**

1. How do you install and remove a package using `yum` or `dnf`?
2. How can you list all installed packages?
3. What’s the difference between `yum update` and `yum upgrade`?

**Intermediate**

4. How would you find out which package provides a certain binary (e.g., `/usr/bin/python3`)?
5. How do you exclude specific packages from being updated?
6. If you face “metadata expired” errors, what’s your first troubleshooting step?

**Advanced**

7. How do you roll back a package to a previous version using yum history?
8. How can you create your own local yum repository?
9. What’s the difference between `yum` and `dnf` in RHEL 8+ systems?

---

## **4. Permissions & Ownership**

**Basic**

1. What’s the meaning of these permissions: `-rw-r--r--`?
2. How do you change the owner of a file?
3. How do you give execute permission to a user?

**Intermediate**

4. What’s the difference between symbolic and numeric modes in `chmod`?
5. How would you recursively give a directory and all subfiles read/write to a specific group?
6. What does `umask` control?

**Advanced**

7. What are SUID, SGID, and sticky bits? Give examples.
8. Why can `chmod 777` be dangerous in production?
9. You have a shared directory for developers — how would you configure it so that files created by one dev are editable by others in the group?

---

## **5. Text Editors (vim/nano)**

**Basic**

1. How do you enter insert mode in vim?
2. How do you save and quit?
3. How do you search for a keyword in vim?

**Intermediate**

4. How do you delete all lines containing a specific string?
5. What’s the difference between `:w!` and `:wq!`?
6. How do you copy and paste multiple lines?

**Advanced**

7. How would you open multiple files in vim and switch between them?
8. How can you record and replay macros?
9. How do you configure `.vimrc` to auto-indent code?

---

## **6. Monitoring System Resources**

**Basic**

1. What’s the difference between `top` and `htop`?
2. How do you check free memory and swap usage?
3. What does `df -h` show?

**Intermediate**

4. How do you find the process consuming the most CPU?
5. What’s the difference between load average and CPU utilization?
6. How do you check when the system was last rebooted?

**Advanced**

7. How can you monitor disk I/O or network usage in real-time?
8. How would you identify memory leaks in a running process?
9. How can you find zombie or defunct processes?

---

##  **7. Process Management**

**Basic**

1. How do you list all running processes?
2. What’s the difference between `kill`, `killall`, and `pkill`?
3. How do you bring a background process back to foreground?

**Intermediate**

4. What are `jobs`, `fg`, and `bg` commands used for?
5. How do you kill all processes of a specific user?
6. What does `nohup` do?

**Advanced**

7. How can you check the parent process of a running PID?
8. What is a “zombie process”?
9. How would you schedule a process to restart automatically if it dies?

---

## **8. Services & systemd**

**Basic**

1. How do you check the status of a service?
2. How do you start, stop, and restart a service?
3. How do you enable a service to start on boot?

**Intermediate**

4. How can you see logs for a specific service using `journalctl`?
5. What’s the difference between `enable` and `start`?
6. How would you reload systemd after creating a new service file?

**Advanced**

7. Write an example systemd unit file for a Python app.
8. How do you create dependencies between services (e.g., DB starts before app)?
9. How can you set resource limits (CPU, memory) for a service?

---

##  **9. Users & Groups Management**

**Basic**

1. How do you create and delete a user?
2. What’s the difference between `/etc/passwd` and `/etc/shadow`?
3. How do you add a user to a group?

**Intermediate**

4. How do you lock and unlock a user account?
5. How do you change a user’s shell?
6. What is the purpose of `/etc/skel`?

**Advanced**

7. How can you enforce password complexity and expiration?
8. How do you create a system (non-login) user for a service?
9. How do you list all users currently logged in?

---

##  **10. Networking & Firewall**

**Basic**

1. How do you check your IP address?
2. How do you test connectivity to another server?
3. How do you see which ports are open?

**Intermediate**

4. How do you add or remove firewall rules in `firewalld`?
5. What’s the difference between `iptables` and `firewalld`?
6. How do you find which process is using a specific port?

**Advanced**

7. How do you permanently open port 8080 using `firewalld`?
8. How would you debug if a port is open locally but unreachable remotely?
9. What’s the difference between NAT and port forwarding?

---

## **11. Log Management**

**Basic**

1. Where are most system logs stored on RHEL?
2. How do you view the last 50 lines of a log file?
3. How do you continuously monitor logs in real time?

**Intermediate**

4. How do you rotate logs manually?
5. What’s the role of `rsyslog`?
6. How do you find all logs related to a specific process?

**Advanced**

7. How would you configure custom log rotation for a service?
8. How can you send logs to a remote syslog server?
9. How do you monitor log growth and alert if a log exceeds a certain size?

---

##  **12. Security & SELinux**

**Basic**

1. How do you check if SELinux is enabled?
2. What are the three SELinux modes?
3. What happens if SELinux blocks a process?

**Intermediate**

4. How do you temporarily disable SELinux?
5. How do you view and interpret SELinux denial logs?
6. What’s the difference between enforcing and permissive modes?

**Advanced**

7. How can you allow a service (e.g., Nginx) to access a specific directory under SELinux?
8. How do you create a custom SELinux policy module?
9. Why is disabling SELinux a bad idea in production?

---

##  **13. Cron Jobs**

**Basic**

1. How do you list existing cron jobs for a user?
2. What’s the syntax for a cron expression?
3. How do you create a cron job that runs every 5 minutes?

**Intermediate**

4. How can you ensure a cron job logs its output?
5. How do you run a script daily at 2 AM?
6. How can you temporarily disable a cron job?

**Advanced**

7. How do you run a cron job with a specific user environment (e.g., Python path)?
8. What’s the difference between system-wide cron and user crontabs?
9. How can you monitor if cron jobs fail or hang?

---

Excellent — that’s a **very practical direction**.

If your company focuses heavily on **Docker image management, debugging, optimization, and deployment**, you’ll want to know Docker *inside out* — not just how to build and run containers, but how to **debug**, **analyze**, and **optimize** them in real-world production conditions.

Here’s a curated progression of **questions in increasing difficulty**, focused entirely on **Docker** (no Compose), tuned for **deployment, debugging, CI/CD, and production server management**.

---

# 🟦 **Docker — Complete Real-World Question Set**

---

## 🟩 **1. Core Concepts & Basics**

**Basic**

1. What is Docker, and how does it differ from a virtual machine (VM)?
2. What’s the difference between a Docker **image** and a **container**?
3. What’s the default Docker network mode?
4. What happens internally when you run `docker run ubuntu:latest bash`?
5. How can you list all running and stopped containers?
6. How can you remove all stopped containers and unused images?

**Intermediate**

7. What’s the difference between `docker run`, `docker start`, and `docker exec`?
8. What happens if you stop a container — does it delete data?
9. How would you mount a host directory inside a running container?
10. Explain what happens behind the scenes when pulling an image from Docker Hub.

**Advanced**

11. What’s the purpose of the Docker daemon (`dockerd`) and client (`docker`)?
12. Explain the architecture of Docker (Daemon, CLI, REST API, containerd, runc).
13. Why is Docker considered more lightweight than VMs at a kernel level?

---

## 🟩 **2. Docker Images & Layers**

**Basic**

1. How do you list all Docker images on your system?
2. What’s the difference between `docker build` and `docker pull`?
3. What is a Docker image tag, and why do we use it?

**Intermediate**

4. Explain the concept of **image layers** in Docker.
5. What does the `docker history` command show?
6. What happens if you rebuild an image — does Docker reuse previous layers?
7. What’s the difference between `latest` and a specific version tag? Why can relying on `latest` be dangerous in production?

**Advanced**

8. How can you reduce the size of a Docker image?
9. What’s the difference between **multi-stage builds** and regular builds?
10. How can you inspect an image’s environment variables and configuration without running it?
11. How would you verify if an image was built securely or signed (e.g., via Docker Content Trust)?

---

## 🟩 **3. Dockerfile Deep Dive**

**Basic**

1. What’s the purpose of a `Dockerfile`?
2. Explain the difference between `RUN`, `CMD`, and `ENTRYPOINT`.
3. What does `COPY` do, and how is it different from `ADD`?
4. What does the `WORKDIR` instruction do?

**Intermediate**

5. How can you pass build-time variables into a Dockerfile?
6. What’s the difference between `ARG` and `ENV`?
7. How do you reduce the number of layers created in a Dockerfile?
8. Why might you use `.dockerignore`, and what happens if you forget it?

**Advanced**

9. Write a Dockerfile for a Python web app that uses a virtual environment and runs via Gunicorn, optimized for production.
10. What are **multi-stage builds**, and how do they improve image security and performance?
11. Explain what happens during the **build cache** process — when is a layer reused and when is it invalidated?
12. Why is it important to pin base image versions (e.g., `FROM python:3.11-slim` instead of `FROM python:latest`)?
13. How do you debug a failing Docker build step?

---

## 🟩 **4. Running & Managing Containers**

**Basic**

1. How do you run a container interactively vs. detached mode?
2. How can you view logs of a running container?
3. How can you enter a running container’s shell?

**Intermediate**

4. How can you restart a container automatically if it crashes?
5. How do you expose a container port to the host system?
6. What’s the difference between `docker stop`, `docker kill`, and `docker rm`?
7. How can you check which ports are being used by running containers?

**Advanced**

8. How can you attach a debugger or exec into a container that’s stuck or unresponsive?
9. What happens internally when you run `docker exec -it container /bin/bash`?
10. If a container is failing immediately after starting, how would you debug it?
11. How can you check a container’s exit code and reason for termination?
12. How do you use Docker events (`docker events`) for debugging container lifecycle issues?

---

## 🟩 **5. Networking & Volumes**

**Basic**

1. What’s the default network driver in Docker?
2. What’s the purpose of the `bridge`, `host`, and `none` network modes?
3. How do you inspect a container’s IP address?

**Intermediate**

4. How do you connect two containers to the same custom network?
5. How can a container access a service running on the host machine?
6. How do volumes differ from bind mounts?
7. How can you check which volumes exist on your system?

**Advanced**

8. How would you back up data stored in a named volume?
9. How do you clean up dangling or orphaned volumes?
10. How do you troubleshoot a container that cannot reach another one in the same network?
11. How can you create a read-only volume mount?

---

## 🟩 **6. Private & Public Registries**

**Basic**

1. What’s the difference between Docker Hub and a private registry?
2. How do you log in to a Docker registry?
3. How do you tag and push an image to a registry?

**Intermediate**

4. How can you pull an image from a private registry securely?
5. How do you remove credentials from your local system after use?
6. How do you handle authentication when using a registry in CI/CD?

**Advanced**

7. How would you set up your own internal Docker registry (e.g., using `registry:2` image)?
8. How can you enable HTTPS and authentication for your private registry?
9. How do you mirror a public image into your internal registry for offline deployments?
10. How can you sign and verify images using Docker Content Trust (`DOCKER_CONTENT_TRUST=1`)?

---

## 🟩 **7. Debugging & Troubleshooting (Real Deployment Level)**

**Basic**

1. How can you see container logs in real-time?
2. What does `docker inspect` show you?
3. How do you find which files or ports a container is using?

**Intermediate**

4. Your container exits right after running — how do you debug what happened?
5. How can you view environment variables of a running container?
6. How can you check the CPU and memory usage of a container?
7. How do you restart a container that crashed automatically?

**Advanced**

8. How can you trace system calls or processes inside a container?
9. How do you debug DNS or network resolution failures inside a container?
10. A container works locally but fails in production — what’s your step-by-step debugging approach?
11. How can you compare differences between two image versions?
12. What’s the difference between `docker stats`, `docker top`, and `docker inspect` for troubleshooting performance?

---

## 🟩 **8. Security & Best Practices**

**Basic**

1. Why is it bad practice to run containers as root?
2. How can you specify a non-root user in a Dockerfile?
3. How can you scan images for vulnerabilities?

**Intermediate**
4. What are the risks of mounting the Docker socket (`/var/run/docker.sock`) inside containers?
5. How can you limit CPU and memory usage of a container?
6. How do you prevent sensitive data (like credentials) from leaking into image layers?

**Advanced**
7. What’s the difference between `USER` and root privilege escalation in containers?
8. How can you enable AppArmor or SELinux profiles for Docker containers?
9. How do you detect and remove outdated or vulnerable images from your registry?
10. How can you sign and verify container images for secure deployment pipelines?

---

## 🟩 **9. Deployment & Optimization**

**Basic**

1. How can you make a container restart automatically after reboot?
2. What’s the difference between `--restart=always` and `--restart=on-failure`?
3. How can you persist logs outside a container?

**Intermediate**
4. How do you version Docker images in CI/CD pipelines?
5. How can you pass secrets (like API keys) into containers securely?
6. How do you reduce cold start time when deploying containers at scale?

**Advanced**
7. How would you handle “ImagePullBackOff” or “CrashLoopBackOff” errors in deployment?
8. How can you optimize Docker builds in CI/CD to avoid rebuilding unchanged layers?
9. How would you ensure your base images are always up to date without breaking builds?
10. What strategies would you use to handle zero-downtime deployments with Docker (without Compose or Kubernetes)?

---

Would you like me to **convert this into a practical quiz mode** next —
for example, starting with a real-world problem like

> “Your container fails to start after build, logs show `/bin/bash not found`. What’s your debugging approach?”

and then progressively move through debugging, image optimization, and registry management — as if you were *on-call for production deployment*?
That style is best if your goal is to reach *production debugging* proficiency.
