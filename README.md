# <span style="color:blue">My Weekly Tasks Repository for Module: Programming and Scripting</span>
## *Author: Laura Lyons*
***
## **Introduction**
***
This repository is a collection of work, complete as part of the H.Dip programme, Higher Diploma in Science in Data Analytics, Module: Programming and Scripting.

Each week, a progam will need to be generated to complete a preassigned task.

## **Week 01** -helloworld.py
---

1. Create a GitHub account and repository for yourself (pands-mywork), and the weekly task (pands-weekly-tasks)
2. Commit and push a file to the weekly tasks repository called helloworld.py. This file should contain a python program that displays Hello World! when it is run.

**My notes:**
- Ensure care is taken when entering the output, ie ensure you include appropriate spaces and colons.

## **Week 02** - bank.py.
---
Write a program called bank.py.

The program should:
 - Prompt the user and read in two money amounts (in cent).
 - Add the two amounts.
 - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

**My notes:**
 - As the input is entered as a whole number, I divided by 100, to get the decimal point in the appropriate position. This is not the most appropriate method, i hope to come across a more suitable method as the course progresses.
 - I have since found out (Reference, Pof DA, Lectire 6.2, Exponential Notiation), that 123e-2= 1.23.
 - Research was needed to find out how to code in the 'Euro' sign. The coding for the euro symbol: \N{euro sign}, was retrieved from stackoverflow.com (https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python). 

## **Week 03** - accounts.py
---
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

Extra:
Modify the program to deal with account numbers of any length ( comment your assumptions)

**My notes:**
 - The **strip()** comand was used, to remove any uncessary white space.
 - The input was then'subdivided into two parts, the *hidden_account_part* and the *visisble_account_part*.
  - The length of the *hidden account part* will be determined by the using the **len()** code, minus 4, replaced the digits with x's.
  - The -4, will represent the *visible_account part*.
 - Splicing code is used to highlight the numbers that we want to be replaced by x's.
 - Negative splicing was used to replace the last 4 digits with x's, as technically, we cannot anticipate the number of digits the user might enter.
 - We used **isdigit()** command to ensure that the input was valid, and only contained integers. Reference: https://www.w3schools.com/python/ref_string_isdigit.asp 
 - An **if** and **else** conditional statement was used to determine which reponse to print in the output.
  - If the input is correct, print the account number, with all but the last 4 digits replaced by x's.
  - If the input is incorrect, ie contains letters or symbols, print, 'Invalid account number entered. Please enter a valid account number.'

## **Week 04** - collatz.py
---
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
- At each step calculate the next value by taking the current value and,
 - If it is even, divide it by two, 
 - But if it is odd, multiply it by three and add one.
- The program will end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository 

**My notes:**
- The **def** function was used to break the task into manageable chunks, and it will only run when called upon. Reference: O'Reilly (2015) A Whirlwind Tour of Python: Defining Functions (pg:42)
- As the program must end when the current value equals 1, we use the **while* loop, so that the function will continue to run until the end result is 1.
- To check if the number is odd or even, as these numbers will be 'treated differently', we use an **if** statement. 
 - '**if** (x % 2) == 0', if, when x is divided by 2, it equals 0, we know this is an even number.
  - As instructed, Proceed to divide the number by 2.
  - And append the list named 'sequence', to refect the calculation applied. Lecture 5: List and Tuples. Reference: O'Reilly (2015) A Whirlwind Tour of Python (pg:16)
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

## **Week 05** - weekday.py
---
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

 - I searchted the internet on how generate what the current day is. The datetime module provides classes for manipulating dates and times in Python. Reference: https://docs.python.org/3/library/datetime.html , https://www.w3schools.com/python/python_datetime.asp. 
 - The variable *current_day* was created to get the current day, using the datetime module.
 - The variable *day_of_week* was created to tell if the specific day of the week.  (0 = Monday, 6 = Sunday)
 - the tuple *name_of_day* was created to define the order of the weekdays, (0 = Monday, 6 = Sunday).
 - The variable *today* was created, to simplify the code

 - An *for* statement was then applied and a range defined to distinguish weekdays [0:5]. 
  - If the day was identified as a weekend, the print out would read ' Today is '*(name_of_day[day_of_week])*. Unfortunately this is a weekday, go back to work'.
 - All other variables within the range would be treated as the weekend using the *else* statement.
  - If the day was identified as the weekend, the print out would read as 'Today is '*(name_of_day[day_of_week])*'. Hurrah, go back to bed!'.

## **Week 06** - sqrt.py
---
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

**My notes:**
Research:
- Newtons method for square roots, is a technique for finding the square root of a number by iteratively improving an initial guess References: python - Finding the square root using Newton's method (errors!) - Stack Overflow ()
- The formula for Newtons method = square_root (original_number)= (((original_number/estimated_sqrt)+ estimated_sqrt)/2).

 - 2 seperate files were created.
   -The first *sqrt.py*, used the math module to compare the estimate value to see how close the approximations were. This was so i could get to grips with what was needed to get the basics working.
     - The second file, *sqrt_no_mathmodule.py*, did not use formulas inported from the math module. Instead, defintions were created of the formulas necessary.

## **Week 07** - .py
---
Write a program that reads in a text file and outputs the number of e's it contains. 
The program should take the filename from an argument on the command line. 

## **Week 08** - plottask.py
___
Write a program called plottask.py that displays:
- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range 0 to 10, 
,on the one set of axes.

A number of libraries were imported to help with this weeks task.
 1. matplotlib is used to create plots.
 2. Numpy was used to help generate random numbers.

To help get my heaad around this weeks tasks, i subdivided the task into creating 2 different plots.
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


