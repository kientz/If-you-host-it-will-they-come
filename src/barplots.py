import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_bar_plot(names, values,ylabel='y',xlabel='x', title='title', figname ='basic_bargraph.png'):
    #Sort bar graph!
    idx_values=values.argsort()
    sorted_values = values[idx_values]
    sorted_names = names[idx_values]

    y_ind = np.arange(len(sorted_names)) # 9 to 0
    fig = plt.figure(figsize=(10, 10))
    plt.barh(y_ind, sorted_values, height = 0.5, align='center')
    plt.ylim(y_ind.min() - 0.5, y_ind.max() + 0.5)
    plt.yticks(y_ind, sorted_names,fontsize=18)
    plt.xlabel(xlabel,fontsize=18)
    plt.title(title,fontsize=24)
    plt.ylabel(ylabel,fontsize=18)
    plt.tight_layout()
    figname = figname
    plt.savefig(figname, dpi = 100)
    #plt.close()

if __name__ == '__main__':


    #3 total attend by category - also avg attendence by Domain_distance_cost_count
    #2x for the Web - 8 plots will be made

    if True:
        title='CONFERENCE DATA'
        df=pd.read_csv('SuperRegion_distance_cost_count.csv')
        names=df['Super_Region']
        values=df['num_attend_1']
        ylabel='Super_Region'
        xlabel='CONF_number_of_attendees'
        figname='SuperRegion_distance_cost_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)

        df=pd.read_csv('Region_distance_cost_count.csv')
        names=df['Region']
        values=df['num_attend_1']
        ylabel='Region'
        xlabel='CONF_number_of_attendees'
        figname='Region_distance_cost_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)

        df=pd.read_csv('Domain_distance_cost_count.csv')
        names=df['Domain']
        values=df['num_attend_1']
        ylabel='Domain'
        xlabel='CONF_number_of_attendees'
        figname='Domain_distance_cost_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)

        values=df['Mean_att_per_event']
        ylabel='Domain'
        xlabel='CONF_Avg Event Attendance by Domain'
        figname='Domain_avg_attend_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)
    #now make Web Plots
    if True:
        title='WEBCAST DATA'
        df=pd.read_csv('WEBSuperRegion_cost_count.csv')
        names=df['Super_Region']
        values=df['num_attend_1']
        ylabel='Super_Region'
        xlabel='WEB_number_of_attendees'
        figname='WEB_SuperRegion_cost_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)

        df=pd.read_csv('WEBRegion_cost_count.csv')
        names=df['Region']
        values=df['num_attend_1']
        ylabel='Region'
        xlabel='WEB_number_of_attendees'
        figname='WEB_Region_cost_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)

        df=pd.read_csv('WEBDomain_cost_count.csv')
        names=df['Domain']
        values=df['num_attend_1']
        ylabel='Domain'
        xlabel='WEB_number_of_attendees'
        figname='WEB_Domain_cost_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)

        values=df['Mean_att_per_event']
        ylabel='Domain'
        xlabel='WEB Avg Event Attendance by Domain'
        figname='WEB_Domain_avg_attend_count.png'
        make_bar_plot(names, values,ylabel,xlabel,title, figname)


    # df=pd.read_csv('Domain_distance_cost_count.csv')
    # df=pd.read_csv('Region_distance_cost_count.csv')
    # df=pd.read_csv('WEBSuperRegion_cost_count.csv')
    # df=pd.read_csv('WEBDomain_cost_count.csv')
    # df=pd.read_csv('WEBRegion_cost_count.csv')
