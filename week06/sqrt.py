# sqrt.py
# Weekly Task 6. Write a program that takes a positive floating-point number as input and 
# outputs an approximation of its square root.
# Author: Laura Lyons

# Newtons method for square roots, is a technique for finding the square root of a number by iteratively improving an initial guess.
# References: python - Finding the square root using Newton's method (errors!) - Stack Overflow ()

# The formula for Newtons method = square_root (original_number)= (((original_number/estimated_sqrt)+ estimated_sqrt)/2)

import math # this will only be used as a check, to see how accurate our formula is.

# application of the Newton Method for square roots formula was extropolated from 
# https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python. 

def newtons_method_sqrt(num, estimate):             # We need to apply the 'Newtons method formula', to create a new_estimate.
    new_estimate= ((num/ estimate)+ estimate)/ 2    # We can now use a 'Built in Function', the 'if' statement to compare our estimates.
    if new_estimate != math.sqrt(num):
        return newtons_method_sqrt(num, new_estimate)
    elif new_estimate == math.sqrt(num):
        approx_sqrt = (new_estimate)
        return approx_sqrt       
# Check point values print (newtons_method_sqrt(20,4))

original_num= (input('Step 1: Please enter the number you wish to retrieve the square root of: '))

# how to check if input is an integer was researched. Reference: https://www.pythonpool.com/python-check-if-string-is-integer/
isInt = True 
try:
   int(original_num)        # first we try converting the varible into an integer
except ValueError:
   isInt = False
while isInt:
   print ('That is a positive integer, please proceed to step 2.')
   break                    # A break is added, to prevent the code from running indefinitely.
else:
   print("That is not a positive integer.")
   original_num= (input('Please enter the number you wish to retrieve the square root of: '))
'''
try:
    while original_num is not float:
        print("That is not a positive integer.")
        original_num= float(input('Please enter the number you wish to retrieve the square root of: '))
    else:
        estimate_sqrt = (int(input('Please enter an educated guess as to the squart root of your original number: ')))
except ValueError:
    print("Invalid input. Please enter a positive integer.")
'''
estimate_sqrt = (int(input('Step 2: Please enter an educated guess as to the squart root of your original number: ')))

answer = newtons_method_sqrt (original_num, estimate_sqrt)
print(f'The approximate square root of {original_num} is {answer}')

