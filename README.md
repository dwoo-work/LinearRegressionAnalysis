# Linear Regression Analysis

This will demonstrate to you how to perform linear regression analysis using Python.

Performing supply chain statistical analysis is important, because it allows us to capture uncertainty that arises within the supply chain.

There is a need to analyse and characterise the distribution of the data, because it will give you a sense of how much supply to have, to fulfill x% of customer's demand at any day.

As a supply chain professional, the ultimate aim is to find a balance between satisfying the customer's demand, as well as reducing cost from having unnecessary supplies in the warehouse.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:

- pandas: to perform data administration by pulling in .csv or .xlsx files.
- numpy: to perform data manipulation by establishing arrays.
- scipy: to perform data analysis using random variables and probability distribution.
- scikit-learn: to perform predictive data analysis.

```bash
pip install pandas
pip install numpy
pip install scipy
pip install scikit-learn
```

## Sample Dataset

You can download the sales_data_sample_utf8.csv file from the source folder, which is located [here](https://github.com/dwoo-work/Linear_Regression_Analysis_using_Python/tree/main/src).

Ensure that the file is in CSV UTF-8 format, to avoid UnicodeDecodeError later on.

## Code Explanation

Lines 1-3:  
To import required libraries like Pandas, Numpy, and Scipy
```python   
import pandas as pd
import numpy as np
import scipy.stats as st
```

Lines 5-6:
To import specific functions from Scipy and SKLearn
```python   
from scipy.stats import kstest
from sklearn.linear_model import LinearRegression
```

Line 8:
Read the CSV file
```python   
sales = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/Linear_Regression_Analysis_using_Python/main/src/sales_data_sample_utf8.csv')
```

Line 10-11:
Create list variables to understand file structure.
Line 10 identifies the different kinds of column titles within the CSV file.
Line 11 identifies the different kinds of vehicles that are sold, and compiled within the CSV file.
```python   
columns_list = list(sales)
productLine_list = list(sales['PRODUCTLINE'].unique()))
```

Line 13-14:
Create table variables for each of the product line. For demonstration, we will only be analysing Motorcycles data.
```python   
specific_columns = pd.DataFrame(sales, columns = ["QUANTITYORDERED","PRICEEACH","PRODUCTLINE"])
motorcycles = specific_columns[specific_columns['PRODUCTLINE'].str.match('Motorcycles')]
```

Line 16:
Make Quantity Ordered as an array, because for SKLearn, in order to train the data to use fit method in linear regression, we have to reshape the 1D arrays.
```python   
qtyOrdered = np.array(motorcycles['QUANTITYORDERED'])
```

Line 18-20:
Identify if the motorcycles data is normally distributed

pvalue=0.0774262. As P>0.05, it is reasonable to accept that the quantity ordered is normally distributed.
```python   
mean = qtyOrdered.mean()
sd = qtyOrdered.std()
kstest(qtyOrdered,'norm',args=(mean, sd))
```

Line 22-26:
Identify the relationship between the quantity ordered, and the unit price for motorcycles data.

model.coef_ = array([[0.02305362]]). For every $1 increase in unit price, there is a 0.0231 decrease in demand.

On the other hand, model.intercept_ = array([33.32225513]). If the motorcycle is sold at S0, there will be a demand of 33.3 units.
```python   
x = motorcycles[['PRICEEACH']]
y = motorcycles[['QUANTITYORDERED']]
model = LinearRegression().fit(x,y)
model.coef_
model.intercept_
```

## Credit

Sales Data Sample (https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

## License

[MIT](https://choosealicense.com/licenses/mit/)
