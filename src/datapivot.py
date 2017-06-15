import pandas as pd
import numpy as np

'''generates a bunch of csv pivot tables'''

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

k=df.pivot_table(index=['L_Region','Domain'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('L_Region_Domain_distance_cost_count.csv')

k=df.pivot_table(index=['L_CityState','Domain'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('L_CityState_Domain_distance_cost_count.csv')

k=df.pivot_table(index=['L_CityState','L_Region'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('L_CityState_L_Region_distance_cost_count.csv')

k=df.pivot_table(index=['L_Region','L_CityState'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('L_Region_L_CityState_distance_cost_count.csv')

k=df.pivot_table(index=['L_CityState','Region'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('L_CityState_Region_distance_cost_count.csv')

k=df.pivot_table(index=['L_CityState'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k.to_csv('L_CityState_distance_cost_count.csv')

k=df.pivot_table(index=['L_Region','Region'],values=['amtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
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





#GOOD
#Get num of conf per city
df=pd.read_csv('ConfOnly_Type_Domain_LCity_count.csv')
df.columns
k=df.pivot_table(index=['L_City'],values=['Number of Repeats of Topic in City'],aggfunc=[np.sum])
k.to_csv('Num_of_Conf_per_City.csv')

#GOOD
k2=dfcity.pivot_table(index=['L_City','Domain'],values=['Number of Repeats of Topic in City'],aggfunc=[np.sum])
k2.to_csv('Num_of_Conf_per_City_Domain.csv')


k3=df.pivot_table(index=['Region'],values=['AmtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k3.to_csv('Num_of_Conf_By_Region.csv')

k4=df.pivot_table(index=['Region','Domain'],values=['AmtRevised','DistanceTraveled'],aggfunc=[np.mean,np.median,np.std,len])
k4.to_csv('Num_of_Conf_By_Region_Domain.csv')

k5=dfcity.pivot_table(index=['Region','Domain'],values=['Number of Repeats of Topic in City'],aggfunc=[np.sum])
k5.to_csv('Num_of_Conf_per_Region_Domain.csv')





#Section on Conference Location and breakdown - no users
dfconf=pd.read_excel('ALLCONFERENCEEVENT_Data.xlsx')
dfconf.columns
k6=dfconf.pivot_table(index=['L_Region','Domain'],values=['L_Lat'],aggfunc=[len])
k6.to_csv('Num_of_EVENTS_per_Region_Domain.csv')

k7=dfconf.pivot_table(index=['L_Region'],values=['L_Lat'],aggfunc=[len])
k7.to_csv('Num_of_EVENTS_per_Region.csv')

k8=dfconf.pivot_table(index=['L_CityState'],values=['L_Lat'],aggfunc=[len])
k8.to_csv('Num_of_EVENTS_per_L_CityState.csv')

k9=dfconf.pivot_table(index=['L_Region','Domain'],values=['L_Lat'],aggfunc=[len])
k9.to_csv('Num_of_EVENTS_per_Region_Domain.csv')

k10=dfconf.pivot_table(index=['L_CityState','Domain'],values=['L_Lat'],aggfunc=[len])
k10.to_csv('Num_of_EVENTS_per_L_CityState_Domain.csv')

k11=dfconf.pivot_table(index=['L_CityState','L_Region'],values=['L_Lat'],aggfunc=[len])
k11.to_csv('Num_of_EVENTS_per_L_CityState_L_Region.csv')

k12=dfconf.pivot_table(index=['L_Region','L_CityState'],values=['L_Lat'],aggfunc=[len])
k12.to_csv('Num_of_EVENTS_per_L_Region_L_CityState.csv')






#note with csv_read - these pivot table CSVs have a strange column header.  - this can handle it.
#df2 = pd.read_csv('Domain_Region_cost_count.csv',header=2)
#df2.rename(columns={'Unnamed: 2': 'Bob1', 'Unnamed: 3': 'Bob2'}, inplace=True)
