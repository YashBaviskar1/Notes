
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