# Weekly Task 08. plottask.py
# The aim of this task is to write a program called plottask.py that displays: a histogram of a normal distribution,
# of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range 0 to 10, 
# on the one set of axes.
# Author: Laura Lyons


import matplotlib.pyplot as plt                         # matplotlib is used to create plots.
import numpy as np                                      # was used to help generate random numbers.

# Plot 1
normal_data= np.random.normal(loc=5, scale= 2, size= 1000) 
# where loc= mean/ average, scale = standard deviation, size= the number of values to be generated.
plt.hist (normal_data, label='Histogram of a normal distribution.\n(Mean= 5, St.dev.= 2)', color='blue', edgecolor='black')  

h_x= np.array(range(0,10))
ypoints = h_x ** 3                                      # ** will raise to the power of 3.
plt.plot(h_x, ypoints, color='red', label='h(x)=x3')    # This will no onger be required, as both plots are to be combined.
                 

plt.title('Weekly Task 08', color='blue')               # This will create a blue title.
plt.xlabel('Variance', color='blue')
plt.ylabel('Frequency', color='blue')
plt.legend()
plt.show()
plt.savefig('Plot_task_1axis.png')
