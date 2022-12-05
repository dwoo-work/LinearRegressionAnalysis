# Import libraries

import pandas as pd
import numpy as np
import scipy.stats as st

# Import specific functions from Scipy and SKLearn

from scipy.stats import kstest
from sklearn.linear_model import LinearRegression

# Read the CSV File

sales = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/Linear_Regression_Analysis_using_Python/main/src/sales_data_sample_utf8.csv')

# Create list variables

columns_list = list(sales)
productLine_list = list(sales['PRODUCTLINE'].unique())

# Create table variables for each of the product line (for this code, only Motorcycles is evaluated)

specific_columns = pd.DataFrame(sales, columns = ["QUANTITYORDERED","PRICEEACH","PRODUCTLINE"])
motorcycles = specific_columns[specific_columns['PRODUCTLINE'].str.match('Motorcycles')]

# Make Quantity Ordered as an Array

qtyOrdered = np.array(motorcycles['QUANTITYORDERED'])

# Identify if the motorcycles data is normally distributed

mean = qtyOrdered.mean()
sd = qtyOrdered.std()

kstest(qtyOrdered,'norm',args=(mean, sd)) # pvalue=0.0774262, as P>0.05, it is reasonable to accept that the quantity ordered is normally distributed.

# Identify the relationship between the quantity ordered, and the unit price for motorcycles data

x = motorcycles[['PRICEEACH']]
y = motorcycles[['QUANTITYORDERED']]

model = LinearRegression().fit(x,y)

model.coef_ # array([[0.02305362]]). For every $1 increase in unit price, there is a 0.0231 decrease in demand.
model.intercept_ # array([33.32225513]). If the motorcycle is sold at S0, there will be a demand of 33.3 units.