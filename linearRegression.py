import pandas as pd
import numpy as np
import scipy.stats as st

from scipy.stats import kstest
from sklearn.linear_model import LinearRegression

sales = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/Linear_Regression_Analysis_using_Python/main/src/sales_data_sample_utf8.csv')

columns_list = list(sales)
productLine_list = list(sales['PRODUCTLINE'].unique())

specific_columns = pd.DataFrame(sales, columns = ["QUANTITYORDERED","PRICEEACH","PRODUCTLINE"])
motorcycles = specific_columns[specific_columns['PRODUCTLINE'].str.match('Motorcycles')]

qtyOrdered = np.array(motorcycles['QUANTITYORDERED'])

mean = qtyOrdered.mean()
sd = qtyOrdered.std()
kstest(qtyOrdered,'norm',args=(mean, sd))

x = motorcycles[['PRICEEACH']]
y = motorcycles[['QUANTITYORDERED']]
model = LinearRegression().fit(x,y)
model.coef_
model.intercept_