# Weekly task 02. bank.py 
# The aim of this program is to prompt the user and read in two money amounts (in cents), 
# add the two amounts and print the answer.
# Author: Laura Lyons

amount1 = int(input('Enter amount 1 (in cents): '))  # Initally, i called this variable 'x' however, 
# after learning about global varialbes, i will re-name it amount1 (similar for ammount2)

# input reads in a string so we need to convert to an integer
# to allow us to perform mathematical operations.   

amount2 = int(input('Enter amount 2 (in cents): '))
answer= ((amount1+amount2)* (10**-2)) # To convert from cents to , i will avoid dividing by 100 and instead use exponential notiation.
print (f'The sum of these is: \N{euro sign}{answer}')

# I pulled the coding for the euro symbol: \N{euro sign}, from stackoverflow.com 
# Ref https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python