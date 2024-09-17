#*~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~*
# Course: ECE 2112: Advanced Computer Programming and Algorithms
# Title: EXPERIMENT 3 PYTHON DATA ANALYSIS (PANDAS)

# Name: Michelle Sophia A. Abamonga
# Section: 2-ECEB
#*~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~*

#PROBLEM 1

#Import the Pandas library in Python.
#Assign pandas the alias pd for easier reference.
import pandas as pd

#Load the corresponding .csv file into a data frame named cars.
#Ensure the .csv file is downloaded to your default user folder for accessibility.
cars = pd.read_csv('cars.csv')

#3Display the first five rows of the resulting cars
#To display the first five rows of a DataFrame, you can use the .head() function. 
#By default, this function will return the first 5 rows, but you can specify a different number inside the parentheses if needed.
#Eg. dataframe.head(6), first 6 rows will be displayed.
cars.head()

#Display the last five rows of the resulting cars
#Similarly to .head(), the .tail() function displays the last five rows by default. 
#You can also specify a different number of rows by changing the number inside the parentheses.
cars.tail()
