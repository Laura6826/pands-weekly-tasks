# <span style="color:blue">My Weekly Tasks Repository for Module: Programming and Scripting</span>
## *Author: Laura Lyons*
***
## **Introduction**
***
This repository is a collection of work, complete as part of the H.Dip programme, Higher Diploma in Science in Data Analytics, Module: Programming and Scripting.

Each week, a progam will need to be generated to complete a preassigned task.

## **Week 01**
###helloworld.py***
---

1. Create a GitHub account and repository for yourself (pands-mywork), and the weekly task (pands-weekly-tasks)
2. Commit and push a file to the weekly tasks repository called helloworld.py. This file should contain a python program that displays Hello World! when it is run.

**My notes:**
- Ensure care is taken when entering the output, ie ensure you include appropriate spaces and colons.

## **Week 02**
---
Write a program called bank.py.

The program should:

 - Prompt the user and read in two money amounts (in cent).
 - Add the two amounts.
 - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

**My notes:**
 - As the input is entered as a whole number, I divided by 100, to get the decimal point in the appropriate position. This is not the most appropriate method, i hope to come across a more suitable method as the course progresses.
 - Research was needed to find out how to code in the 'Euro' sign. The coding for the euro symbol: \N{euro sign}, was retrieved from stackoverflow.com (https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python). 

## **Week 03**
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
 - We used **isdigit()** command to ensure that the input was valid, and only contained integers.
 - An **if** and **else** conditional statement was used to determine which reponse to print in the output.
  - If the input is correct, print the account number, with all but the last 4 digits replaced by x's.
  - If the input is incorrect, ie contains letters or symbols, print, 'Invalid account number entered. Please enter a valid account number.'

## **Week 04**
---

## **Week 05**
---



