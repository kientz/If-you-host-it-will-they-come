import folium
import pandas as pd
import numpy as np

from set_region_and_super_region import define_regions

superregions2, superregions, regions, regions2, state_to_code, code_to_state = define_regions()


srg=pd.read_csv('superregions.csv')  #Get Lat Long of Region Centers
rg=pd.read_csv('regions.csv')

latrg = list(rg["LAT"])
lonrg = list(rg["LON"])
rgid = list(rg["REGIONS"])

latsrg = list(srg["LAT"])
lonsrg = list(srg["LON"])
srgid = list(srg["SUPER_REGIONS"])

dfrd=pd.read_excel('RealData_JustConferences.xlsx',sheetname='Pivot_Conf_Region_Domain_by_attendee')
lendfrd=len(dfrd)
dfr=pd.read_excel('RealData_JustConferences.xlsx',sheetname='Pivot Cof_Region_by_Attendee')
lendfr=len(dfr)
dfrd.fillna(0,inplace=True)

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
# map = folium.Map(location=[38.58, -99.09], zoom_start=2, tiles="OpenStreetMap")

#one at a time
#map.add_child(folium.Marker(location=[38.2,-99.1]),popup="MARKER HERE",icon=folium.Icon(color='red'))

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
    #fgsrc = folium.FeatureGroup(name="SuperRegionCenters")  #feature group
    for lt, ln, id in zip(latsrg, lonsrg,srgid):
         fgSR.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(id),
         fill_color='red', color = 'grey', fill_opacity=0.9))

'''
<table>
 <tr>
  <th>Name</th>
  <th>Favorite Color</th>
 </tr>
 <tr>
  <td>Bob</td>
  <td>Yellow</td>
 </tr>
 <tr>
  <td>Michelle</td>
  <td>Purple</td>
 </tr>
</table>
'''




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


    #Feature Group
    #fgrc = folium.FeatureGroup(name="RegionCenters")  #or use fg
    ##fgv.add_child(folium.Marker(location=[38.2,-99.1]),popup="MARKER HERE",icon=folium.Icon(color='red'))


    #Used columns
    #L_Region	Total Conf in Region	Total Attendance Result,	Percentage From Home Region,Avg Attend per conference By Region, LAT,LON

    dom_list=list(dfrd.Domain.unique())

    for i in range(lendfr):  #14
        #set up vars to use as indicies

        reg=dfr['L_Region'][i]
        tcon=str(dfr['Total Conf in Region'][i])
        tatt=str(dfr['Total Attendance Result'][i])
        aatt=str(round(float(dfr['Avg Attend per conference By Region'][i]),1))
        phome=str(round((float(dfr['Percentage From Home Region'][i])*100),2))

        if float(tcon)<5:
            rad=5
        else:
            rad = float(tcon)
        a0=[]
        a=[]
        b=[]
        c=[]
        d=[]
        for  j , dom  in enumerate(dom_list):
            a0.append(dom)
            atemp=str(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Total Attendance Result'].reset_index()['Total Attendance Result'][0])
            a.append(atemp)
            #a.append(str(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Total Attendance Result'][j]))
            btemp=str(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Total Conf by Domain in Region'].reset_index()['Total Conf by Domain in Region'][0])
            b.append(btemp)
            #b.append(str(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Total Conf by Domain in Region'][j]))
            ctemp=str(round(float(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Avg_Attend_Region_domain'].reset_index()['Avg_Attend_Region_domain'][0]),1))
            c.append(ctemp)
            #c.append(str(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Avg_Attend_Region_domain'][j]))
            dtemp=str(round((float(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Percentage From Home'].reset_index()['Percentage From Home'][0])*100),2))
            d.append(dtemp)
            #d.append(str(dfrd.loc[(dfrd.L_Region == reg) & (dfrd.Domain == dom),'Percentage From Home'][j]))
            # print(reg, "a0",a0)
            # print("a",a)
            # print("b",b)
            # print("c",c)
            # print("d",d)

        html = '<i>' + 'Region: ' + reg +  '<br>'+\
        'Total Num Conferences in Region: ' + tcon + '<br>' +\
        'Total Conference Attendees: ' + tatt + '<br>' +\
        'Avg Conference Attendace for Region: ' + aatt + '<br>' +\
        'Percentage of home region attendees: ' + phome + '%<br><br>' +\
        '<table><tr> <th>Domain</th><th>Attend</th><th>Num_Conf</th><th>Avg_Attend</th><th>Att_from_Home_Reg</th></tr>' +\
        '<tr> <td>'+ a0[0] + '</td>  <td>'+ str(a[0]) + '</td> <td>' + str(b[0]) + '</td>  <td>'+ str(c[0]) + '</td>  <td>'+ str(d[0]) + '%</td> </tr>'  +\
        '<tr> <td>'+ a0[1] + '</td>  <td>'+ str(a[1]) + '</td> <td>' + str(b[1]) + '</td>  <td>'+ str(c[1]) + '</td>  <td>'+ str(d[1]) + '%</td> </tr>'  +\
        '<tr> <td>'+ a0[2] + '</td>  <td>'+ str(a[2]) + '</td> <td>' + str(b[2]) + '</td>  <td>'+ str(c[2]) + '</td>  <td>'+ str(d[2]) + '%</td> </tr>'  +\
        '<tr> <td>'+ a0[3] + '</td>  <td>'+ str(a[3]) + '</td> <td>' + str(b[3]) + '</td>  <td>'+ str(c[3]) + '</td>  <td>'+ str(d[3]) + '%</td> </tr>'  +\
        '<tr> <td>'+ a0[4] + '</td>  <td>'+ str(a[4]) + '</td> <td>' + str(b[4]) + '</td>  <td>'+ str(c[4]) + '</td>  <td>'+ str(d[4]) + '%</td> </tr>'  +\
        '<tr> <td>'+ a0[5] + '</td>  <td>'+ str(a[5]) + '</td> <td>' + str(b[5]) + '</td>  <td>'+ str(c[5]) + '</td>  <td>'+ str(d[5]) + '%</td> </tr>'  +\
        '<tr> <td>'+ a0[6] + '</td>  <td>'+ str(a[6]) + '</td> <td>' + str(b[6]) + '</td>  <td>'+ str(c[6]) + '</td>  <td>'+ str(d[6]) + '%</td> </tr>'  +\
        '<tr> <td>'+ a0[7] + '</td>  <td>'+ str(a[7]) + '</td> <td>' + str(b[7]) + '</td>  <td>'+ str(c[7]) + '</td>  <td>'+ str(d[7]) + '%</td> </tr>'  +\
        '</table></i>'
        #['Academic Administration: ' + df['Academic Administration'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Academic Administration'][i]),1))+'<br>',''][df['Academic Administration'][i]==0] +\
        # ['Advancement: ' + df['Advancement'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Advancement'][i]),1))+ '<br>',''][df['Advancement'][i]==0] +\
        # ['Enrollment Management: ' + df['Enrollment Management'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Enrollment Management'][i]),1))+ '<br>',''][df['Enrollment Management'][i]==0] +\
        # ['Leadership: ' + df['Leadership'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Leadership'][i]),1))+ '<br>',''][df['Leadership'][i]==0] +\
        # ['Physical Campus: ' + df['Physical Campus'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Physical Campus'][i]),1))+ '<br>',''][df['Physical Campus'][i]==0]+\
        # ['Planning & Finance: ' + df['Planning & Finance'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Planning & Finance'][i]),1))+ '<br>',''][df['Planning & Finance'][i]==0] +\
        # ['Student Affairs: ' + df['Student Affairs'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Student Affairs'][i]),1))+ '<br>',''][df['Student Affairs'][i]==0] +\
        # ['Teaching & Learning: ' + df['Teaching & Learning'][i].astype(str) + '      ' + str(round(float(df['Avg Atten Teaching & Learning'][i]),1)) + '</i>','</i>'][df['Teaching & Learning'][i]==0]

        iframe = folium.IFrame(html=html, width=750, height=370)
        popup = folium.Popup(iframe, max_width=2650)

        #popup ="hey"


        fgR.add_child(folium.CircleMarker(location=[dfr['LAT'][i], dfr['LON'][i]], radius = rad, popup=popup,
        fill_color='red', color = 'grey', fill_opacity=0.9))



from folium.features import DivIcon
#m = folium.Map([45.0302, -105.22], zoom_start=13)
folium.map.Marker(
    [52, -105.2352],
    icon=DivIcon(
        icon_size=(700,120),
        icon_anchor=(0,0),
        html='<div style="font-size: 24pt">Domain Attendance by Region</div>',
        )
    ).add_to(map)



#map.add_child(fgSR)
map.add_child(fgR)
map.add_child(folium.LayerControl())

map.save("Map_of_Regions.html")


# #Markers
# map_2 = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner',  zoom_start=13)
# folium.CircleMarker(location=[45.5215, -122.6261], radius=500,
#                          popup='Laurelhurst Park', color='#3186cc',
#      fill_color='#3186cc').add_to(map_2)
#
# folium.Marker(location=[45.5244, -122.6699], popup='The Waterfront').add_to(map_2)
# map_2.save("MarkersExamp.html")
