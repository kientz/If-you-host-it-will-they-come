import pandas as pd
import math
import zipcode  #for US Zipcodes

from geopy.distance import great_circle
from geopy.geocoders import Nominatim
# >>> newport_ri = (41.49008, -71.312796)
# >>> cleveland_oh = (41.499498, -81.695391)
# >>> print(great_circle(newport_ri, cleveland_oh).miles)
# 537.1485284062816

geolocator = Nominatim()
# location = geolocator.geocode("175 5th Avenue NYC")
# print(location.address)
# print((location.latitude, location.longitude))

def prepare_data(df):
    dffull.EventType.nunique()  #Count
    dffull.EventType.unique()  #List


    dffull.groupby(['EventType'])['EventType'].count()  #Count Events by Type
    #There are a small number of 5 types of events 1500 books, 1K Renewals - They will be dropped.
    #Keeping only Webcast and Conference

    df= dffull[dffull.EventType.isin(['Conference', 'Webcast'])]

    #Left with this:
    #Conference    11111
    #Webcast       19895  #31006 total

    #Clean up zip codes with the -XXXX  10 chars  to 5.
                   #11111
    not_in_database=0 #counter




    #164 not US or Canada Attendees

    #USE GEOPY
    #1200 Canadians

    return df


if __name__ == '__main__':
    #dffull =pd.read_excel('RealData.xlsx',skip_blank_lines=True,encoding = "ISO-8859-1")
    dffull =pd.read_excel('RealData_JustConferences.xlsx',skip_blank_lines=True,encoding = "ISO-8859-1")
    scrubbed=prepare_data(dffull)

    #dfUSA=df[dffull.country=='USA']  Subset just USA Countries


    unique_countries=list(scrubbed.country.unique())
