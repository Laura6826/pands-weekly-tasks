# sqrt.py
# Weekly Task 6. Write a program that takes a positive floating-point number as input and 
# outputs an approximation of its square root.
# Author: Laura Lyons

# Newtons method for square roots, is a technique for finding the square root of a number by iteratively improving an initial guess.
# The formula for Newtons method = square_root (original_number)= (((original_number/estimated_sqrt)+ estimated_sqrt)/2)
# References: python - Finding the square root using Newton's method (errors!) - Stack Overflow ()

# The application of the Newton Method for square roots formula was extropolated from 
# https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python. 

# The math.isclose () method checks whether two values are close to each other, or not.
# To avoid using the math module, I defined is_close() and refered to this definition within the code.
# Reference: https://www.w3schools.com/python/ref_math_isclose.asp
def is_close(num1, num2, tolerance=0.001):  
    return abs(num1 - num2) < tolerance     

def newtons_method_sqrt(num, estimate): # We need to apply the 'Newtons method formula', to create a new_estimate.
    new_estimate = ((estimate +(num/ estimate))/ 2) 
    # We can now use a 'Built in Function', the 'if' statement to compare our estimates.

    if is_close(estimate, new_estimate):
        approx_sqrt = (new_estimate)
        return approx_sqrt
    else:
        return newtons_method_sqrt(num, new_estimate)

original_num= (int(input('Please enter the number you wish to retrieve the square root of: ')))

# We need to ensure that the input number is a positive integer only.
while original_num <=0:
    original_num= input('That is not a positive integer. Please enter a positive integer: ')
else:
    estimate_sqrt = (int(input('Please enter an educated guess as to the squart root of your original number: ')))

    answer = newtons_method_sqrt (original_num, estimate_sqrt)
    print(f'The approximate square root of {original_num} is {answer}')