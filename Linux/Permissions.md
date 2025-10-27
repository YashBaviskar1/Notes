
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


### Answers 

1) `-rw-r--r--` : Owner(u) can read write, Group can only read, Others can only read
2) chmod 
3) chmod u+x filename 


4) Symbolic has u,g,o and + and - to add remove the permissions r, w, x 
numeric link has values read - 4, write - 2, execute -1 and based on it 

5) chmod -R path/to/directory
6) umask -> basically controls whenever there is a new file or directory in system how much to "mask" -> by deault its 777 and 555 so umask "subtracts" usually 0022 to set the permission