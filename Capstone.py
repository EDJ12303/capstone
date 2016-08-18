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
import datetime

#This program plots NIH funding for cancer immunotherapy as well as
#the number of clinical trials for cancer immunotherapy from 1997-2015

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
#convert to millions
SumFunds = (SumFunds/1000000)
print SumFunds

#plot sumfunds versus year
# The dependent variable
y = SumFunds
# The independent variables shaped as columns
x = UniqueYear2

plt.scatter(x,y)

#read in the ClinicalTrials data
Trials = pd.read_csv('C:\Users\Erin\immunotherapy_trials.csv', parse_dates=['Start Date'])
print Trials['Start Date'][0:10]

#split start date column to extract year
Trials['year']= Trials['Start Date'].apply(lambda x: x.split('/')[-1])
print Trials['year'][0:15]


#count frequency of studies per year
CountTrials = Trials.groupby(by=['year'])['Title'].count()
CountTrials2 = CountTrials[0:19]
print "CountTrials2"
print CountTrials2[0:19]

#convert to numeric
Trials2= Trials.apply(pd.to_numeric, errors='coerce')
#get unique list of years
YearList = pd.unique(Trials2['year'].ravel())
YearList2 = YearList[0:19]
print "YearList" 
print YearList
#get correct years, 1997-2015
print "YearList2" 
print YearList2

#plot number of studies versus year
y2 = CountTrials2
x2 = YearList2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x2, y, 'o-', label = 'Funding')
ax2 = ax.twinx()
ax2.plot(x2, y2, 'xr-', label = 'Trials')
ax.legend(loc=0)
ax2.legend(loc=4)
ax.grid()
ax.set_xlabel("Year")
ax.set_ylabel(r"Funding in Millions of $")
ax2.set_ylabel(r"# Clinical Trials")
ax2.set_ylim(0, 180)
ax.set_ylim(0, 450)
ax.set_xlim(1997, 2015)
ax.set_title('Cancer Immunotherapy Funding and Clinical Trials, 1997-2015')
plt.show()
