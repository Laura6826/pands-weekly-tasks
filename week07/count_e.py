# Weekly Task 07. count_e.py
# The aim of this program is to write a program that reads in a text file and outputs the number of e's it contains.
# Author: Laura Lyons


def count_e(filename): # It is necessary to create a module to count the number of 'e's in predefinied file.
    try:                                        # We use the 'try' command so that we can 
        with open (filename, 'r') as f:         # The file is opened in the 'read' mode.
            content = f.read()                  # The f.read() command is used to access the file content.
            e_count = content.lower().count('e')        # The count() command was used to count the number of 'e's present in the text.
            # Reference https://www.w3schools.com/python/ref_list_count.asp.
            return e_count  
    except FileNotFoundError:
        return ('File not found.')


file_location = input ('Please enter the location of the text file to be analyised: ').strip()
# Here we request the user to enter the file that they wish to analyis.
# The strip command is used to remove any unecessary white space present in the input.

e_occurrences = count_e(file_location)
print(f"This file contains {e_occurrences} iterations of the letter 'e'.")
