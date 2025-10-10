# SSH 

Secure Shell is a way to remotely access a server. 
the basic way in which you do ssh is as follows : 
```bash 
ssh <name-of-host>@<ip-address-of-host>
```

Most times after you do it this way, since there will always be a sudo access reserved by password, it will well ask for password 

ALso if you want to ssh into server you need `openssh` services installed in it


<-- **KeyConcepts : Passwordless ssh** --->

Passwordless ssh is needed in order for smoother access to server to a devloper 
But since the access should be restricted only to the devloper's piecece, you cannot simply remove password from server (-Major Security Hazard-)
Hence here are the steps to do passwordless ssh 
- using keygen-ssh to genrate pair of public keys and private keys 
- copy the public key to the server 
- then you can ssh remotely viola

```bash
ssh-keygen -t rsa -b 4096 -C "yashbav24@gmail.com"
````

- `ssh-keygen` : Used to connvert, manage and genrate authenticication key 
- `-t rsa` : -t -> Type of Keys to create 
rsa : RSA alogorithm 
- `b` number of bits 
 `4096` -> strong   ad high secuity 
 - `-C` comment flag to identitfy later 

- Stores it here if left deafult : `/home/ygb/.ssh/id_rsa`
(deafult)

```bash
ssh-copy-id yash@192.168.0.178
```

This will copy id to the server and store it in authenticication 

After that you can directly log in to ssh without password :

```bash
ssh yash@192.168.0.178
```



### Remote Command Execution 

Commands can be executed on the server with just 
```bash
ssh user@<ip-address-of-server> [commands]
```

for example : 
```bash 
ssh user@192.168.0.178 "uname && uptime"
```


### File transfer using SFTP 