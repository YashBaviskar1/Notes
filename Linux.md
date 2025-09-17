# Quick Notes for Linux


### Fedora 42 

Linux distribution of fedora project, continued by Red Hat Linux Project 

- Ubuntu uses APT package manager to provide and manage software (applications, libraries and other required codes) while Fedora uses DNF package manager.

-  Fedora on the other hand focuses on providing only open-source software.




### Commands to get known 

```bash
cat /etc/fedora-release
```



```bash 
dnf update -y
```
- note : fedora uses dnf packages 


- adding new user and giving mod access 
```bash
adduser yash
passwd yash 
usermod -aG wheel yash 
```



## SELinux 

- it is security enhanced linux which basically a security module inbuilt in Linux Kernal 

- It enforces Mandatory Access Control (MAC) on top of normal Linux permissions (chmod/chown).

- enforcing by default in fedora 



## Check Logs for Security Reules

```bash 
jorurnalctl -t trobuleshoot 
```

