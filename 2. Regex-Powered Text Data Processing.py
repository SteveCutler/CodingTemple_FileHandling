# Objective:
# The purpose of this assignment is to harness the power of regular expressions (regex) in Python for 
# advanced text data processing. You will apply regex to extract, manipulate, and analyze data from 
# text files, combining it with efficient file handling techniques.

# Task 1: Email Extractor:

# Problem Statement:
# Write a Python script to extract all email addresses from a given text file (contacts.txt). 
# The file contains a mix of text and email addresses.

#     File Example:

# Contact List:

# John Doe - john.doe@example.com
# Jane Smith - jane.smith@gmail.com
# Jane Smith - jane.smith@gmail.com

# For inquiries, please contact info@example.com

#     Code Example:

import re
import os


def extract_emails(filename):
    
    with open(filename, "r") as file:
        contents = file.read()
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', contents)
        print(emails)
    #check for duplicates
        
    x = 0
    while x < len(emails)-1:
        if emails.count(emails[x]) > 1:
            print(f"removing {emails[x]}")
            emails.remove(emails[x])
            x +=1
        else:
            x +=1
    
    return emails

    
   # print(contents)
    

emails = extract_emails("contactList.txt")
print(f"the unique email addresses from the file are: {emails}")
## Read the file and use regex to find and return all email addresses

# Expected Outcome:
# The script should output a list of all unique email addresses found in the file. 
# Utilize regex to accurately identify email addresses amidst other text.