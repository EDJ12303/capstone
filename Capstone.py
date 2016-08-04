# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:59:06 2016

@author: Erin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats

NIHfunding = pd.read_csv('C:\Users\Erin\SR_18May2016_074615_11063347.csv', skiprows=3, header=0, usecols=[9,10], names=['FY', 'FY Total Cost'], date_parser=True, skip_blank_lines=True)

print NIHfunding['FY Total Cost'][1201:1500]

#convert columns to numeric
NIHfunding2 = NIHfunding.apply(pd.to_numeric, errors='coerce')

#create variables for columns
Year = NIHfunding2['FY']
Funds = NIHfunding2['FY Total Cost']

#need a singe instance of each year (new column)

UniqueYear = pd.unique(NIHfunding2['FY'].ravel())
UniqueYear2 = UniqueYear[1:20]
print 'UniqueYear2='
print UniqueYear2

#need total funding for each year
SumFunds = NIHfunding2.groupby(by=['FY'])['FY Total Cost'].sum()

print SumFunds


# The dependent variable
y = SumFunds
# The independent variables shaped as columns
x = UniqueYear2

plt.scatter(x,y)



