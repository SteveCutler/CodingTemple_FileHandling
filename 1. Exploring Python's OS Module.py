# Objective:
# The goal of this assignment is to deepen your understanding of the OS module in Python. 
# You will engage in tasks that involve file and directory operations, path manipulations, 
# and practical applications of these operations in real-world scenarios.

# Task 1: Directory Inspector:

# Problem Statement:
# Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

#     Code Example:

import os

def listDirectoryContents(path):
    contents = os.listdir(path)
    print(contents)

dir = input("What folder would you like to know the contents of? (use 'newDir' for demo purposes)\n")
listDirectoryContents(dir)



#     Expected Outcome:
#     The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.

# Task 2: File Size Reporter:

# Problem Statement:
# Write a Python program that reports the sizes of all files in a specific directory. 
# The program should ask the user for a directory path and then print each file's name 
#     and size within that directory.

#     Code Example:

import os

def listDirectoryContents(path):
    contents = os.listdir(path)
    print(f"the contents of {path} are: {contents}")
    for file in contents:
        fullPath = os.path.join(path, file)
        if os.path.isfile(fullPath):
            size = os.path.getsize(fullPath)
            print(f"file {file} has a size of {size} bytes")
        else:
            print(f"file {file} is not a file")


dir = input("What folder would you like to know the contents of? (use 'newDir' for demo purposes)\n")
listDirectoryContents(dir)

#     Expected Outcome:
#     Your program should display the name and size (in bytes) of each file in the given 
# directory. Ensure that the program only reports on files, not directories, and handles any errors gracefully.

# Task 3: File Extension Counter:

# Problem Statement:
# Develop a Python script that counts the number of files of each extension type in a directory. 
# For instance, in a directory with five '.txt' files and three '.py' files, 
# the script should report "TXT: 5" and "PY: 3".

#     Code Example:
import os
import re

def countExtensions(dir):
    x = 0
    fileType = ""
    fileTypes = []
    fileTally = {}
    for file in os.listdir(dir):
        match = re.search(r'\.([^.]+)$', file.lower())
        if match:
            fileType = match.group().strip(".").upper()
            #fileTypes.append(fileType)
            if fileType in fileTally:
                for file, num in fileTally.items():
                    if file == fileType:
                        
                        fileTally[file] = num + 1
            else:
                fileTally[fileType] = 1
                

    print(fileTally)

countExtensions("newDir")

#.lower()
#count number of specific file name in directory
#regex?

# Count and print the number of files of each extension type in the directory

#     Expected Outcome:
#     The script should accurately count and display the number of files for each extension 
# type in the specified directory. Handle different cases of file 
# extensions (e.g., '.TXT' and '.txt' should be considered the same).
