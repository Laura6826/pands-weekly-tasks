# Repository of weekly tasks for the module: Programming and Scripting, 2024 as part of the Higher Diploma in Science, Data Analytics.

## *Author: Laura Lyons*

***

## **Table of contents**

[Introduction](#introduction)\
[How to get started](#how-to-get-started)

  1. [Week 01- Setting up the Environment](#week-01--helloworldpy)
  2. [Week 02- Statements](#week-02---bankpy)
  3. [Week 03- Variables](#week-03---accountspy)
  4. [Week 04- Controlling the flow](#week-04---collatzpy)
  5. [Week 05- Date](#week-05---weekdaypy)
  6. [Week 06- Functions](#week-06---sqrtpy)
  7. [Week 07- Files](#week-07---count_epy)
  8. [Week 08- Looking ahead](#week-08---plottaskpy)

***

## **Introduction**

This repository is a collection of work, complete as part of the Higher Diploma in Science in Data Analytics, Module: Programming and Scripting.

Each week, following a series of lectures, a task was assigned, to demonstrate both learning and additional reading/research on the topics discussed in the lectures.

This repository is collection of my weekly tasks, including some additional guidance and instruction in how to run each task/program.

***

## **How to get started**

In order to run the files, you will need to ensure that you have access to the correct softwear.
I would recommend downloading the following applications (ensuring sufficent space on your hard drive prior to installation):

1. Anaconda (if Anaconda is too large, miniconda would also suffice).\
Wikipedia defines Anaconda as;
"*a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment*".
2. Visual Studio Code (this is a code editor made by Microsoft).

***

## **Week 01** -helloworld.py

**Asignment Instructions:**

1. Create a GitHub account and repository for:\
  1st. Your own work, called 'pands-mywork'. This was not be assessed as part of the module.\
  2nd. Weekly tasks [pands-weekly-tasks](https://github.com/Laura6826/pands-weekly-tasks). The second repository was assessed and represent 50% of the overall grade for the module.
2. Commit and push a file to the weekly tasks repository called helloworld.py. This file should contain a python program that displays Hello World! when it is run.

**My notes:**

- When installing Anaconda, make sure you check the PATH variable ; "*Add Anaconda3 to my PATH environment variable*'
- When creating a Github account, ensure a personal email address that you will have continual access too is used. A college email address will be deactivated after graduation, if used when setting up a Git hub account, there maybe difficulties in accessing the Github account further down the line.
- Once the account was set up on Github, 2 folders were created.
    1. **pands_weekly_tasks**. Each week, a new folder was created as a subfolder within *pands_weekly_tasks*, to represent each weekly task and named accordingly. The URL for this folder was submitted on **Moodle** to allow for the correction of the tasks (totaling 50% of this modules mark).
    2. **pands_my_work**. This folder was where all my personal work associated with each weeks leactures was stored.

- Ensure care is taken when entering the output, *i.e.* you include appropriate spaces and colons.
- The language identifier, *ruby* was used to enable [syntax highlighting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks#syntax-highlighting) in the code blocks below.

**When run:**

- The program will print: Hello World!

**Associated Code:**

```ruby
print("Hello World!")
```

***

## **Week 02** - bank.py

**Asignment Instructions:**

Write a program called bank.py.

The program should:

- Prompt the user and read in two money amounts (in cent).
- Add the two amounts.
- Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

**My notes:**

- As the input is entered as a whole number, I divided by 100, to get the decimal point in the appropriate position. This is not the most appropriate method, i hope to come across a more suitable method as the course progresses.
- I have since found out (Reference, Pof DA, Lecture 6.2, Exponential Notiation), that 123e-2= 1.23.
- Research was needed to find out how to code in the 'Euro' sign. The coding for the euro symbol: \N{euro sign}, was retrieved from stackoverflow.com (<https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python>).

**When run:**

- The user will be prompted: .

  - Enter ammount 1 (in cents):  .
  - Enter ammount 2 (in cents):  .

- The program will print:

  - The sum of these is: €  .

**Associated Code:**

```ruby
ammount1 = int(input('Enter ammount 1 (in cents): '))     
ammount2 = int(input('Enter ammount 2 (in cents): '))
answer= ((ammount1+ammount2)* (10**-2)) 
print (f'The sum of these is: \N{euro sign}{answer}')
```

***

## **Week 03** - accounts.py

**Asignment Instructions:**\
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

Extra:
Modify the program to deal with account numbers of any length (comment your assumptions)

**My notes:**

- The **strip()** comand was used, to remove any uncessary white space.
- The input was then'subdivided into two parts, the *hidden_account_part* and the *visisble_account_part*.
  - The length of the *hidden account part* will be determined by the using the **len()** code, minus 4, replaced the digits with x's.
  - The -4, will represent the *visible_account part*.
- Splicing code is used to highlight the numbers that we want to be replaced by x's.
- Negative splicing was used to replace the last 4 digits with x's, as technically, we cannot anticipate the number of digits the user might enter.
- We used **isdigit()** command to ensure that the input was valid, and only contained integers.\ Reference: <https://www.w3schools.com/python/ref_string_isdigit.asp>
- An **if** and **else** conditional statement was used to determine which reponse to print in the output.
  - If the input is correct, print the account number, with all but the last 4 digits replaced by x's.
  - If the input is incorrect, ie contains letters or symbols, print, *'Invalid account number entered. Please enter a valid account number.'*

**When run:**

- The user will be prompted: .
  - Please enter a 10 digit account number: 123455678

- The program will print:
  - xxxxxx678
  
**Associated Code:**

1. The first code  deals with a bank account number of a specified length (i.e. 10 digits long)

```ruby
account_number = input('Please enter a 10 digit account number: ').strip()
hidden_account_number = 'x' * 6 + account_number [6:]

while len(account_number) != 10 and not account_number.isdigit():  
    account_number= input('Invalid account number entered. Please enter a valid 10 digit number.')
    hidden_account_number = 'x' * 6 + account_number [6:]
else:
    print(hidden_account_number)
```

2. The second code block deals with a bank account number of unspecified length.

```ruby
account_number = input('Please enter your account number: ').strip()
hidden_account_part= 'x' * (len(account_number) - 4)
visible_account_part = account_number[-4:]
output_account_number = (f'{hidden_account_part}{visible_account_part}')

while not account_number.isdigit():
   account_number = input ('Invalid account number entered. Please enter a valid account number.')
   hidden_account_part= 'x' * (len(account_number) - 4)
   visible_account_part = account_number[-4:]
   output_account_number = (f'{hidden_account_part}{visible_account_part}') 
else:
    print (output_account_number)
```

***

## **Week 04** - collatz.py

**Asignment Instructions:**\
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

- At each step calculate the next value by taking the current value and,
- If it is even, divide it by two,
- But if it is odd, multiply it by three and add one.
- The program will end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository

**My notes:**

- The **def** function was used to break the task into manageable chunks, and it will only run when called upon. Reference: [O'Reilly (2015) A Whirlwind Tour of Python: Defining Functions (pg:42)](https://www.oreilly.com/content/a-whirlwind-tour-of-python/).
- As the program must end when the current value equals 1, we use the **while* loop, so that the function will continue to run until the end result is 1.
- To check if the number is odd or even, as these numbers will be 'treated differently', we use an **if** statement.
- '**if** (x % 2) == 0', if, when x is divided by 2, it equals 0, we know this is an even number.
- As instructed, Proceed to divide the number by 2.
- And append the list named 'sequence', to refect the calculation applied. Reference: Lecture 5: List and Tuples and [O'Reilly (2015) A Whirlwind Tour of Python (pg:16)](https://www.oreilly.com/content/a-whirlwind-tour-of-python/).
- **else** assume the number is an odd number, as when 'x' is divided by 2 and the answer is not 0, the number entered must be an odd number.
- Proceed to multiply the entered number by 3 and then add 1.
- Append 'sequence', to refect the calculation applied.
- Once all calculations are complete, and the current value is 1.
- Return the sequence.

Once the definition of the collatz_sequence was complete, we could proceed to use/ call this definition to ammend potential input.

- It was requested for the user to 'Please enter a positive integer: '
- To ensure that the input was a positive integer and not 0, a **while loop** was used.
  - If the input did not meet the requirements, ie, a positive integer, the program would request another guess using the following prompt, 'That is not a positive integer. Please enter a positive integer:'
  - An **else** conditional statement was then used, to call forward the function created and apply it to the input data.
Finally, the output was printed, to include each digit generated through out the process, hence generating the collatz sequence for the originally entered digit.

**When run:**

- The user will be prompted: .
  - Please enter a positive integer: 6

- The program will print:
  - xThe Collatz sequence is [6, 3, 10, 5, 16, 8, 4, 2, 1]
  
**Associated Code:**

```ruby
def collatz_sequence (num):      
    sequence = [num]              
    while num!= 1:                
        if (num % 2) ==0:         
            num= num /2 
            sequence.append(num)
        else:
            num = (num*3) +1 
            sequence.append(num)  
    return sequence
       
guess= int(input('Please enter a positive integer: ')) 
while guess <= 0:
    guess = int(input('That is not a positive integer. Please enter a positive integer:'))
else:
    collatz_sequence_guess = collatz_sequence(guess)
    print ('The Collatz sequence is {}'. format (collatz_sequence_guess))
```

***

## **Week 05** - weekday.py

**Asignment Instructions:**\
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

**My notes:**

- I had to research, on the internet, how generate what the current day is. The datetime module provides classes for manipulating dates and times in Python.\Reference: <https://docs.python.org/3/library/datetime.html> , <https://www.w3schools.com/python/python_datetime.asp>.
- The variable *current_day* was created to get the current day, using the datetime module.
- The variable *day_of_week* was created to tell if the specific day of the week.  (0 = Monday, 6 = Sunday)
- the tuple *name_of_day* was created to define the order of the weekdays, (0 = Monday, 6 = Sunday).
- The variable *today* was created, to simplify the code.
- An **for** statement was then applied and a range defined to distinguish weekdays [0:5].
- If the day was identified as a weekend, the print out would read:
  - *'Today is '*(name_of_day[day_of_week])*. Unfortunately this is a weekday, go back to work'*
- All other variables within the range would be treated as the weekend using the *else* statement.
- If the day was identified as the weekend, the print out would read as;
  - *'Today is '*(name_of_day[day_of_week])*'. Hurrah, go back to bed!'*

**When run:**

- The program will print:
  - Today is Saturday.
    Its the weekend! Hurrah, go back to bed!

**Associated Code:**

```ruby
from datetime import date 
current_day = date.today()         
day_of_week = current_day.weekday() 
name_of_day= ('Monday',             
              'Tuesday', 
              'Wednesday', 
              'Thursday', 
              'Friday', 
              'Saturday', 
              'Sunday')         

if day_of_week <5:  
    print(f"Today is {(name_of_day[day_of_week])}.\nUnfortunately this is a weekday, go back to work!.")
else:
    print(f"Today is {(name_of_day[day_of_week])}.\nIts the weekend! Hurrah, go back to bed!")
```

***

## **Week 06** - sqrt.py

**Asignment Instructions:**\
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called ***sqrt*** that does this.

**My notes:**\
Research:

- Newtons method for square roots, is a technique for finding the square root of a number by iteratively improving an initial guess References: python - Finding the square root using Newton's method (errors!) - Stack Overflow ()
The formula for Newtons method:

```ruby
square_root (original_number)= (((original_number/estimated_sqrt)+ estimated_sqrt)/2).
```

- 2 seperate files were created.
   1. The first *sqrt.py*, used the math module to compare the estimate value to see how close the approximations were. This was so i could get to grips with what was needed to get the basics working.
   1. The second file, *sqrt_no_mathmodule.py*, did not use formulas inported from the math module. Instead, defintions were created of the formulas necessary.

1. For *'sqrt.py'*:

- The Math Module was downloaded to use as an initial reference.
- The application of the Newton Method for square roots formula was extropolated from <https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python>.
- The **def** function was used to break the task into manageable chunks, and it will only run when called upon. Reference: [O'Reilly (2015) A Whirlwind Tour of Python: Defining Functions (pg:42)](https://www.oreilly.com/content/a-whirlwind-tour-of-python/).
- The definiation for *'newtons_method_sqrt'* was created, whereby the original number and an educated guess as to the squart root of the original number.
  - An **if** and **else** conditional statement was used to determine which reponse to print in the output.
  - If the input is correct, ie the calculated '*new_estimate'* was equal to the square root of the original estimate ( as calculated by the math module), then the number would be returned as the *'approx_sqrt'*.
  - If the input is incorrect, ie the calculated '*new_estimate'* was not equal to the square root of the original estimate (as calculated by the math module), then the number would loop back into the def until it is equal to square root of the original estimate and returned as the *'approx_sqrt'*.

- Once *'newtons_method_sqrt'* was defined, the user was promted to,*'Step 1: Please enter the number you wish to retrieve the square root of: '*, which would be feed into the program as *'original_number'*.

- The **'try, except'** statement was used to deal with potential exceptions, in this case, we need the entered integer to be positive. How to check if input is an integer was researched. Reference: <https://www.pythonpool.com/python-check-if-string-is-integer>.
  - First we try converting the varible into an integer
  - A break is added, to prevent the code from running indefinitely.
  - If the integer added was not a positive integer, the user was prompted with, *'Step 1: Please enter the number you wish to retrieve the square root of: '*
  - The user was then prompted again, *'Step 2: Please enter an educated guess as to the square root of your original number: '*
- Both number prompted by the user were feed into the definition *'newtons_method_sqrt'*.
- With the program returning. *'The approximate square root of {original_num} is {answer}'*

2. For *sqrt_no_mathmodule.py*.

- Similar to the above method:
  - The application of the Newton Method for square roots formula was extropolated from <https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python>.
  - The **def** function was used to break the task into manageable chunks, and it will only run when called upon. Reference: [O'Reilly (2015) A Whirlwind Tour of Python: Defining Functions (pg:42)](https://www.oreilly.com/content/a-whirlwind-tour-of-python/).
  - The definition for *'newtons_method_sqrt'* was created, whereby the original number and an educated guess as to the squart root of the original number.
- However on this occassion, the *math* module was not used. Instead a def was created where by the **is_close()** command is used, with a tolerance of 0.001. When the second number is within 0.001 of the first number, the function will return the absolute of the original number. This was pluged into the definition for *'newtons_method_sqrt'*

- Once *'newtons_method_sqrt'* was defined, the user was promted to,*'Step 1: Please enter the number you wish to retrieve the square root of: '*, which would be feed into the program as *'original_number'*.

- The **'try, except'** statement was used to deal with potential exceptions, in this case, we need the entered integer to be positive. How to check if input is an integer was researched. Reference: <https://www.pythonpool.com/python-check-if-string-is-integer>.
  - If the *'new_estimate'* is notnwithin 0.001 of the original number, ie is 'False', the *'new_estimate'* is looped back into the calculation until it is within 0.001 of the original number.
  - First we try converting the varible into an integer
  - A break is added, to prevent the code from running indefinitely.
  - If the integer added was not a positive integer, the user was prompted with, *'Step 1: Please enter the number you wish to retrieve the square root of: '*
  - The user was then prompted again, *'Step 2: Please enter an educated guess as to the square root of your original number: '*
- Both number prompted by the user were feed into the definition *'newtons_method_sqrt'*.
- With the program returning. *'The approximate square root of {original_num} is {answer}'*

**When run:**

- The user will be prompted: .
  - Step 1: Please enter the number you wish to retrieve the square root of: 25
- The programme will return:
  - That is a positive integer, please proceed to step 2.
- The user will be prompted: .
  - Step 2: Please enter an educated guess as to the squart root of your original number:6
- The programme will return:
  -The approximate square root of 36 is 6

**Associated Code:**

1. The first file uses the math module:

```ruby
import math

def newtons_method_sqrt(num, estimate):             
    new_estimate= ((num/ estimate)+ estimate)/ 2    
    if new_estimate != math.sqrt(num):
        return newtons_method_sqrt(num, new_estimate)
    elif new_estimate == math.sqrt(num):
        approx_sqrt = (new_estimate)
        return approx_sqrt       

original_num= int(input('Step 1: Please enter the number you wish to retrieve the square root of: '))

isInt = True 
try:
   int(original_num)       
except ValueError:
   isInt = False
while isInt:
   print ('That is a positive integer, please proceed to step 2.')
   break                    
else:
   print("That is not a positive integer.")
   original_num= int(input('Please enter the number you wish to retrieve the square root of: '))

estimate_sqrt = (int(input('Step 2: Please enter an educated guess as to the squart root of your original number: ')))
answer = newtons_method_sqrt (original_num, estimate_sqrt)
print(f'The approximate square root of {original_num} is {answer}')
```

2. The second file does not use the math module.

```ruby
def is_close(num1, num2, tolerance=0.001):  
   return abs(num1 - num2) < tolerance 

def newtons_method_sqrt(num, estimate):             
    new_estimate = ((estimate +(num/ estimate))/ 2) 
    if is_close(estimate, new_estimate) is False:
        return newtons_method_sqrt(num, new_estimate)
    elif is_close(estimate, new_estimate) is True:
        return new_estimate

original_num = (input('Please enter the number you wish to retrieve the square root of: '))

isInt = True 
try:
   int(original_num)       
except ValueError:
   isInt = False
while isInt:
   print ('That is a positive integer, please proceed to step 2.')
   break                    
else:
   print("That is not a positive integer.")
   original_num= int(input('Please enter the number you wish to retrieve the square root of: '))

estimate_sqrt = (int(input('Step 2: Please enter an educated guess as to the squart root of your original number: ')))
answer = newtons_method_sqrt (original_num, estimate_sqrt)
print(f'The approximate square root of {original_num} is {answer}')
```

***

## **Week 07** - count_e.py

**Asignment Instructions:**\
Write a program that reads in a text file and outputs the number of e's it contains.
The program should take the filename from an argument on the command line

**My notes:**

- The **def** function was used to break the task into manageable chunks, and it will only run when called upon. Reference: [O'Reilly (2015) A Whirlwind Tour of Python: Defining Functions (pg:42)](https://www.oreilly.com/content/a-whirlwind-tour-of-python/). It is necessary to create a module to count the number of 'e's in predefinied file.
- The **'try, except'** statement was used to deal with potential exceptions.
- The file was opened with *'r'* , as this is read mode.We do not anticipate having to add anything text to the file, we just want to read in the text contained within the tile.
- The **'f.read()'** command was used, to access the file content.
- Research was needed to figure out how to count the number of 'e's present in the text. The source use for *'count()'* was <https://www.w3schools.com/python/ref_list_count.asp>.
- **'.lower()'** was used to transform the text to be analyised into all lower case Reference: <https://www.w3schools.com/python/ref_list_count.asp>.
- The exception *'FileNotFoundError'* was applied, should the user input an incorrect location for the text to be analyised.
- The user was them prompted to enter the location of the file to be analyised: ''Please enter the location of the text file to be analyised: ', with any additional white space removed with the command, *'strip()'*.
- The file submitted was run through the code, with the user recieving the following output: *'This file contains {e_occurrences} iterations of the letter 'e'.'*

**When run:**

- The user will be prompted: .
  -Please enter the location of the text file to be analyised: .
 Once the user has entered a valid location for the file to be analyised, the program will print:
  - This file contains 1260 iterations of the letter 'e'.

**Associated Code:**

```ruby
    try:                                        
        with open (filename, 'r') as f:         
            content = f.read()                 
            e_count = content.lower().count('e')        
            return e_count  
    except FileNotFoundError:
        return ('File not found.')

file_location = input ('Please enter the location of the text file to be analyised: ').strip()
e_occurrences = count_e(file_location)
print(f"This file contains {e_occurrences} iterations of the letter 'e'.")
```

***

## **Week 08** - plottask.py

**Asignment Instructions:**\
Write a program called plottask.py that displays:

- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
- and a plot of the function  h(x)=x3 in the range 0 to 10,
,on the one set of axes.

**My notes:**\
A number of libraries were imported to help with this weeks task.

 1. matplotlib is used to create plots.
 2. Numpy was used to help generate random numbers.

To help get my heaad around this weeks tasks, I subdivided the task into creating 2 different plots.

### Plot 1

A random number generator was used to help generate the numbers needed for this task:

- *normal_data= np.random.normal (loc=5, scale= 2, size= 1000)*
- where loc= mean/ average, scale = standard deviation, size= the number of values to be generated.
The plot was then created using the *plt.hist* function. The color of the legend was defined and a black edge was applied to each of the bins to help differentiate each category.

Once the first plot was generated, and i was happy with the appearence of the plot,i started to research how to create plot 2.

### Plot 2

The second plot involved creating a plot for the function  *h(x)=x^3*

As the task stated that the integers should be within the range (0-10), we using *numpy* to help define the data set.

- The data to be displayed on the x-axis was defined using the function, *h_x= np.array(range(0,10))*.
- The data to be displayed on the x-axis was defined using the function, *ypoints = h_x**3*.
The plot was then created using the *plt.plot* function, as we wanted this data to be displayed as a line.

A title, x  and y axis labels and a ledged added to the plot.

The plot was then saved using the *plt.savefig()* function.

On this plot, the y-axis was *log* transformed, to make the plot easier to read and more visually appealing (Plot_task_1axis.log).

**Associated Code:**

1. The first  only utilizes the primary axes.

```ruby
import matplotlib.pyplot as plt                       
import numpy as np                                    

normal_data= np.random.normal(loc=5, scale= 2, size= 1000) 
plt.hist (normal_data, label='Histogram of a normal distribution.\n(Mean= 5, St.dev.= 2)', color='blue', edgecolor='black')  

h_x= np.array(range(0,10))
ypoints = h_x ** 3                                     
plt.plot(h_x, ypoints, color='red', label='h(x)=x3') 
plt.title('Weekly Task 08', color='blue')              
plt.xlabel('Variance', color='blue')
plt.ylabel('Frequency', color='blue')
plt.legend()
plt.show()
plt.savefig('Plot_task_1axis.png')
```

1. The second graph, Plot_task_2axis.png, utilizes both primary and secondary axiss. The histogram is plotted using the x and y axis, and the linear function is plotted on the z axis. This allows us to manipulate the exes to achieve the best visual output, without having to transform the data.

```ruby
import matplotlib.pyplot as plt            
import numpy as np                          

normal_data= np.random.normal(loc=5, scale= 2, size= 1000) 
h_x= np.array(range(0,10))
ypoints = h_x ** 3                        

fig, ax1 = plt.subplots()                   
ax1.hist(normal_data, label='Histogram of a normal distribution.\n(Mean= 5, St.dev.= 2)', color='blue', edgecolor='black' )                       
ax1.set_xlabel('Values', color='blue')      
ax1.set_ylabel('Frequency', color='blue')   
ax2 = ax1.twinx()                           
ax2.plot(h_x, ypoints, color='red', label='h(x)=x3') 
ax2.set_ylabel('h(x)^3', color='blue')

plt.title('Weekly Task 08', color='blue')                 
plt.legend()
plt.show()
plt.savefig('Plot_task_2axis.png')
```
