# PA3 - PYTHON DATA ANALYSIS (PANDAS)
This repository contains Python scripts designed to address a range of programming problems in ECE2112. The focus is on DataFrame creation and the utilization of the Pandas library. Presented below are the key concepts and functionalities used in the given Python exercises.

***
### Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

***
### Introduction to Pandas:
Python Data Analysis (Pandas), is a core Python library that provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
<br> <br>
It is best used for: <br>
* Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet.
* Ordered and unordered (not necessarily fixed-frequency) time series data.
* Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels.
* Any other form of observational/statistical data sets.

***
## Problem 1
### Instructions:
Using knowledge obtained from the experiment and demonstrations: <br>
a. Load the corresponding .csv file into a data frame named cars using pandas <br>
b. Display the first five and last five rows of the resulting cars. <br>

##
### Key Concepts and Functionalities:
#### 1. Loading Data into a DataFrame
* **pd.read_csv('dataname.csv')** - Loads a CSV file into a pandas DataFrame. Ensure that the file is  downloaded to your default user folder in order for it to be accessible.

#### 2. Basic DataFrame Operations
* **df.head()** - Allows user to quickly view the first few rows of a DataFrame. By default, first 5 rows are displayed.
> Sample Syntax and Output: <br>
> ![Screen Shot 2024-09-17 at 11 05 02 PM](https://github.com/user-attachments/assets/0519e27e-2d53-42be-b494-19945c8f963e)
 
* **df.tail()** - Allows user to quickly view the last few rows of a DataFrame. By default, last 5 rows are displayed.
> Sample Syntax and Output: <br>
> ![Screen Shot 2024-09-17 at 11 03 36 PM](https://github.com/user-attachments/assets/40648d7f-b732-4e02-a431-10b1cd15369d)

***
## Problem 2
### Instructions:
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations. <br>
a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars. <br>
b. Display the row that contains the ‘Model’ of ‘Mazda RX4’. <br>
c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? <br>
d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford <br> Pantera L’ and ‘Honda Civic’ have. <br>

##
### Key Concepts and Functionalities:
#### 1. Column Selection
* **df['column_name']** - Accesses a specific column in the DataFrame. This returns the data of that column as a pandas Series.

#### 2.  Positional Indexing and Slicing
* **df.iloc[]** - Selects rows and columns by their integer positions. Consequently, using the slicing method specific rows or columns based on the index can be retrieved. Note that the general form of a slice is [start:stop:step].
> Sample Syntax and Output: <br>
> ![Screen Shot 2024-09-17 at 11 50 59 PM](https://github.com/user-attachments/assets/898b2767-99ce-42f2-96b0-03682729c92c)


#### 3. Boolean Indexing
* **(df[df['column_name'] == value])** - Filters rows in the DataFrame based on a condition. This technique allows you to retrieve rows where a certain condition is met.
> Sample Syntax and Output: <br>
> ![Screen Shot 2024-09-17 at 11 20 47 PM](https://github.com/user-attachments/assets/b4d25a99-d315-4673-8925-ed2ce6f4d098)

From this specific python excercise, the given function **(df[df['column_name'] == value])** is manipulated in various conditions like:
* (df[df['column 1'] == 'value']['column 2']) - Filters the DataFrame to return a series containing the values from column 2 for all rows where column 1 matches the specified value.
> Sample Syntax and Output: <br>
> ![Screen Shot 2024-09-17 at 11 42 20 PM](https://github.com/user-attachments/assets/b7ca89cf-3af4-41c3-ab1c-16e6e43b09a0)

* **df[df['column'].isin([...])]** - Filters the DataFrame to include only rows where the column matches one of the values in the provided list. The function **.isin([...])** checks if values in a column are part of a given list. This method is especially useful for filtering rows based on multiple possible values.
> Sample Syntax and Output: <br>
> ![Screen Shot 2024-09-17 at 11 35 15 PM](https://github.com/user-attachments/assets/a0a65e48-1957-4678-98a1-35dfaf2f071e)

***
### Reference:
ECE 2112: Numerical Python (Numpy) and Python Data Analysis (Pandas) PowerPoint Presentation by Engr. Ma. Madecheen S. Pangaliman

***
### Submitted by:
Michelle Sophia. Abamonga <br>
2023184181 <br>
2-ECEB 


