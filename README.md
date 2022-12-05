# Linear_Regression_Analysis_using_Python

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

## The Flow

Firstly, we have to find out if the data is having a normal distribution. This can be done, by using the [Kolmogorov–Smirnov test](https://towardsdatascience.com/kolmogorov-smirnov-test-84c92fb4158d), which will tell us if the sample comes from a population with a specific distribution (in this case, a normal distribution).

Next, if the data follows a normal distribution, we can perform [Linear Regression](https://www.ibm.com/sg-en/topics/linear-regression) to find out the best fit line for the two variables. The first variable is the quantity ordered (demand), and the other variables is the price for each item (price).

Then, once the best fit line is determined, find out the coefficient value, and the intercept value. These two variables will provide you with insight, on the relationship between the demand, and the price.

## Credit

[Sales_Data_Sample] (https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

## License

[MIT](https://choosealicense.com/licenses/mit/)