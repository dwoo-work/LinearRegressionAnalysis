# Import the relevant libraries

import pandas as pd
import numpy as np
import scipy.stats as st

# Import kstest function from Scipy, and Linear Regression function from SKLearn

from scipy.stats import kstest
from sklearn.linear_model import LinearRegression

vehicle = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/Linear_Regression_Analysis_using_Python/main/src/sales_data_sample_utf8.csv')
