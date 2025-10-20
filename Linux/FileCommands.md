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

5) The way to approch this is in two parts, one part is 'how to find and isolate file with certain extension or name'.
There is a universal command in linux to find files which is `find` command. 
The basic way in which find commands works is 
```bash
find [options] [path..] [expression]
```
Where options control the symbolic links, debugging options and optimization method 

for `options`
the methods are 
- `-L` which is used to follow the symbolic link while traversing the directores 

- `-P` : deafult behaviour of not following th symbolic links 

- The Optimisation Flags `-O1 -O2 -O3` based on the level of performance and safety, by deault `O1` is considered but for Large and VERY huge directors `O2 and O3` might be used for fastest possible result 

- `-D` showcases the debug level for the which has these various levels 
```bash 
Valid arguments for -D:
exec       Show diagnostic information relating to -exec, -execdir, -ok and -okdir
opt        Show diagnostic information relating to optimisation
rates      Indicate how often each predicate succeeded
search     Navigate the directory tree verbosely
stat       Trace calls to stat(2) and lstat(2)
time       Show diagnostic information relating to time-of-day and timestamp comparisons
tree       Display the expression tree
all        Set all of the debug flags (but help)
help       Explain the various -D options
```



- **Path** : the path showcases the starting directory from where it will start the search 

- **expression** : options, search patterns, operators etc 


Now there are various flags by which we can search the file name by its extension, the useful one in this case is `-name`
and we can also specify the -`type` what we want to find the common descriptors are : 
- `f`: a regular file
- `d`: directory
- `l`: symbolic link
- `c`: character devices
- `b`: block devices
- `p`: named pipe (FIFO)
- `s`: socket

So to find files with `.log` extension we use : `-type f` and `-name "*.log"` which will help us find all the .log files 

But if we want to find it system wide it is important to understand that it can get really cluttered with permissiond denied errors to a neat trick is to hide all the `stderr` using this line `2>/dev/null` what does do is put all the stderr stream to a null device file which hides it 

So our command till now has become  : 
`find / -type f -name "*.log"`

But the important distinction now to find the files **modified in last 24 hours**
For this we will use another flag `-mtime N` which basically finds files by modification date, so for within 24 hours we can use `-1` (within a day ), hence we get our final output as : 
```bash
find / -type f -name "*.log" -mtime -1 2>/dev/null
```
