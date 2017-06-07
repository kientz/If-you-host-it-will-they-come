import pandas as pd
import numpy as np

#This is libre office vlookup for attendees per confernece
#=VLOOKUP(A4,'file:///home/skientz/galvanize/CAPSTONE/WEBType_Domain_count.xlsx'#$Type_Domain_count.$B$2:$H$11,2)

#TWO LEVEL PIVOTS - DOMAIN AND REGIONS
#Handle the Conferences first
df = pd.read_excel('RealData_JustConferences.xlsx')

k=df.pivot_table(index=['Domain','Super_Region'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('Domain_SuperRegion_distance_cost_count.csv')

k=df.pivot_table(index=['Domain','Region'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('Domain_Region_distance_cost_count.csv')


k=df.pivot_table(index=['Super_Region','Domain'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('SuperRegion_Domain_distance_cost_count.csv')


k=df.pivot_table(index=['Region','Domain'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('Region_Domain_distance_cost_count.csv')

#get the single level Pivots as well
k=df.pivot_table(index=['Domain'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('Domain_distance_cost_count.csv')


k=df.pivot_table(index=['Super_Region'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('SuperRegion_distance_cost_count.csv')


k=df.pivot_table(index=['Region'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('Region_distance_cost_count.csv')



#Now do the webcasts
df = pd.read_excel('RealData_JustWebcasts.xlsx')

m=df.pivot_table(index=['Domain','Super_Region'],values=['amtRevised'],aggfunc=[np.mean,np.median,np.std,len])
m.to_csv('WEBDomain_SuperRegion_cost_count.csv')

m=df.pivot_table(index=['Domain','Region'],values=['amtRevised'],aggfunc=[np.mean,np.median,np.std,len])
m.to_csv('WEBDomain_Region_cost_count.csv')


m=df.pivot_table(index=['Super_Region','Domain'],values=['amtRevised'],aggfunc=[np.mean,np.median,np.std,len])
m.to_csv('WEBSuperRegion_Domain_cost_count.csv')

m=df.pivot_table(index=['Region','Domain'],values=['amtRevised'],aggfunc=[np.mean,np.median,np.std,len])
m.to_csv('WEBRegion_Domain_cost_count.csv')

#get the single level Pivots as well
k=df.pivot_table(index=['Domain'],values=['amtRevised'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('WEBDomain_cost_count.csv')


k=df.pivot_table(index=['Super_Region'],values=['amtRevised'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('WEBSuperRegion_cost_count.csv')


k=df.pivot_table(index=['Region'],values=['amtRevised'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('WEBRegion_cost_count.csv')




#note with csv_read - these pivot table CSVs have a strange column header.  - this can handle it.
#df2 = pd.read_csv('Domain_Region_cost_count.csv',header=2)
#df2.rename(columns={'Unnamed: 2': 'Bob1', 'Unnamed: 3': 'Bob2'}, inplace=True)
