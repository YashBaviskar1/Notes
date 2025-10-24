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



### Remote Access & File Transfer


####  Install and enable SSH Server on Fedora VM 

```bash
sudo dnf install -y openssh-server

sudo systemctl enable sshd --now

systemctl status sshd
```


### Firewall add to ssh 

To ensure fedora firewall allows ssh 
```bash 
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

## SFTP 

SFTP (Secure File Transfer Protocol) runs over SSH.

It lets you upload, download, and manage files securely between your client and server 


File Transfer module

Local Mzchine -> server
```bash 
scp myfile.txt username@192.168.1.50:/home/username/
```


server -> localmachine
