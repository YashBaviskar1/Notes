
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





##### Answers 
