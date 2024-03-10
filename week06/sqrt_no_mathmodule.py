# sqrt_no_math_module.py
# Weekly Task 6. Write a program that takes a positive floating-point number and outputs an approximation of its square root.
# Author: Laura Lyons

# Newtons method for square roots, is a technique for finding the square root of a number by iteratively improving an initial guess.
# The formula for Newtons method = square_root (original_number)= (((original_number/estimated_sqrt)+ estimated_sqrt)/2)
# References: python - Finding the square root using Newton's method (errors!) - Stack Overflow ()/ README.md

def is_close(num1, num2, tolerance=0.001):  
   return abs(num1 - num2) < tolerance 

def newtons_method_sqrt(num, estimate):             # We need to apply the 'Newtons method formula', to create a new_estimate.
    new_estimate = ((estimate +(num/ estimate))/ 2) # We can now use a 'Built in Function', the 'if' statement to compare our estimates.
    if is_close(estimate, new_estimate) is False:
        return newtons_method_sqrt(num, new_estimate)
    elif is_close(estimate, new_estimate) is True:
        return new_estimate

original_num = (input('Please enter the number you wish to retrieve the square root of: '))

while type (original_num) is str:
# isinstance(original_num, str):                
    # I tried to also ensure that the integer is positive, by using the code 'while original_num <0', however it through out an error.
    print ('That is not a positive integer. Please enter a positive integer: ')
    original_num = (input('Please enter the number you wish to retrieve the square root of: '))
if type (original_num) is float:
    estimate_sqrt = (int(input('Please enter an educated guess as to the squart root of your original number: ')))
    
answer = newtons_method_sqrt (original_num, estimate_sqrt)
print(f'The approximate square root of {original_num} is {answer}')

