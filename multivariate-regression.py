import pandas as pd
import statsmodels.api as sm

df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls') 

df['Model_ord'] = pd.Categorical(df.Model).codes
X = df[['Mileage', 'Model_ord', 'Doors']]
y = df[['Price']]

x1 = sm.add_constant(X)
est = sm.OLS(y, x1).fit()

est.summary()

print(est.summary())