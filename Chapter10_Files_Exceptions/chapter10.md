# FILES and EXCEPTIONS

## Simple File Reader 
```with open('sample_file.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

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
        print(line)
```

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

### Readlines Method 
The `readlines()` method takes each line from file and stores it in a list. The list is then stored in lines, which we can continue to work with after block ends. Since each item in the `lines` corresponds to each line in the file, output matches file contents exactly. 

### Working with a File's Contents 
You can do whatever you want with the data after you read a file into memory!

## Writing to a File 
Simplest way to save data is to write it to a file. </br>
When you write text to a file, output will still be available after you close terminal containing output. 

### Writing to an Empty File 
To write text to a file, you need to call `open()` with a *second argument*:* 
``` with open(filename, 'w') as file_object:
    file_object.write("I love Programming!")
```
Second argument, **'w'** tell Python you want to open file in **write mode**. </br>
This file has no terminal output, but if you open the file `programming.txt` you'll see the line. </br>
The `open()` function automatically creates file you're writing to f it doesn't already exist, but you can open a file with: </br>
```
`read mode ('r')`
`write mode ('w')`
`append mode ('a')` or 
`read and write mode ('+r')`
```

### Writing Multiple Lines 
The `write()` function doesn't add any newlines to text you write.</br>
If you want to write more than a line, you should include: `\n`

###Appending to a File 
To add content to a file, you can open file in **append mode**</br>
Any lines you write to file with be added at teh end of file. If the file doesn't exist, Python will create an empty file for you. 
``` with open(filename, 'a') as file object:
    file_object.write("I also love large datasets.\n")
    file_object.write("I love creating apps.\n"
```


# Exceptions 
Python uses special objects called, `exceptions` to manage errors that arise during execution.</br>
When Python doesn't know what to do next, it creates an **exception object**</br>
If your code handles the exception, program will continue running</br>
If code does not handle exception, program will halt and show a **traceback** which includes a report of the exception. </br>
Exceptions are handled with `try-except` blocks.</br>
**Try-Except Blocks** ask Python to do something. With these blocks, users will see a friendly error message that you write instead of a confusing *traceback* </br>
A Traceback might looks something like this:
```Traceback (most recent call last):
     File "division.py", line 1, in <module>
        print(5/0)
ZeroDivisionError: division by zero
```

### Using try-except Blocks 
Write a   `try-except` block when you think an error might occur.
```try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### Using Exceptions to Prevent Crashes 


### The else Block

### Handling FileNotFoundError Exception

##Analyzing Text

### Working with Multiple Files 

###Failing Silently... 

### Deciding Which Errors to Report 


# Storing Data 

## Saving and Reading User-Generated Data 

## Refactoring 