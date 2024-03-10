# Weekly Task 04. collatz.py. 
# The aim of this program is to ask the user to input any positive integer and to read out the successive values
# following the application of specific calculations
# If the integer is even, divide it by two
# if the integer is odd, multiple it by three and add one.

# Author: Laura Lyons


def collatz_sequence (num):       # Reference: O'Reilly (2015) A Whirlwind Tour of Python: Defining Functions (pg:42)
    sequence = [num]              # Reference: O'Reilly (2015) A Whirlwind Tour of Python (pg:8)
    while num!= 1:                # while 'x' is not equal to 1,
        if (num % 2) ==0:         # If 'x' is divided by 2 and the answer is 0, the number entered is an even number. 
                                  # Proceed to divide the number by 2.
            num= num //2
            sequence.append(num)  # Appendthe list named 'sequence', to refect the calculation applied. Lecture 5: List and Tuples.
                                  # Reference: O'Reilly (2015) A Whirlwind Tour of Python (pg:16)
        else:
            num = (num*3) +1      # If, when 'x' is divided by 2 and the answer is not 0, the number entered must be an odd number.
                                  # Proceed to multiply the entered number by 3 and then add 1. 
            sequence.append(num)  # Append 'sequence', to refect the calculation applied.
    return sequence
       

guess= int(input('Please enter a positive integer: ')) 
# We need into check that the value entered is a positive integer

while guess <= 0:
    guess = int(input('That is not a positive integer. Please enter a positive integer:'))
else:
    collatz_sequence_guess = collatz_sequence(guess)
    print ('The Collatz sequence is {}'. format (collatz_sequence_guess))
