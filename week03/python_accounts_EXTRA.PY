# python_accounts_EXTRA.py, weekly task number 3
# The aim of this program is to read in a bank account number and to output
# the account number, with x's replaceing all but the last four digits. 
# Author: Laura Lyons

# I decided to create a second program for the EXTRA part of this task, so as not to interfer with the original program.

account_number = input('Please enter your account number: ')

clean_account_number = account_number.strip()
#  the strip() comand was used, to remove any uncessary white space.

hidden_account_part= 'x' * (len(clean_account_number) - 4)
# "Elements from a list can be accessed with a negative number, starting with -1" Lecture 5, List Indexing

visible_account_part = clean_account_number[-4:]
output_account_number = (f'{hidden_account_part}{visible_account_part}')
# the splicing code is used to highlight the numbers that we want to be replaced by x's.
# I used negative splicing to replace the last 4 digits with x's.

if clean_account_number.isdigit():
    print(output_account_number)
else:
    print ('Invalid account number entered. Please enter a valid account number.')
    # we want to ensure that the number entered only contains exactly 10 numerical characters.
    # Reference: https://www.w3schools.com/python/ref_string_isdigit.asp 


