# hm15.py

# Ref:
# http://bokeh.pydata.org/en/latest/docs/gallery/heatmap_chart.html

# Demo:
# ~/anaconda3/bin/python hm15.py

import pandas as pd
from bokeh.charts   import HeatMap, bins, output_file, show
from bokeh.layouts  import column, gridplot
from bokeh.palettes import RdYlGn6, RdYlGn9

yr_i     = 1990
yr_s     = str(yr_i)
feat0_df = pd.read_csv("feat.csv")
feat1_df = feat0_df[['cdate','pctlead','pctlag1','dow','moy']]
cdate_sr = (feat1_df.cdate > yr_s)
feat2_df = feat1_df[cdate_sr]

lagdown_sr = (feat2_df.pctlag1 < 0.0)
lagup_sr   = (feat2_df.pctlag1 > 0.0)
lagdown_df = feat2_df[lagdown_sr]
lagup_df   = feat2_df[lagup_sr]

tools_s  = 'box_zoom,box_select,crosshair,resize,reset,save,help'

hm6 = HeatMap(lagdown_df
              ,x     ='dow'
              ,y     ='moy'
              ,values='pctlead'
              ,stat  ='mean'
              ,tools = tools_s
              ,legend='top_right'
              ,title ='Lag-down Heatmap'
              ,xlabel='Day Of Week'
              ,ylabel='Month Of Year'
              ,palette      =RdYlGn9
              ,spacing_ratio=0.9
              ,width        =900
              ,plot_height  =900
              )

hm7 = HeatMap(lagup_df
              ,x     ='dow'
              ,y     ='moy'
              ,values='pctlead'
              ,stat  ='mean'
              ,tools = tools_s
              ,legend='top_right'
              ,title ='Lag-up Heatmap'
              ,xlabel='Day Of Week'
              ,ylabel='Month Of Year'
              ,palette      =RdYlGn9
              ,spacing_ratio=0.9
              ,width        =900
              ,plot_height  =900
              )

output_file('hm15.html', title='Bokeh heatmap example (hm15.py)')

show(column(hm6,hm7))

'bye'
