# File system Navigation 




## **2. File System Navigation & File Operations**

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



6) "Deleting All files larger than 500MB inside `/var/log` "safely"

- at first from our previous understanding we can use find command to find files larger than 500MB in a specific diretory, by using `-size` flag 

- we know deleting stuff in linux is `rm` 

- we have to combine the `find` and `rm` command -> in order to do that we can use `xargs` command 

the basic way in which `xargs` work is 
```bash 
[some command that produces output] → xargs → [another command using that output as arguments]
```

It's basic syntax is : 
```bash 
command1 | xargs [options] command2
```
the options it has are 
| Option          | Meaning                                                |
| --------------- | ------------------------------------------------------ |
| `-n N`          | Run the command **N items at a time**                  |
| `-I {}`         | Use `{}` as a placeholder for each item                |
| `-0` / `--null` | Handle filenames with spaces (use with `find -print0`) |

to combine it with find we can hence do 
```bash 
find /var/log -type f -name "*.log" -size +100M 2>/dev/null | xargs rm -i
```

(After trying this out there is a werid interactive issue due to the batch processing, file output handling)

In order to "safely" : we can use `-exec` flag in order to treat the output one-by-one :
the basic syntax for that is : 
```
find [path] [arguments] -exec [command] {} \;
```
what does this do is, the output is used in placeholer `{}` and `\` indicates to execute in the next line, 
you can also use : 
```
find [path] [arguments] -exec [command] {} +;
```
for combining the file outputs into a single command  

Hence combining with our question the final result for 
"safely deleteing files larger than 500MB in /var/log" wil be : 
```
find /var/log -type f -size +500M -exec rm -i {} \;
```
which will safely delete by interactivly asking user to confirm the deletion, 
since var/log/ is usually temp and safe to delete we can also directly delete is by : 
```
find /var/log -type f -size +500M -exec rm -rf {} \;
```

----------------

7) `>` and `>>` are called output redirections, they essentially control the output of the command. 
- `>` is for overwrite 
- `>>` is for append 

once of the basic ways it works as : 
```bash
echo "Hello there" > file1.txt
```
```bash
echo "Hello there" > file1.txt
```
output : 
```
Hello There
```


```
echo "Hello there again" >> file1.txt
```
output :
```
Hello there 
Hello there again
```

----------------------------------- 
Advanced 
8) To find which directory takes up most space in linux server 

There are couple of ways where you can see the sapce of the directory of the linux server, we can use the traditional `find` but instead we can also simply use 
`du` which essentially talks about disk usage of the system, you can directly ask for the directories that consume space in human readable form 

you can combine it with `sort` and `head` to see the top most space consuming directores hence 
```bash
du -h | sort -rh | head -n 10
```

`-rh` is reverse sorting in descending order 


9) Understanding how the pipe opeations work essentially 
- We Assume we have a `file.txt` with this type of text inside it : 
```bash
yash@localhost:~/test$ cat file.txt
test
test
test1
test2
test2
error : disk failed
error : error in conf file
error : disk failed
error : disk failed


yash@localhost:~/test$
```

Now in order to to understand let's see we want to see the occurances of all the unique errors hence we get : 
```
cat file.txt | grep "error" 
```

this will grab the lines that have error in them 

Now in order to use `uniq` which is a filter command for repeated lines which are adjacent to each other (important)

Hence : 
```
cat file.txt | grep "error" | sort | uniq -c
```

will grep the lines which has errors and then provide the unique count of each of the following. 


---
10) Using SSH pipe we can do it, i had one file.text on server 1 (fedora VM)
and server 2 (GCP) and using this i transfered the file : 
```bash
ssh yash@192.168.0.133 "cat test/file.txt" |  ssh -i ~/.ssh/pro_fixionoff pro_fixionoff@profixion.in
"cat > temp/file.txt"
```
Output : 
```bash
Hello there i am in the virtual machine of yash, let's see the magic
one dream one soul
one price one goal
one golden glance of what should be
```

Hence without saving locally we have successuly transfered file from server A to server B 