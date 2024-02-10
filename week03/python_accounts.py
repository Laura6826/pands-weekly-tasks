# python_accounts.py, weekly task number 3
# The aim of this program is to read in a 10 digit bank account number and to output
# the account number, with the first 6 digits replaced with 'x' only the last four digits visible.
# Author: Laura Lyons

account_number = input('Please enter a 10 digit account number: ')

clean_account_number = account_number.strip()
#  the strip() comand was used, to remove any uncessary white space.
hidden_account_number = 'x' * 6 + clean_account_number [6:]
# the splicing code is used to highlight the numbers that we want to be replaced by x's.

if len(clean_account_number) == 10 and clean_account_number.isdigit():
    print(hidden_account_number)
else:
    print ('Invalid account number entered. Please enter a valid 10 digit number.')
    # we want to ensure that the number entered only contains exactly 10 numerical characters only.
    # Reference: https://www.w3schools.com/python/ref_string_isnumeric.asp 



