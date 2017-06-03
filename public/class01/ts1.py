"""
ts1.py
This script should plot a time series of prices.
"""

import matplotlib.pyplot as plt
import pandas            as pd

my_df    = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')
sp0_sr   = my_df.cdate > '2016'
sp1_sr   = my_df.cdate < '2017'
sp2_sr   = (sp0_sr & sp1_sr)
sp0_df   = my_df[sp2_sr]
cdate_sr = sp0_df.cdate
cp_sr    = sp0_df.cp
  
# matplotlib likes datetime:
cdate_dt_sr = pd.to_datetime(cdate_sr)

# cdate_dt_sr holds x values, cp_sr: y values
plt.plot(cdate_dt_sr, cp_sr)
plt.show()
'bye'
