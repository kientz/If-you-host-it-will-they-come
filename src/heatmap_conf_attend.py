import pandas as pd
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns; sns.set()

''''Generate Heatmap of all location cities by domain'''
'''Z is the avg attend at any one conference'''

dfheat=pd.read_excel('LCity_Domain_distance_cost_count.xlsx')  #both Web and Conference
colnames=list(dfheat.columns)
dfh = dfheat.pivot("Domain","L_CityState","AVG_ATTEN_PER_CITY_DOMAIN")


plt.close()
ax = sns.heatmap(dfh, cmap="RdBu_r",annot=True)
ax.set_yticklabels(ax.yaxis.get_majorticklabels(), rotation=0)
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=90)

plt.show()
