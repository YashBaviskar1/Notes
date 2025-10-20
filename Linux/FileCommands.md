# File system Navigation 




## 🟩 **2. File System Navigation & File Operations**

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

### Answers 

1) `pwd` shows the current path of the current directory ("where am i" in the syste)

2) The command `mv file1 /dir/` -> moves the file one to the `/dir/`
whereas the command `mv /dir/file1 ,` --> brings that file from that specified `/dir/` to the current directory.

3) In order to recursivly copy a directory from one place as well as its contents inside it you can use `cp -r source_dir/ destionation_dir/` 

4) `.` indicates current dirctory where the terminal is pointing to, whereas `..` referes to previous directory with respect to current one 


Intermediate 

5) 


