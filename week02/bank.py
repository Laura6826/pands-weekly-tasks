# bank.py Week 02 Task
# The aim of this program is to prompt the user and read in two money amounts (in cents), add the two ammounts and print the answer.
# Authoer: Laura Lyons

x = int(input('Enter ammount 1 (in cents): ')) 
y = int(input('Enter ammount 2 (in cents): '))
answer= ((x+y)/100) # By dividing by 10, i will convert from cents to euros
print (f'The sum of these is: \N{euro sign}{answer}')

# I pulled the coding for the euro symbol: \N{euro sign}, from stackoverflow.com 
# Ref https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python.