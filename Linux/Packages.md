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
#### Answers

1. `dnf` is a package manager of fedora used to install, update, remove packages , its full form ins dandified YUM, it is a successor of `yum` 
- `yum` was the package manager of previous fedora versions 

to install something using `dnf` you do : 
```bash 
sudo dnf install nyancat
```

You can also view info of your installed packages by : 
```bash 
sudo dnf info <package>
```



to delete a package you can do : 
```
dnf remove <package=name>
```


2) to list all the installed packagaes one can do : 
``` 
dnf list
```

and it will list all the packages 
for a specific package 

and you can even search 
```bash 
dnf search <package>
```


3) Package manager `yum` is used to install, remove, update and delete the software packages 
before installing we usually do 
```bash
yum update
```
or 
```bash
yum upgrade
```

Both commands are basically same but what `yum update` does is -> updates the presently installed packages 

`yum upgrade` does the same thing but after updatating it also removes the obselete packages in the system, the speciality about upgrade is it will modify the internal dependicies as well (install or remove packages)

for routine updates `yum update` is suffice but for brining it upto date, we can use `yum upgrade` 





**INTERMEDIATE**

4) `rpm` is the core management system of fedora, `rpm` can be used to install as well and `yum/dnf` is built on top of it, 
To see any binary or a file to which package it is exactly dependent one can use 
```bash
rpm -qf /usr/bin/python3
```

Here the flags `-q` are for querying, which brings to the rpm query mode 
and `-f` is the is to indicate that we are pointing to a file to verify/query



5) To exclude certain files from being updated, changed when we do update & upgrade operations 

- For YUM package manager, we can have a `--exclude=` flag which will directly exclude these packages from being updated temporarily.

- For More permenanant solution we have to change the conf file of the `yum` which is in `/etc/yum/yum.conf` where we need to add something like this  :
```
exclude=kernel* redhat-release* php* mysql* httpd* 
```

to exclude any package that starts with kernal, redhat-release, php, mysql, httpd etc 

- For DNF, it is slightly different 
`–exclude=package1,package2,package3` for temoporary command 
but for permenenat solution the config file in `/etc/dnf/dnf.conf`

```text
excludepkgs=[package1, package2]
```
Will be used essentially  



**Advanced**

7) We can see the history of the commands that were executed  
```bash
dnf historylist 
```
Then in order to `rollback` or `undo` we can use : 

```bash
dnf history rollback ID
```
```
dnf history undo ID 
```
rollback -> will rollback all the commands will that specific id 
undo -> will undo that specific command to that id 




