# hm14.py

# Ref:
# http://bokeh.pydata.org/en/latest/docs/gallery/heatmap_chart.html

# Demo:
# ~/anaconda3/bin/python hm14.py

import pandas as pd

from bokeh.charts   import HeatMap, bins, output_file, show
from bokeh.layouts  import column, gridplot
from bokeh.palettes import RdYlGn6, RdYlGn9

import pdb

yr_i     = 2014
yr_s     = str(yr_i)
feat0_df = pd.read_csv("feat.csv")
feat1_df = feat0_df[['cdate','pctlead','dow','moy']]
cdate_sr = (feat1_df.cdate > yr_s) & (feat1_df.cdate < str(yr_i+1))
feat2_df = feat1_df[cdate_sr]

hm0 = HeatMap(feat2_df, x=bins('dow'), y=bins('moy'), values='pctlead', stat='mean')

'bye'
