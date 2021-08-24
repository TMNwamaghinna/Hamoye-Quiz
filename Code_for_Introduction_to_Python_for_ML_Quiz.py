#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd #Importin the pandas package
import numpy as np #Importing the numpy package
import matplotlib.pyplot as plt #Importing the matplotlib package

data = pd.read_csv('Hamoye.csv') #Importing the dataset. Note that data from link has been previously stored as a CSV file in the folder

pd.set_option("precision", 2) #To provide all data in two decimal places
print(data) #To confirm that the right data was uploaded.
print(data.describe()) #This provides the statistical details of each column of the data. The print function is used to display the output.
print(" ") #to differentiate output for legibility

Lowest_Avg_fuel_burned = data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean() #This provides the mean of each item in the column fuel_type_code_pudl using details from fuel_cost_per_unit_burned
print(Lowest_Avg_fuel_burned) #This function is used to display output]
print(" ")

Skewness_fuel = data.skew() #used to generate the skewness of the dataset
Kurtosis_fuel = data.kurt() #used to generate the kurtosis of the dataset
print("Skewness of data is as below ", Skewness_fuel)
print(" ")
print("Kurtosis of data is as below ",Kurtosis_fuel)
print(" ")

pd.set_option("precision", 3) #To provide the data after this to three decimal places
Missing_values = data.isnull().sum().sort_values(ascending=False) #to find data with number of rows with missing values
Percent_missing = Missing_values / len(data) #to determine the percentage of the missing values
              
print(Missing_values) #to display the number of missing rows
print(Percent_missing) #to display the rows with missing values as a percentage of the total rows
print(" ")

correlation = data.corr() #determine the correlation of the data
print(correlation)
print(" ")

Year_with_highest_fuel_delivered = data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean() #This provides the mean of the fuel delivered by year
print(Year_with_highest_fuel_delivered.sort_values(ascending=False)) #This function is used to display output]




# In[ ]:





# In[ ]:





# In[ ]:




