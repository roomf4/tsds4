"""
hist1.py

This script should create a histogram plot from a CSV file.
"""

import pandas as pd
import matplotlib.pyplot as plt

my_df    = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
sp0_sr   = (my_df.cdate > '2016') & (my_df.cdate < '2017')
sp0_df   = my_df[sp0_sr]
day1g_sr = sp0_df.pctlag1
plt.hist(day1g_sr)
plt.show()
'bye'
