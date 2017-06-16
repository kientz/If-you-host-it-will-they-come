import pandas as pd
import numpy as np


#TWO LEVEL PIVOTS - DOMAIN AND REGIONS
#Handle the Conferences first
df = pd.read_excel('../data/ALLEVENT_Data.xlsx')



k=df.pivot_table(index=['Type','Domain','L_City'],values=['shortName'],aggfunc=[len])
k.to_csv('ConfOnlyType_Domain_LCity_count.csv')


k=df.pivot_table(index=['Type','Domain'],values=['shortName'],aggfunc=[len])
k.to_csv('Type_Domain_count.csv')

#note with csv_read - these pivot table CSVs have a strange column header.  - this can handle it.
#df2 = pd.read_csv('Domain_Region_cost_count.csv',header=2)
#df2.rename(columns={'Unnamed: 2': 'Bob1', 'Unnamed: 3': 'Bob2'}, inplace=True)
