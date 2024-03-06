# sqrt.py
# Weekly Task 6. Write a program that takes a positive floating-point number as input and 
# outputs an approximation of its square root.
# Author: Laura Lyons

# Newtons method for square roots, is a technique for finding the square root of a number by iteratively improving an initial guess.
# References: python - Finding the square root using Newton's method (errors!) - Stack Overflow ()

# The formula for Newtons method = square_root (original_number)= (((original_number/estimated_sqrt)+ estimated_sqrt)/2)

import math as m # this will only be used as a check, to see how accurate our formula is.

# application of the Newton Method for square roots formula was extropolated from 
# https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python. 

def newtons_method_sqrt(num, estimate):
    # We need to apply the 'Newtons method formula', to create a new_estimate.
    new_estimate= ((num/estimate)+ estimate)/ 2
    # We can now use a 'Built in Function', the 'if' statement to compare our estimates.
    
    if new_estimate != m.sqrt(num):
        return newtons_method_sqrt(num, new_estimate)
    elif new_estimate == m.sqrt(num):
        approx_sqrt = (new_estimate)
        return approx_sqrt
        

# Check point values 'newtons_method_sqrt(20,4)'

original_num= int(input('Please enter the number you wish to retrieve the square root of: '))

# We ne6d to ensure that the input number is a positive integer only

while isinstance(original_num, str) or original_num < 0:
    print ('That is not a positive integer. Please enter a positive integer: "')
    original_num = (input('Please enter the number you wish to retrieve the square root of: '))
else:
    estimate_sqrt = (int(input('Please enter an educated guess as to the squart root of your original number: ')))

answer = newtons_method_sqrt (original_num, estimate_sqrt)
print(f'The approximate square root of {original_num} is {answer}')