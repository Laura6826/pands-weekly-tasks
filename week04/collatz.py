# collatz.py
# The aim of this program is to ask the user to input any positive integer and to read out the successive values
# following the application of specific calculations
# If the integer is even, divide it by two
# if the integer is odd, multiple it by three and add one.
# Author: Laura Lyons



def collatz_sequence (x):
    sequence = [x] #Reference Copilot (AI) 
    while x!= 1:
        if (x % 2) ==0:
            x= x //2
        else:
            x = (x*3) +1
            sequence.append(x)
    return sequence
       

guess= int(input('Please enter a positive integer: '))
# We need into check that the value entered is a positive integer
while guess <= 0:
    guess = int(input('That is not a positive integer. Please enter a positive integer:'))
else:
    collatz_sequence_guess = collatz_sequence(guess)
    print ('The Collatz sequence is {}'. format (collatz_sequence_guess))
