#*~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~*
# Course: ECE 2112: Advanced Computer Programming and Algorithms
# Title: EXPERIMENT 3 PYTHON DATA ANALYSIS (PANDAS)

# Name: Michelle Sophia A. Abamonga
# Section: 2-ECEB
#*~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**~*

#PROBLEM 2

#Import the Pandas library in Python.
#Assign pandas the alias pd for easier reference.
import pandas as pd

#Load the corresponding .csv file into a data frame named cars.
#Ensure the .csv file is downloaded to your default user folder for accessibility.
cars = pd.read_csv('cars.csv')

#Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
#Using the slicing method, you can select the odd-numbered columns with a step of 2. 
#The .head() function will then display the first five selected columns from the latter condition.
cars.iloc[:, 0::2].head()

#Display the row that contains the ‘Model’ of ‘Mazda RX4’.
#With Bolean Indexing, the dataframe is filtered and will return a new one that contains only the 
#rows from cars where the 'Model' column's value is 'Mazda RX4'.
(cars[cars['Model'] == 'Mazda RX4'])

#Determine the number of cylinders for the car model ‘Camaro Z28’
#Also with the use of Bolean Indexing, the dataframe is filtered and will return a series containing the 
#values from the 'cyl' column for all rows where the 'Model' was 'Camaro Z28'
(cars[cars['Model'] == 'Camaro Z28']['cyl'])

#Determine the number of cylinders and the gear type for the ff. car models: ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’
#Again, with Boolean Indexing, the DataFrame is filtered to include only the specified car models. The .isin() function checks if 
#the values in the 'Model' column match any of the values in the provided list. After filtering, the relevant information 
#(number of cylinders and gear type) for each model is selected from the DataFrame.
(cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])][['cyl', 'gear']])
