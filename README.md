# PA3 - PYTHON DATA ANALYSIS (PANDAS)
This repository contains Python scripts designed to address a range of programming problems in ECE2112. The focus is on DataFrame creation and the utilization of the NumPy library for numerical analysis. Presented below are the key concepts and functionalities used in the given Python exercises.

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
* **pd.read_csv('dataname.csv')** - Loads a CSV file into a pandas DataFrame, making it easy to work with structured data in Python.



#### 2. Basic DataFrame Operations
* **df.head()** - Allows user to quickly view the first few rows of a DataFrame. By deafult, first 5 rows are displayed.
<br> <br> Example: <br>
![Screen Shot 2024-09-17 at 11 05 02 PM](https://github.com/user-attachments/assets/0519e27e-2d53-42be-b494-19945c8f963e)


* **df.tail()** - Allows user to quickly view the last few rows of a DataFrame. By deafult, last 5 rows are displayed.
<br> <br> Example: <br>
![Screen Shot 2024-09-17 at 11 03 36 PM](https://github.com/user-attachments/assets/40648d7f-b732-4e02-a431-10b1cd15369d)
