import pandas as pd
import zipcode
from geopy.geocoders import Nominatim
from time import sleep
geolocator = Nominatim()


'''Basic Flow
1. Get Lat Long for all Non US Countries
2. Get Lat Long for all good US Zipcodes (fast)
3. Get Lat Long for missing Zipcodes and Canada cities based on
city and postal code (Slow)
4. Set Regions and super regions for each row
5. Calc Distance traveled to each conference based on lat long
'''

#df = df.reset_index()


def country_lat_long(df):
    '''For Countries outside of the US or Canada return the Lat/Long of the center of the country
    uses geolocator.geocode
    '''
    for i in range(len(df)):
        if df.country[i] != "Canada":
            if df.country[i] != "USA":
                #Not USA or Canada (145 cnt)
                temp=geolocator.geocode(df.country[i])
                df.Lat[i] = temp.latitude
                df.Long[i] = temp.longitude
                print(i, df.country[i], temp.address,temp.latitude, temp.longitude)
    return df



def us_zipcode_to_lat_long(df):
    '''This uses zipcode package to convert zip to lat long - doesn't find them all...
    '''
    not_in_database=0
    for i in range(len(df)):
        if df.country[i] == "USA":
            print(i)
            #Only check zip if USA
            if len(str(df.zip[i]))==10:  #set the length to 5 for the -XXXX Zips.
                df.zip[i]=df.zip[i][0:5]
            if df.Lat[i] > 0.0:
                print("SKIPPING IF LAT LONG IS ALREADY DEFINE")
            else:
                if isinstance(df.zip[i],(str,int)):  #Blanks become float nans - make sure string
                    if str(df.zip[i]).isdigit():  #look for 5 digits.
                        #Everything here is a 5 digit zip code
                        myzip=zipcode.isequal(str(df.zip[i]))
                        if myzip == None:  #can't find a match but it was a 5 digit zip.
                            not_in_database += 1
                            print('missing number:',i,':', df.city[i],':', df.state[i], df.zip[i],"totMiss",not_in_database)

                        else:
                            df.Lat[i] = myzip.lat
                            df.Long[i] = myzip.lon
                            #print(myzip.lat,myzip.lon)
                            print('input:', i,':', df.city[i],':', df.state[i],':',df.country[i],':','output:', myzip.lat, myzip.lon)
        print('missing number of zipcodes not in zipcode database', not_in_database)



def us_canada_city_state_lat_long(df):
    '''Use City and State (province code) to get remaining Lat Long data
    geocode
    '''
    not_in_database=0
    for i in range(len(df)):

        if df.Lat[i] > -90.0: #if lat is > -90 skip
            #If Lat is defined - we don't need to get it again!
            #run after zipcode so most us are good.
            pass
        else:
            temp=geolocator.geocode(df.city[i]+', '+ df.state[i])
            if temp == None:
                not_in_database += 1

                print('missing:',i,':', df.city[i],':', df.state[i],"TotMiss=",not_in_database)
            else:
                df.Lat[i] = temp.latitude
                df.Long[i] = temp.longitude
                print('input:', i,':', df.city[i],':', df.state[i],':',df.country[i],':','output:', temp.address,':',temp.latitude,':', temp.longitude)

        print("Number of locations (US and Canada) that were not in the database=",not_in_database)
        return df


if __name__ == '__main__':
    dffull =pd.read_excel('RealData_JustConferences.xlsx',skip_blank_lines=True,encoding = "ISO-8859-1")
    df2=country_lat_long(df)
    df3=us_zipcode_to_lat_long(df2)
    df4=us_canada_city_state_lat_long(df3)

    df4.to_csv('finaloutput.csv')
    #Will run calc_distance and set_region manually after this step.
