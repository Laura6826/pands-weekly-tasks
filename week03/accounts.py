# python_accounts.py, weekly task number 3
# The aim of this program is to read in a 10 digit bank account number and to output
# the account number, with the first 6 digits replaced with 'x' only the last four digits visible.
# Author: Laura Lyons

account_number = input('Please enter a 10 digit account number: ')
print(account_number)
'''
# the number is refered to as a string as the account number is not to be changed


def get_valid_number():
    while True:
        if account_number.isdigit() and len(account_number) == 10:
            return int(account_number)
        else:
            print ('Invalid account number entered. Please enter a valid 10 digit number.')
            

length_of_account_number = len(account_number)
if length_of_account_number != 10: 
    print ('Invalid account number entered. Please enter a valid 10 digit number.')
    

clean_account_number = account_number.strip()
# the strip() comand was used, to remove any uncessary white space.

if len(clean_account_number) == 10 and clean_account_number.isdigit():
    print(clean_account_number)
    
    print (clean_account_number.replace('[:6]','x'))

else:
    print ('Invalid account number entered. Please enter a valid 10 digit number.')
# we want to ensure that the number entered only contains exactly 10 numerical characters only.
    # Reference: https://www.w3schools.com/python/ref_string_isnumeric.asp 

hidden_account_number = clean_account_number (replace("[:6]", "x"))
'''