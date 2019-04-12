# FILES and EXCEPTIONS

## Simple File Reader 
```with open('sample_file.txt') as file_object:
    contents = file_object.read()
    print(contents)```

### Open Function 
The `open()` function allows the program to access a file.</br>
This function needs one argument: the name of the file. </br>
Python looks for file in directory where program that is currently being executed is stored. </br>
The `open()` function returns an **object** representing the file, and Python stores this object in `file_object` </br>

### Close Function, `with` keyword 
The `close()` function closes the file, but it's better to use `with` keyword to avoid accidental error. <br>
The `with` keyword will automatically close the file once access is no longer needed. 

### Read Method 
The `read()` method reads the entire contents of the file and stores it as one long string in **contents**. When we print the value of contents, we get the whole text file back. 

### Stripping White Space 
The output will have a blank line because `read()` returns an empty string when when it reaches the end of the file.</br>
To remove this line, consider using the `rstrip()` method. 

## File Paths 
Python typically looks in the directory where the file that is currently being executed is stored.</br>
Sometimes the file you want isn't in the same directory as the program file... </br>
To get Python to open files from anotehr directory, you need to provide a **file path**. </br>
`with open('text_files/filename.txt') as file_object` tells Python to look for the desired .txt file in teh folder *text_files*. </br>
You can also tell Python exactly where the file on your computer is stored  regardless of its location (absolte path)</br>
**Absolute paths** are usually longer than relative paths and might look something like this: `file_path = '/home/ehmatthes/other_files/text_files/filename.txt' with open(file_path) as file_object:`

## Reading Line by Line
Its common to examine files line by line. You might want to look for certain information or modify the text in some way. </br>
Use a **for loop** on a *file object* to do so</br>
``` filename = 'pi_digits.txt' 

with open(filename) as file_object:
    for line in file_object:
        print(line) ```

Its convention to store the name of the file in a varaible called `filename` b/c it doesn't represent an actual file, just a string that tells Python where to find the file. 

## Making a list of Lines from a File 
When using `with` keyword, the *file object* returned by `open()` is *only available inside the with block.* </br>
To retain access to file's content outside with block, you can *store the file's lines in a list insid teh block.*</br>
You can process parts of the file immediately and postpone some processing for later. </br> 
``` filename = 'pi_digits.txt' 

with open(filename) as file_object:
    **lines = file_object.readlines()**

for line in file_object:
        print(line) 
```