from geopy.distance import great_circle
import pandas as pd
import numpy as np



def calc_great_dist_regions(df):
    '''For Each region compute the distance to every other region from the LAT LON
    Returns Lists with Reg and Dist frame with all this new distance data  - for 14 regions there are 91 pairs
    miles
    '''
    REGSTART=[]
    REGEND=[]
    DIST=[]

    for i,reg1 in enumerate(df.REGIONS):
        for j,reg2 in enumerate(df.REGIONS):
            REGSTART.append(reg1)
            REGEND.append(reg2)
            DIST.append(great_circle((df['LAT'][i], df['LON'][i]),(df['LAT'][j], df['LON'][j])).miles)
            print('Calculating Distance Between ', reg1, ' and ', reg2, ' is ', DIST[i*j+j], ' miles')
            df2 = pd.DataFrame(
            {'Start Region': REGSTART,
            'End Region': REGEND,
            'Distance': DIST
            })


    #return REGSTART, REGEND, DIST
    return df2
if __name__ == '__main__':
    df =pd.read_csv('../data/regions.csv')
    df2 = calc_great_dist_regions(df)
    print("Writing CSV file with distances calculated")
    df2.to_csv('Region_Distances.csv')
