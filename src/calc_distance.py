from geopy.distance import great_circle
import pandas as pd
import numpy as np



def calc_great_dist(df):
    '''This will compute the distance between the antendee and the conference location
    uses the Lat Long data to compute the great circle distance
    Then it will write to the output CSV with the DistanceTraveled column filled out in miles
    '''

    for row in range(len(df)):
         df.DistanceTraveled[row]=great_circle((df['Lat'][row], df['Long'][row]),(df['L_Lat'][row], df['L_Long'][row])).miles
         print("processing distance for row number: ", row) #debug

    return df



if __name__ == '__main__':
    df =pd.read_excel('../data/RealData_JustConferences.xlsx',skip_blank_lines=True,encoding = "ISO-8859-1")
    df2 = calc_great_dist(df)
    print("Writing CSV file with distances calculated")
    df2.to_csv('RealData_conference_with_distance.csv')
