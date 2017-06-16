import folium
import pandas as pd
import numpy as np
'''Generates a map with appropriate attendee clustering'''

from set_region_and_super_region import define_regions

# float_formatter = lambda x: "%.1f" % x
# np.set_printoptions(formatter={'float_kind':float_formatter})

superregions2, superregions, regions, regions2, state_to_code, code_to_state = define_regions()


srg=pd.read_csv('../data/superregions.csv')  #Get Lat Long of Region Centers
rg=pd.read_csv('../data/regions.csv')

#Region Lat Long
latrg = list(rg["LAT"])
lonrg = list(rg["LON"])
rgid = list(rg["REGIONS"])

#Super Region Lat Long and names
latsrg = list(srg["LAT"])
lonsrg = list(srg["LON"])
srgid = list(srg["SUPER_REGIONS"])

#df=pd.read_excel('conference_lat_long_and_counts.xlsx')
#df=pd.read_excel('Type_Domain_count.xlsx')  #both Web and Conference

df=pd.read_excel('../data/RealData_JustConferences.xlsx')  #both Web and Conference
colnames=list(df.columns)



# def color_producer(elevation):
#     if elevation < 1000:
#         return 'green'
#     elif 1000 <= elevation < 3000:
#         return 'orange'
#     else:
#         return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
#40.0150° N, 105.2705  Boulder

#one at a time
#map.add_child(folium.Marker(location=[38.2,-99.1]),popup="MARKER HERE",icon=folium.Icon(color='red'))

#Have map show base of  super regions colored differently

if False:
    fgSR = folium.FeatureGroup(name="SuperRegions")

    #fgSR.add_child(folium.GeoJson(data=open('gz_2010_us_040_00_500k.json', 'r', encoding='utf-8-sig'),
    #style_function = lambda feature: dict(color='red', weight=0.2, opacity=0.6))) #South

    fgSR.add_child(folium.GeoJson(data=open('gz_2010_us_040_00_500k.json', 'r', encoding='utf-8-sig'),
    style_function=lambda x: {'fillColor':
    'cyan' if x['properties']['NAME'] in superregions2['Northeast']
    else 'orange' if x['properties']['NAME'] in superregions2['Midwest']
    else 'red' if x['properties']['NAME'] in superregions2['West']
    else 'm','weight':0.1})) #South

    # #fgsrc = folium.FeatureGroup(name="SuperRegionCenters")  #feature group
    # for lt, ln, id in zip(latsrg, lonsrg,srgid):
    #      fgSR.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(id),
    #      fill_color='red', color = 'grey', fill_opacity=0.9))

if True:
    fgR = folium.FeatureGroup(name="Regions")

    fgR.add_child(folium.GeoJson(data=open('gz_2010_us_040_00_500k.json', 'r', encoding='utf-8-sig'),
    style_function=lambda x: {'fillColor':
    '#ffff00' if x['properties']['NAME'] in regions2['Great Lakes']
    else '#7fffd4' if x['properties']['NAME'] in regions2['Central Midwest']
    else '#b03060' if x['properties']['NAME'] in regions2['Mid-Atlantic']
    else '#cd853f' if x['properties']['NAME'] in regions2['Mountain States']
    else '#b22222' if x['properties']['NAME'] in regions2['Northwest']
    else '#ff0000' if x['properties']['NAME'] in regions2['South-Central']
    else '#00ff00' if x['properties']['NAME'] in regions2['Southeast']
    else '#0000ff' if x['properties']['NAME'] in regions2['Northeast']
    else '#a020f0','weight':0.1})) #Southwest

    # #Feature Group
    # #fgrc = folium.FeatureGroup(name="RegionCenters")  #or use fg
    # ##fgv.add_child(folium.Marker(location=[38.2,-99.1]),popup="MARKER HERE",icon=folium.Icon(color='red'))
    # for lt, ln, id in zip(latrg, lonrg,rgid):
    #      fgR.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(id),
    #      fill_color='red', color = 'grey', fill_opacity=0.9))




from folium.features import DivIcon
#m = folium.Map([45.0302, -105.22], zoom_start=13)
folium.map.Marker(
    [52.0, -100.0],
    icon=DivIcon(
        icon_size=(700,36),
        icon_anchor=(0,0),
        html='<div style="font-size: 24pt">Cluster Conference Attendees</div>',
        )
    ).add_to(map)

num_cities=len(df)

#df['Lat'][df['L_CityState']==i].count()
popup="one attendee"

marker_cluster = folium.MarkerCluster().add_to(map)
#fgCon = folium.FeatureGroup(name="AllAttendees")
for i in df['L_CityState'].unique():  #Step through CityState
    print(i)
    temptot=df['Lat'][df['L_CityState']==i].count()
    Lattemp=df['Lat'][df['L_CityState']==i].reset_index(drop=True)
    Longtemp=df['Long'][df['L_CityState']==i].reset_index(drop=True)
    for j in range(temptot):
        if j %20 ==0: print(j)
        folium.CircleMarker(location=[Lattemp[j],Longtemp[j]],color='red',fill_color='red',radius=2,popup=popup).add_to(marker_cluster)

'''
#do not include domains with 0 counts.
fgCon = folium.FeatureGroup(name="Conference")
for i in range(num_cities):
    html = '<i>' +  'Total Num Events: ' + sum(df['Num Events']).astype(str) + '<br>' +\
                    'Total Conferences: ' + str(ev_breakout[0]) + '<br>' +\
                    'Total Webcasts: ' + str(ev_breakout[1]) + '<br><br>' +\
                    ['Academic Administration: ' + df['Academic Administration'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Academic Administration'][i]),1))+'<br>',''][df['Academic Administration'][i]==0] +\
                    ['Advancement: ' + df['Advancement'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Advancement'][i]),1))+ '<br>',''][df['Advancement'][i]==0] +\
                    ['Enrollment Management: ' + df['Enrollment Management'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Enrollment Management'][i]),1))+ '<br>',''][df['Enrollment Management'][i]==0] +\
                    ['Leadership: ' + df['Leadership'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Leadership'][i]),1))+ '<br>',''][df['Leadership'][i]==0] +\
                    ['Physical Campus: ' + df['Physical Campus'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Physical Campus'][i]),1))+ '<br>',''][df['Physical Campus'][i]==0]+\
                    ['Planning & Finance: ' + df['Planning & Finance'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Planning & Finance'][i]),1))+ '<br>',''][df['Planning & Finance'][i]==0] +\
                    ['Student Affairs: ' + df['Student Affairs'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Student Affairs'][i]),1))+ '<br>',''][df['Student Affairs'][i]==0] +\
                    ['Teaching & Learning: ' + df['Teaching & Learning'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Teaching & Learning'][i]),1)) + '</i>','</i>'][df['Teaching & Learning'][i]==0]
    iframe = folium.IFrame(html=html, width=360, height=250)
    popup = folium.Popup(iframe, max_width=2650)

    #folium.CircleMarker(location=[df['L_lat'][i],df['L_lon'][i]],color='red',fill_color='red',radius=6,popup=popup).add_to(map)
fgCon.add_child(folium.CircleMarker(location=[40.0150, 105.2705],color='red',fill_color='red',radius=10,popup=popup))



    # for lt, ln, id in zip(latrg, lonrg,rgid):
    #     fgR.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(id),
    #     fill_color='red', color = 'grey', fill_opacity=0.9))

    # crime['text'] = '<i>' + 'Murder: ' + crime['Murder'].astype(str) + '<br>' +\
    #                 'Rape: ' + crime['Rape'].astype(str) + '<br>' +\
    #                 'Aggr. Aslt.: ' + crime['Aggravated Assault'].astype(str) + '</i>'

# df['L_CityState'][i] +
# str(df['Total Conferences'][i])+
# str(df['Academic Administration'][i])+
# str(df['Advancement'][i])+
# str(df['Enrollment Management'][i])+
# str(df['Leadership'][i])+
# str(df['Physical Campus'][i])+
# str(df['Planning & Finance'][i])+
# str(df['Student Affairs'][i])+
# str(df['Teaching & Learning'][i])
#
# df['L_CityState'][i] +str(df['Total Conferences'][i])+str(df['Academic Administration'][i])+str(df['Advancement'][i])+str(df['Enrollment Management'][i])+str(df['Leadership'][i])+str(df['Physical Campus'][i])+str(df['Planning & Finance'][i])+str(df['Student Affairs'][i])+str(df['Teaching & Learning'][i])

'''
#map.add_child(fgrc)
#map.add_child(fgsrc)
#map.add_child(fgSR)
map.add_child(fgR)
#map.add_child(fgCon)
map.add_child(folium.LayerControl())

map.save("Map_of_AllAttendees2.html")


# #Markers
# map_2 = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',  zoom_start=13)
#  folium.CircleMarker(location=[45.5215, -122.6261], radius=500,
#                          popup='Laurelhurst Park', color='#3186cc',
#      fill_color='#3186cc').add_to(map_2)
#
# folium.Marker(location=[45.5244, -122.6699], popup='The Waterfront').add_to(map_2)
# map_2.save("MarkersExamp.html")
