#!/usr/bin/python

import pandas as pd
import numpy as np
import pylab as P
import matplotlib.pyplot as plt
from array import array
from scipy import stats
from scipy.stats import beta
from sets import Set
import random
import sys
import datetime as dt

cluster5 = [476, 513, 471,477,479, 474, 467, 518, 468, 581, 809, 473, 210]

""" This code was used to create the 'Week end' column
dailySales = pd.read_csv("SalesbyDay.csv")
print "Daily sales initially has " , len(dailySales), "rows"
dailySales['BusinessDate'] = pd.to_datetime(dailySales['BusinessDate'], format="%m/%d/%Y 0:00")
dailySales['DOW'] = dailySales['BusinessDate'].dt.dayofweek

#print dailySales.ix[0:10,'DOW']
for n in range(len(dailySales)):
    dailySales.ix[n,'WkEndSun'] = dailySales.ix[n,'BusinessDate'] + dt.timedelta((6 - dailySales.ix[n,'DOW']) % 7)

dailySales.to_csv('DailySales_with_WkEnd.csv')
"""

dailySales = pd.read_csv("DailySales_with_WkEnd.csv")
dailySales['BusinessDate'] = pd.to_datetime(dailySales['BusinessDate'], format="%Y-%m-%d 00:00:00")
dailySales['WkEndSun'] = pd.to_datetime(dailySales['WkEndSun'], format = "%Y-%m-%d 00:00:00")
baCols = list(dailySales.columns.values)
print "dailySales has ", len(baCols), " columns like ", baCols[0], " ", baCols[1], " ", baCols[6]
baRows = list(dailySales.index.values)
print "dailySales has ", len(baRows), " rows like ", baRows[0], " ", baRows[1]
print dailySales.ix[0:10,'DOW']

numStores = len(cluster5)
store = 0
#ax = [None] * numStores

for storeNum in cluster5[:1]:
    print 'Results for store', storeNum
    storeSales = dailySales[dailySales['Store_Id'] == storeNum]
    storeSales.reindex
    noSales = storeSales[storeSales['NetSales'] == 0]
    if len(noSales) > 0:
        print 'No Sales on ', len(noSales), ' dates:'
        print noSales['BusinessDate']
        #storeSales['NetSales'].replace(0, np.nan)

    #storeStats = storeSales.describe()
    print storeSales['NetSales'].describe()
    xticks = storeSales['NetSales'].index.values
    xlabs = [storeSales[x]['WkEndSun'] for x in xticks ]        
    #print storeSales[0:10]
    f,ax = plt.subplots(1,1,1)
    storeSales['NetSales'].plot(style='o-',ax=ax)

    #plt.set_ylabel('Store ' + str(storeNum))
    plt.axis([0,1100,0,7500])
    #ax.set_xticks(days, ticklabs)
    #plt.set_xlabel('Daily Net Sales')
    #plt.savefig("wand" + str(storeNum)+ ".pdf", format = 'pdf')
plt.show()    
