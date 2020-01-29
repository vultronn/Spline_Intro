#%% Import Modules
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
%matplotlib inline

This notebook walks through the exercise used in https://www.analyticsvidhya.com/blog/2018/03/introduction-regression-splines-python-codes/

#%% Read in Data
df = pd.read_csv('Wage.csv')

# %%
df.head()

# %%
