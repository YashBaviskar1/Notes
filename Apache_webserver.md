# Apache web server 

### This is a notes repository for Apache web server 



#### What is Apache 

Apache is a HTTPD Web Server which helps to serve web pages to users over the internet 

It processes requests from browsers and serves websites using the HTTP Protocol 



- making a local html page which is locally accessible  


- handles HTTP protocal and D -> handles Daemon services as well  

- server index.html 

- (Nginx, Apache, Cloudflare Server )


- Hosting static websites, DYnamic content, reverse proxy, load balancings, multiple website host on same server, 
custom domain configuration 



### Installing Apache Web Server : 

```bash
yum install httpd
```

```bash
apt install apache2
```

#### Start HTTPD service 
```bash 
systemctl start httpd 
```


#### Enable HTTP service firewalld
```bash 
sudo firewall-cmd --permenant --add-service=http
```

#### Access deafult website from browser 
- Config 
```bash 
/etc/httpd/conf/httpd.conf #centos
/etc/apache2/apach2.cong #ubuntu
```

- in order to server static pages initlially it can be done so through 
/var/www/html 



### Configuration File Description 



- **Server Root** : top of the directory tree under which the server's configuration, error, and log files are kept 

(Do not add alash at then end of directory path)


- Listen : Allows to change bind Apache to specific IP addresses or ports, instead of deafult

- Dynamic Shared Object (DSO) Support : To be able to use the functionality of a module which has built as a DSO you have to place the corresponding 'LoadModule   ` lines at this location so the directives contained in it are actually avaliable before they are used, Statically complied mocules do not need to be laoded here



- ServerAdmin

- Registered DNS< specific port>


- Directory : expliclit permissions 


- Document Root 

- DirectoryIndex index.html ---> to find that file 


LogLeve warn 


-log_config_module 


#### HTTP Logging 
```
/var/log/httpd/access_log 
```
```
/var/log/httpd/error_log
```


It is very important to understand that
