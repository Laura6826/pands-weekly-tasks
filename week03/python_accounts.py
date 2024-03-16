# Weekly task 03. python_accounts.py.
# The aim of this program is to read in a 10 digit bank account number and to output
# the account number, with the first 6 digits replaced with 'x' only the last four digits visible.
# Author: Laura Lyons

account_number = input('Please enter a 10 digit account number: ').strip()
#  the strip() comand was used, to remove any uncessary white space.

hidden_account_number = 'x' * 6 + account_number [6:]
# the splicing code is used to highlight the numbers that we want to be replaced by x's.

while len(account_number) != 10 and not account_number.isdigit(): 
    # Print the final number if the entered number contains 10 intgers only
    # Reference: w3schools https://www.w3schools.com/python/ref_stringisdigit.asp 
    account_number= input('Invalid account number entered. Please enter a valid 10 digit number.')
    hidden_account_number = 'x' * 6 + account_number [6:]
else:
    print(hidden_account_number)
    
   



