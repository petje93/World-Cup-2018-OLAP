# -*- coding: utf-8 -*-
"""
--OLAP of Sports Data--
@author: Xesfingis Petros
"""

# IMPORTS #################################
from tkinter import *
from cubes import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import ttk
##########################################
#from cubes import Workspace,Cell,PointCut



# CUBES INITIALIZATION#######################
## WORKSPACE
ws = Workspace()
ws.register_default_store("sql", url="sqlite:///world_cup.sqlite")
ws.import_model("world_cup_model.json")

## BROWSER
browser = ws.browser("players")
##################################################

'''
global CLUB_LIST
CLUB_LIST = ['None','Club Atletico Boca Juniors','Club Atletico Independiente','Club Atletico River Plate','Melbourne City FC','Newcastle United Jets','Western Sydney Wanderers',
             'Red Bull Salzburg' ,'Cercle Brugge','Club Brugge KV','KAA Gent','KAS Eupen','KRC Genk','KSC Lokeren','KV Oostende','RSC Anderlecht','Standard Liege','Waasland-Beveren',
             'Club de Regatas Vasco da Gama','Clube de Regatas do Flamengo','Cruzeiro Esporte Clube','Gremio Foot-Ball Porto Alegrense','Sao Paulo Futebol Clube','Sociedade Esportiva Palmeiras',
             'Sport Club Corinthians Paulista','Levski Sofia','PFK Ludogorets Razgrad','Vancouver Whitecaps','Club Universidad de Chile','Huachipato FC','Beijing Sinobo Guoan','Changchun Yatai',
             'Dalian Yifang','Guangzhou Evergrande Taobao','Hebei China Fortune','Tianjin Quanjian','Tianjin Teda','Atletico Bucaramanga','Deportivo Cali','Junior FC','Once Caldas','Rionegro Aguilas',
             'CS Herediano','Deportivo Saprissa','LD Alajuelense','GNK Dinamo Zagreb','HNK Rijeka','Aalborg BK','Brondby IF','FC Copenhagen','FC Nordsjaelland','FC Roskilde','Randers FC',
             'El Ahly Cairo','Zamalek SC','Arsenal FC','Aston Villa','Birmingham City','Brentford FC','Brighton & Hove Albion','Bristol City','Burnley FC','Cardiff City','Chelsea FC',
             'Crystal Palace','Everton FC','Fulham FC','Huddersfield Town','Hull City','Ipswich Town','Leeds United','Leicester City','Liverpool FC','Manchester City','Manchester United',
             'Millwall FC','Nottingham Forest','Queens Park Rangers','Reading FC','Southampton FC','Stoke City','Sunderland AFC','Swansea City','Tottenham Hotspur','Watford FC','West Bromwich Albion',
             'West Ham United','Wigan Athletic','Wolverhampton Wanderers','KuPS','AS Monaco','EA Guingamp','ES Troyes AC','FC Girondins Bordeaux','FC Metz','FC Nantes','FC Toulouse','FCO Dijon','HSC Montpellier',
             'LB Chateauroux','LOSC Lille','OGC Nice','Olympique Lyon','Olympique Marseille','Paris Saint-Germain','SC Amiens','SM Caen','Stade Rennais FC','1. FC Koln','1.FSV Mainz 05','Bayer 04 Leverkusen',
             'Bayern Munich','Borussia Dortmund','Borussia Monchengladbach','Eintracht Frankfurt','FC Augsburg','FC Schalke 04','FC St. Pauli','Fortuna Dusseldorf','Hamburger SV','Hannover 96','Hertha BSC',
             'RB Leipzig','SV Sandhausen','SV Werder Bremen','TSG 1899 Hoffenheim','VfB Stuttgart','VfL Bochum','VfL Wolfsburg','AEK Athens','Atromitos Athens','Olympiacos Piraeus','PAOK Thessaloniki',
             'CSD Municipal','Horoya AC','CD Olimpia','Valur Reykjavik','Esteghlal FC','Padideh Khorasan FC','Persepolis FC','Saipa FC','Zob Ahan Esfahan','Hapoel Beer Sheva','Maccabi Tel Aviv','AC Milan','ACF Fiorentina',
             'AS Roma','Atalanta BC','Bologna FC 1909','FC Crotone','Genoa CFC','Hellas Verona','Inter Milan','Juventus FC','SPAL 2013','SS Lazio','SSC Napoli','Torino FC','UC Sampdoria','Udinese Calcio','Cerezo Osaka',
             'FC Tokyo','Gamba Osaka','Kashima Antlers','Kashiwa Reysol','Kawasaki Frontale','Sagan Tosu','Urawa Red Diamonds','Vissel Kobe','Yokohama F. Marinos','Atlas Guadalajara','CD Cruz Azul','CF America',
             'CF Monterrey','CF Pachuca','Cafetaleros de Tapachula','Deportivo Toluca','Lobos BUAP','Monarcas Morelia','Puebla FC','Tiburones Rojos de Veracruz','Tigres UANL','UNAM Pumas','Ittihad Tanger',
             'Renaissance de Berkane','ADO Den Haag','AZ Alkmaar','Ajax Amsterdam','Feyenoord Rotterdam','PSV Eindhoven','SC Heerenveen','Enyimba Aba','Valerenga Oslo','CD Plaza Amador','San Francisco FC',
             'UD Universitario','Olimpia Asuncion','Sport Boys Callao','Alianza Lima','Deportivo Municipal','FBC Melgar','UTC Cajamarca','Universitario de Deportes','Gornik Zabrze','Lechia Gdansk','Legia Warszawa',
             'CS Maritimo','FC Porto','SL Benfica','Sporting CP','Vitoria Guimaraes SC','Al Gharafa Sports Club','Al Sadd Sports Club','Dinamo Bukarest','Akhmat Grozny','Amkar Perm','Arsenal Tula','CSKA Moscow',
             'FK Krasnodar','FK Rostov','Lokomotiv Moscow','Rubin Kazan','Spartak Moscow','Zenit St. Petersburg','Al-Ahli Jeddah','Al-Batin','Al-Ettifaq','Al-Fateh','Al-Hilal Riyadh','Al-Ittihad','Al-Nasr Riyadh',
             'Al-Raed','Al-Shabab Riyadh','Al-Taawoun','Aberdeen FC','Celtic FC','Hibernian FC','Rangers FC','FK Partizan Belgrade','Red Star Belgrade','DAC Dunajska Streda','Chippa United','Asan Mugunghwa FC',
             'Daegu FC','FC Seoul','Incheon United FC','Jeju United FC','Jeonbuk Hyundai Motors FC','Sangju Sangmu FC','Seongnam FC','Suwon Samsung Bluewings FC','Ulsan Hyundai','Athletic Bilbao','Atletico Madrid',
             'CD Leganes','CD Numancia','Celta de Vigo','Deportivo Alaves','Deportivo de La Coruna','FC Barcelona','Getafe CF','Girona FC','Levante UD','Malaga CF','RC Deportivo Fabril','RCD Espanyol Barcelona',
             'Real Betis Balompie','Real Madrid','Real Sociedad','SD Eibar','Sevilla FC','UD Las Palmas','Valencia CF','Villarreal CF','IFK Norrkoping','Malmo FF','Ostersunds FK','FC Basel 1893','FC Lausanne-Sport',
             'FC Luzern','Grasshopper Club Zurich','Club Africain Tunis','Club Sportif Sfaxien','Esperance Tunis','Etoile Sportive du Sahel','Alanyaspor','Antalyaspor','Basaksehir','Besiktas JK','Bursaspor',
             'Fenerbahce SK','Galatasaray SK','Goztepe','Kardemir Karabukspor','Kasimpasa','Trabzonspor','Yeni Malatyaspor','Dynamo Kyiv','Shakhtar Donetsk','Al-Ain FC','Al-Jazira (Abu Dhabi)','Houston Dynamo',
             'Los Angeles FC','Los Angeles Galaxy','Minnesota United FC','New York City FC','New York Red Bulls','Orlando City SC','Portland Timbers','San Jose Earthquakes','Seattle Sounders FC','CA Penarol']
'''


'''
Changing Active Frame of GUI
'''
###############################################################################
def raise_frame(frame):
    frame.tkraise()
###############################################################################


'''
Deletes everything from Listbox
'''
###############################################################################
def clear():
    listbox.delete('0','end')    
###############################################################################    


'''
Prepare Values for plotting
'''
###############################################################################
def prepare(sizes,labels):
     
    ### REMOVING ZEROS          
    k=0                  
    while k<len(labels):
        if sizes[k]==0:
            sizes.pop(k)
            labels.pop(k)
        else:
            k += 1    
    
    ### SORT RESULTS
    tuples = sorted(zip(sizes, labels))
    sizes, labels = [t[0] for t in tuples], [t[1] for t in tuples]
    sizes, labels = sizes[::-1], labels[::-1]
        
    ### UNIFY AS "OTHERS" THOSE < 3%
    i = 0
    flag=1
    total=0
    while i < len(sizes):
        if (sizes[i]/sum(sizes))>0.03:
            i +=1
        else:
            if flag:
                cut_point=i
                flag=0
            total += sizes[i]
            i +=1
    
    if flag==0:
        sizes = sizes[0:cut_point]    
        sizes.append(total)
        labels = labels[0:cut_point]
        labels.append('Others')

    return sizes,labels
###############################################################################    


'''
Creates plots (Pie, Barchart, Boxplot)
'''
###############################################################################
def plot():
    global img_pie

    
    ### READ VARIABLES
    dr = drill_var.get()
    a = drilldown_define()
    b = cell_define()
    plot_type=plt_var.get()

    if plot_type=="Stats Table":
        stats_table(b)
        return
    
    aggr = aggr_var.get()
    if aggr== 'Players Count': aggr = 'players'
    elif aggr=='Age': aggr = 'age.age_ex'
    elif aggr=='Matches': aggr = 'matches'
    elif aggr=='Goals': aggr = 'goals'
    elif aggr=='Assists': aggr = 'assists'
    elif aggr=='Yellow Cards': aggr = 'ycards'
    elif aggr=='Red Cards': aggr = 'rcards'
    elif aggr=='Minutes': aggr = 'minutes'
    elif aggr=='Total National Caps': aggr = 'n-caps'
    elif aggr=='Total National Goals': aggr = 'n-goals'   
    
    
    ### LABELS AND SIZES TO APPEAR IN PLOT 
    if a!=None:
        result = browser.aggregate(cell=b,drilldown=a)
 
        sizes=[]
        labels=[]
        for record in result:
            sizes.append(record[aggr])
            if dr=='National Team': labels.append(record["nat_team"])
            elif dr=='League': labels.append(record["team.league"])
            elif dr=='Club': labels.append(record["team.club"])
            elif dr=='Age Group': labels.append(record["age.age_gr"])
            elif dr=='Exact Age': labels.append(record["age.age_ex"])        
            elif dr=='Position': labels.append(record["position.pos"])
            elif dr=='Role': labels.append(record["position.role"]) 
    
        boxplot_sizes=sizes    
        sizes,labels=prepare(sizes,labels)
        
    else:
        result = browser.facts(cell=b)
        boxplot_sizes=[]
        for record in result:
            if aggr == 'age.age_ex':
                boxplot_sizes.append(int(record[aggr]))
            else:
                boxplot_sizes.append(record[aggr])             
   

    ### CREATE PLOT
    fig = plt.figure()
    fig.patch.set_facecolor('darkgreen')
             
    if plot_type=='Pie':   
        plt.pie(sizes, labels=labels,autopct='%1.1f%%',
                shadow=True, startangle=0) 
        plt.axis('equal')
    elif plot_type=='Bar Chart':

        short_labels=[]
        for label in labels:
            short_labels.append(label[:8])
            
        y_pos = np.arange(len(short_labels))
        plt.barh(y_pos,sizes)
        plt.yticks(y_pos, short_labels)
    elif plot_type=='Boxplot':
        plt.boxplot(boxplot_sizes)         
    
    plt.savefig('pie.png', facecolor=fig.get_facecolor())
    plt.show()
    img_pie = PhotoImage(file="pie.png")

    panel_pie.config(image=img_pie)
 
###############################################################################    


'''
Creates the Stats Table
'''
###############################################################################
def stats_table(cell):
    
    global img_pie
    
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('darkgreen')    
    ax.axis('off')
    
    rows=['Goals','Assists','Caps','Minutes','Yellow Cards','Red Cards']
    columns=['Total','Max','Average']
    colors=[['skyblue','skyblue','skyblue'],
            ['cyan','cyan','cyan'],
            ['c','c','c'],['turquoise','turquoise','turquoise'],
            ['aquamarine','aquamarine','aquamarine'],
            ['paleturquoise','paleturquoise','paleturquoise']]
    
    result = browser.aggregate(cell=cell)
    
    df = pd.DataFrame(np.random.randn(6, 3))
    
    df.values[0,0]=result.summary["Total Goals"]
    df.values[0,1]=result.summary["Max Goals"]
    df.values[0,2]=result.summary["Average Goals"]
    df.values[1,0]=result.summary["Total Assists"]
    df.values[1,1]=result.summary["Max Assists"]
    df.values[1,2]=result.summary["Average Assists"]
    df.values[2,0]=result.summary["Total Caps"]
    df.values[2,1]=result.summary["Max Caps"]
    df.values[2,2]=result.summary["Average Caps"]
    df.values[3,0]=result.summary["Total Minutes"]
    df.values[3,1]=result.summary["Max Minutes"]
    df.values[3,2]=result.summary["Average Minutes"]
    df.values[4,0]=result.summary["Total Yellow Cards"]
    df.values[4,1]=result.summary["Max Yellow Cards"]
    df.values[4,2]=result.summary["Average Yellow Cards"]
    df.values[5,0]=result.summary["Total Red Cards"]
    df.values[5,1]=result.summary["Max Red Cards"]
    df.values[5,2]=result.summary["Average Red Cards"]
    
    ax.table(cellText=df.values,
                          rowLabels=rows,
                          rowColours=['whitesmoke' for x in rows],
                          colColours=['whitesmoke' for x in columns],
                          cellColours=colors,
                          colLabels=columns,
                          colWidths=[0.25 for x in columns],
                          loc='center',
                          bbox=[0.2, 0, 0.7, 0.7])
                              #[left, bottom, width, height]

    fig.tight_layout()
    
    plt.savefig('pie.png', facecolor=fig.get_facecolor())
    plt.show()
    img_pie = PhotoImage(file="pie.png")

    panel_pie.config(image=img_pie)
    
###############################################################################    


'''
Produce the result of Aggregation
'''
###############################################################################
def aggregate(event):
    
    dr = drill_var.get()
    a = drilldown_define()
    b = cell_define()
    c = aggr_define()
    
    result = browser.aggregate(cell=b,drilldown=a,aggregates=c)
        
    if a==None:
        print(result.summary)
        listbox.insert(END, result.summary)
        plt_var.set(OPTIONS_PLOT[1])
        plot()
        label_title.config(text="\n Results ",font=40,fg='white')
    else:        
        print("\n Drilldown by " + dr +" \n")
        listbox.insert(END, "\n Drilldown by " + dr +" \n")

        for record in result:
            print(record)
            listbox.insert(END, record)
        
        plot()
        label_title.config(text="\n Drilldown by " + dr +" \n",
                           font=40,fg='white')
    
    raise_frame(Frame2)
    
###############################################################################


'''
Print the facts included in the cell
'''
###############################################################################
def facts(event):
    
    a = cell_define()
    result = browser.facts(cell=a)
    
    print("\n Players List: \n")
    listbox.insert(END,"\n")
    listbox.insert(END,"\n Players List: \n")
    
    rec_count=0
    for record in result:
        print(record["__fact_key__"],record["name"])
        rec=str(record["__fact_key__"])+", "+record["name"]
        listbox.insert(END, rec)
        rec_count +=1

    if rec_count==0: 
        print("No player meets the criteria")
        listbox.insert(END, "No player meets the criteria")
    
    drill_var.set(OPTIONS_DRILL[0])    
    plt_var.set(OPTIONS_PLOT[1])
    plot()
    label_title.config(text="\n Players List ",font=40,fg='white')
    raise_frame(Frame2)
          
###############################################################################


'''
Return top X percent for every player in cell
'''
###############################################################################
def top_percent(sizes):
    
    perc=[]
    i=0
    while i < len(sizes):
        j=i+1
        count=0   
        while j < len(sizes):
            if sizes[j] == sizes[i]:
                count+=1
                j+=1
            else: break
        percentage=round(((i+1+count)/len(sizes))*100,3)
        perc.append(percentage)       
        i+=1
         
    return perc
         
###############################################################################


'''
Sort the players in cells according to measure
'''
###############################################################################
def sort():
     
    aggr = sort_var.get()
    if aggr=='Age': val = 'age.age_ex'
    elif aggr=='Matches': val = 'matches'
    elif aggr=='Goals': val = 'goals'
    elif aggr=='Assists': val = 'assists'
    elif aggr=='Yellow Cards': val = 'ycards'
    elif aggr=='Red Cards': val = 'rcards'
    elif aggr=='Minutes': val = 'minutes'
    elif aggr=='Total National Caps': val = 'n-caps'
    elif aggr=='Total National Goals': val = 'n-goals' 
    
    names=[]
    values=[]
    keys=[]
    
    a = cell_define()
    result = browser.facts(cell=a) 
    
    for record in result:
        names.append(record["name"])
        values.append(record[val])
        keys.append(record["__fact_key__"])
   
    ### SORT RESULTS
    tuples = sorted(zip(values, names, keys))
    values, names, keys = [t[0] for t in tuples],[t[1] for t in tuples],[t[2] for t in tuples] 

    if val != "age.age_ex" :
        values, names, keys = values[::-1], names[::-1], keys[::-1]

    top=top_percent(values)

    i=0
    spaces=[]
    while i<len(values):
        if len(str(keys[i])) == 1: spaces.append("      ")
        elif len(str(keys[i])) == 2: spaces.append("    ")
        elif len(str(keys[i])) == 3: spaces.append("  ")
        i+=1

    i=0
    listbox.insert(END, "\n")
    listbox.insert(END, "\n Sorted Players List:")
    while i<len(values):
        rec=str(keys[i])+","+spaces[i]+str(i+1)+". "+names[i]+", "+aggr+": "+str(values[i])+", Top "+str(top[i])+"%"
        print(rec)
        listbox.insert(END, rec)
        i+=1
              
###############################################################################


'''
Choose Dimension for Drilldown
'''
###############################################################################
def drilldown_define():
    
    dr = drill_var.get()

    
    if dr=='National Team':
        a=["nat_team"]
    elif dr=='League':
        a=["team"]
    elif dr=='Club':
        a=[("team","default","club")]
    elif dr=='Age Group':
        a=["age"]
    elif dr=='Exact Age':
        a=[("age","default","age_ex")]        
    elif dr=='Position':
        a=["position"]
    elif dr=='Role':
        a=[("position","default","role")]  
    elif dr=='None':
        a=None 
        
    return a
###############################################################################


'''
Define the cell of the cube
'''
###############################################################################
def cell_define():
    
    cut=[]
    
    nateam = nateam_var.get()
    if nateam!='None':
        a=PointCut("nat_team",[nateam]) 
        cut.append(a)
            
    league = league_var.get()
    if league!='None':
        b=PointCut("team",[league]) 
        cut.append(b)

    club = club_var.get()
    if club!='None' and club!='Choose League First':
        g=PointCut("team",[league,club]) 
        cut.append(g)

    agroup = agroup_var.get()
    if agroup!='None':
        c=PointCut("age",[agroup]) 
        cut.append(c)

    age = age_var.get()
    if age!='None':
        d=PointCut("age",[age],hierarchy="only_age")
        cut.append(d)

    pos = pos_var.get()
    if pos!='None':
        e=PointCut("position",[pos]) 
        cut.append(e)

    role = role_var.get()
    if role!='None':
        f=PointCut("position",[role],hierarchy="only_role") 
        cut.append(f)    
        
    custom_age1 = Ent1.get()
    custom_age2 = Ent2.get()
    if custom_age1!='' or custom_age2!='':
        if len(custom_age1)==1: custom_age1= '0'+custom_age1
        if len(custom_age2)==1: custom_age2= '0'+custom_age2
        if custom_age1=='':custom_age1='15'
        if custom_age2=='':custom_age2='45'
        f=RangeCut("age",[custom_age1],[custom_age2],hierarchy="only_age") 
        cut.append(f)
    
    cell = Cell(browser.cube,cut)
    return cell
###############################################################################    

 
'''
choose aggregates to include in result
'''
###############################################################################
def aggr_define():
    
    aggrs=[]
    
    goals = var_goals.get()
    if goals==1:
        aggrs.append("Total Goals")
            
    assists = var_assists.get()
    if assists==1:
        aggrs.append("Total Assists")

    caps = var_caps.get()
    if caps==1:
        aggrs.append("Total Caps")
            
    mins = var_minutes.get()
    if mins==1:
        aggrs.append("Total Minutes")
    '''
    maxmins = var_maxmins.get()
    if maxmins==1:
        aggrs.append("Max Minutes")
            
    maxgoals = var_maxgoals.get()
    if maxgoals==1:
        aggrs.append("Max Goals")
    '''
    ycards = var_ycards.get()
    if ycards==1:
        aggrs.append("Total Yellow Cards")

    rcards = var_rcards.get()
    if rcards==1:
        aggrs.append("Total Red Cards")

    sc_count = var_sc_count.get()
    if sc_count==1:
        aggrs.append("Scored at least one")

    pl_count = var_pl_count.get()
    if pl_count==1:
        aggrs.append("Played at least one")

    ga_count = var_ga_count.get()
    if ga_count==1:
        aggrs.append("Scored and gave assists")

    count = var_count.get()
    if count==1:
        aggrs.append("players")
        
    return aggrs
############################################################################### 


'''
Configure options for Role Combobox 
'''
###############################################################################
def position_callback(*args):
    
    global OPTIONS_ROLE
    p = pos_var.get()
    role_var.set('None')
    
    if p=='GK':
        OPTIONS_ROLE = ['None','Goalkeeper']
    elif p=='DF':
        OPTIONS_ROLE = ['None','Centre-Back','Left-Back','Right-Back']
    elif p=='MF':
        OPTIONS_ROLE = ['None','Attacking Midfield','Central Midfield',
                        'Defensive Midfield','Left Midfield','Right Midfield']
    elif p=='FW':
        OPTIONS_ROLE = ['None','Centre-Forward','Left Winger',
                        'Right Winger','Second Striker']
    else:
        OPTIONS_ROLE = ['None','Centre-Back','Left-Back','Right-Back',
                        'Centre-Forward','Left Winger','Right Winger',
                        'Second Striker','Goalkeeper','Attacking Midfield',
                        'Central Midfield','Defensive Midfield',
                        'Left Midfield','Right Midfield']
        
    w6.config(values=OPTIONS_ROLE)

    return
###############################################################################


'''
Configure options for Age Combobox 
'''   
###############################################################################
def age_callback(*args):

    global OPTIONS_AGE
    a = agroup_var.get()
    age_var.set('None')
    
    if a=='15-20':
        OPTIONS_AGE = ['None','19','20']
    elif a=='21-25':
        OPTIONS_AGE = ['None','21','22','23','24','25']
    elif a=='26-30':
        OPTIONS_AGE = ['None','26','27','28','29','30']
    elif a=='31-35':
        OPTIONS_AGE = ['None','31','32','33','34','35']
    elif a=='36+':
        OPTIONS_AGE = ['None','36','37','38','39','45']
    else:
        OPTIONS_AGE = ['None','19','20','21','22','23','24','25','26','27',
                       '28','29','30','31','32','33','34','35','36','37',
                       '38','39','45']
        
    w7.config(values=OPTIONS_AGE)

    return
###############################################################################


'''
Configure options for Club Combobox 
'''
###############################################################################
def league_callback(*args):

    global OPTIONS_CLUB
    x = league_var.get()
    club_var.set('None')
    
    if x=='Argentina': OPTIONS_CLUB = ['None','Club Atletico Boca Juniors','Club Atletico Independiente','Club Atletico River Plate']
    elif x=='Australia': OPTIONS_CLUB = ['None','Melbourne City FC','Newcastle United Jets','Western Sydney Wanderers']
    elif x=='Austria': OPTIONS_CLUB = ['None','Red Bull Salzburg']    
    elif x=='Belgium': OPTIONS_CLUB = ['None','Cercle Brugge','Club Brugge KV','KAA Gent','KAS Eupen','KRC Genk','KSC Lokeren','KV Oostende','RSC Anderlecht','Standard Liege','Waasland-Beveren']
    elif x=='Brazil': OPTIONS_CLUB = ['None','Club de Regatas Vasco da Gama','Clube de Regatas do Flamengo','Cruzeiro Esporte Clube','Gremio Foot-Ball Porto Alegrense','Sao Paulo Futebol Clube','Sociedade Esportiva Palmeiras','Sport Club Corinthians Paulista']
    elif x=='Bulgaria': OPTIONS_CLUB = ['None','Levski Sofia','PFK Ludogorets Razgrad']    
    elif x=='Canada': OPTIONS_CLUB = ['None','Vancouver Whitecaps']    
    elif x=='Chile': OPTIONS_CLUB = ['None','Club Universidad de Chile','Huachipato FC']    
    elif x=='China': OPTIONS_CLUB = ['None','Beijing Sinobo Guoan','Changchun Yatai','Dalian Yifang','Guangzhou Evergrande Taobao','Hebei China Fortune','Tianjin Quanjian','Tianjin Teda']    
    elif x=='Colombia': OPTIONS_CLUB = ['None','Atletico Bucaramanga','Deportivo Cali','Junior FC','Once Caldas','Rionegro Aguilas']
    elif x=='Costa Rica': OPTIONS_CLUB = ['None','CS Herediano','Deportivo Saprissa','LD Alajuelense']
    elif x=='Croatia': OPTIONS_CLUB = ['None','GNK Dinamo Zagreb','HNK Rijeka']
    elif x=='Denmark': OPTIONS_CLUB = ['None','Aalborg BK','Brondby IF','FC Copenhagen','FC Nordsjaelland','FC Roskilde','Randers FC']
    elif x=='Egypt': OPTIONS_CLUB = ['None','El Ahly Cairo','Zamalek SC']
    elif x=='England': OPTIONS_CLUB = ['None','Arsenal FC','Aston Villa','Birmingham City','Brentford FC','Brighton & Hove Albion','Bristol City','Burnley FC','Cardiff City','Chelsea FC','Crystal Palace','Everton FC','Fulham FC','Huddersfield Town','Hull City',
                                       'Ipswich Town','Leeds United','Leicester City','Liverpool FC','Manchester City','Manchester United','Millwall FC','Nottingham Forest','Queens Park Rangers','Reading FC','Southampton FC','Stoke City',
                                       'Sunderland AFC','Swansea City','Tottenham Hotspur','Watford FC','West Bromwich Albion','West Ham United','Wigan Athletic','Wolverhampton Wanderers']
    elif x=='Finland': OPTIONS_CLUB = ['None','KuPS']    
    elif x=='France': OPTIONS_CLUB = ['None','AS Monaco','EA Guingamp','ES Troyes AC','FC Girondins Bordeaux','FC Metz','FC Nantes','FC Toulouse','FCO Dijon','HSC Montpellier','LB Chateauroux','LOSC Lille','OGC Nice','Olympique Lyon',
                                      'Olympique Marseille','Paris Saint-Germain','SC Amiens','SM Caen','Stade Rennais FC']
    elif x=='Germany': OPTIONS_CLUB = ['None','1. FC Koln','1.FSV Mainz 05','Bayer 04 Leverkusen','Bayern Munich','Borussia Dortmund','Borussia Monchengladbach','Eintracht Frankfurt','FC Augsburg','FC Schalke 04','FC St. Pauli',
                                       'Fortuna Dusseldorf','Hamburger SV','Hannover 96','Hertha BSC','RB Leipzig','SV Sandhausen','SV Werder Bremen','TSG 1899 Hoffenheim','VfB Stuttgart','VfL Bochum','VfL Wolfsburg']
    elif x=='Greece': OPTIONS_CLUB = ['None','AEK Athens','Atromitos Athens','Olympiacos Piraeus','PAOK Thessaloniki']    
    elif x=='Guatemala': OPTIONS_CLUB = ['None','CSD Municipal']    
    elif x=='Guinea': OPTIONS_CLUB = ['None','Horoya AC']    
    elif x=='Honduras': OPTIONS_CLUB = ['None','CD Olimpia']    
    elif x=='Iceland': OPTIONS_CLUB = ['None','Valur Reykjavik']
    elif x=='Iran': OPTIONS_CLUB = ['None','Esteghlal FC','Padideh Khorasan FC','Persepolis FC','Saipa FC','Zob Ahan Esfahan']
    elif x=='Israel': OPTIONS_CLUB = ['None','Hapoel Beer Sheva','Maccabi Tel Aviv']    
    elif x=='Italy': OPTIONS_CLUB = ['None','AC Milan','ACF Fiorentina','AS Roma','Atalanta BC','Bologna FC 1909','FC Crotone','Genoa CFC','Hellas Verona','Inter Milan','Juventus FC','SPAL 2013','SS Lazio','SSC Napoli','Torino FC','UC Sampdoria','Udinese Calcio']    
    elif x=='Japan': OPTIONS_CLUB = ['None','Cerezo Osaka','FC Tokyo','Gamba Osaka','Kashima Antlers','Kashiwa Reysol','Kawasaki Frontale','Sagan Tosu','Urawa Red Diamonds','Vissel Kobe','Yokohama F. Marinos']
    elif x=='Mexico': OPTIONS_CLUB = ['None','Atlas Guadalajara','CD Cruz Azul','CF America','CF Monterrey','CF Pachuca','Cafetaleros de Tapachula','Deportivo Toluca','Lobos BUAP','Monarcas Morelia','Puebla FC','Tiburones Rojos de Veracruz','Tigres UANL','UNAM Pumas']
    elif x=='Morocco': OPTIONS_CLUB = ['None','Ittihad Tanger','Renaissance de Berkane']
    elif x=='Netherlands': OPTIONS_CLUB = ['None','ADO Den Haag','AZ Alkmaar','Ajax Amsterdam','Feyenoord Rotterdam','PSV Eindhoven','SC Heerenveen']    
    elif x=='Nigeria': OPTIONS_CLUB = ['None','Enyimba Aba']
    elif x=='Norway': OPTIONS_CLUB = ['None','Valerenga Oslo']    
    elif x=='Panama': OPTIONS_CLUB = ['None','CD Plaza Amador','San Francisco FC','UD Universitario']
    elif x=='Paraguay': OPTIONS_CLUB = ['None','Olimpia Asuncion']    
    elif x=='Peru': OPTIONS_CLUB = ['None','Sport Boys Callao','Alianza Lima','Deportivo Municipal','FBC Melgar','UTC Cajamarca','Universitario de Deportes']
    elif x=='Poland': OPTIONS_CLUB = ['None','Gornik Zabrze','Lechia Gdansk','Legia Warszawa']
    elif x=='Portugal': OPTIONS_CLUB = ['None','CS Maritimo','FC Porto','SL Benfica','Sporting CP','Vitoria Guimaraes SC']
    elif x=='Qatar': OPTIONS_CLUB = ['None','Al Gharafa Sports Club','Al Sadd Sports Club']    
    elif x=='Romania': OPTIONS_CLUB = ['None','Dinamo Bukarest']    
    elif x=='Russia': OPTIONS_CLUB = ['None','Akhmat Grozny','Amkar Perm','Arsenal Tula','CSKA Moscow','FK Krasnodar','FK Rostov','Lokomotiv Moscow','Rubin Kazan','Spartak Moscow','Zenit St. Petersburg']
    elif x=='Saudi Arabia': OPTIONS_CLUB = ['None','Al-Ahli Jeddah','Al-Batin','Al-Ettifaq','Al-Fateh','Al-Hilal Riyadh','Al-Ittihad','Al-Nasr Riyadh','Al-Raed','Al-Shabab Riyadh','Al-Taawoun']
    elif x=='Scotland': OPTIONS_CLUB = ['None','Aberdeen FC','Celtic FC','Hibernian FC','Rangers FC']    
    elif x=='Serbia': OPTIONS_CLUB = ['None','FK Partizan Belgrade','Red Star Belgrade']
    elif x=='Slovakia': OPTIONS_CLUB = ['None','DAC Dunajska Streda']    
    elif x=='South Africa': OPTIONS_CLUB = ['None','Chippa United']    
    elif x=='South Korea': OPTIONS_CLUB = ['None','Asan Mugunghwa FC','Daegu FC','FC Seoul','Incheon United FC','Jeju United FC','Jeonbuk Hyundai Motors FC','Sangju Sangmu FC','Seongnam FC','Suwon Samsung Bluewings FC','Ulsan Hyundai']
    elif x=='Spain': OPTIONS_CLUB = ['None','Athletic Bilbao','Atletico Madrid','CD Leganes','CD Numancia','Celta de Vigo','Deportivo Alaves','Deportivo de La Coruna','FC Barcelona','Getafe CF','Girona FC','Levante UD','Malaga CF',
                                     'RC Deportivo Fabril','RCD Espanyol Barcelona','Real Betis Balompie','Real Madrid','Real Sociedad','SD Eibar','Sevilla FC','UD Las Palmas','Valencia CF','Villarreal CF']
    elif x=='Sweden': OPTIONS_CLUB = ['None','IFK Norrkoping','Malmo FF','Ostersunds FK']
    elif x=='Switzerland': OPTIONS_CLUB = ['None','FC Basel 1893','FC Lausanne-Sport','FC Luzern','Grasshopper Club Zurich']
    elif x=='Tunisia': OPTIONS_CLUB = ['None','Club Africain Tunis','Club Sportif Sfaxien','Esperance Tunis','Etoile Sportive du Sahel']                
    elif x=='Turkey': OPTIONS_CLUB = ['None','Alanyaspor','Antalyaspor','Basaksehir','Besiktas JK','Bursaspor','Fenerbahce SK','Galatasaray SK','Goztepe','Kardemir Karabukspor','Kasimpasa','Trabzonspor','Yeni Malatyaspor']    
    elif x=='Ukraine': OPTIONS_CLUB = ['None','Dynamo Kyiv','Shakhtar Donetsk']    
    elif x=='United Arab Emirates': OPTIONS_CLUB = ['None','Al-Ain FC','Al-Jazira (Abu Dhabi)']    
    elif x=='United States': OPTIONS_CLUB = ['None','Houston Dynamo','Los Angeles FC','Los Angeles Galaxy','Minnesota United FC','New York City FC','New York Red Bulls','Orlando City SC','Portland Timbers','San Jose Earthquakes','Seattle Sounders FC']    
    elif x=='Uruguay': OPTIONS_CLUB = ['None','CA Penarol']
    else: OPTIONS_CLUB = ['Choose League First']
        
    w8.config(values=OPTIONS_CLUB)

    return
###############################################################################


'''
Configure Plot Combo-boxes 
'''   
###############################################################################
def plot_boxes_callback(*args):
    global OPTIONS_AGGR,OPTIONS_PLOT
    a = drill_var.get()

    
    if a=='None':
        OPTIONS_PLOT = ['Boxplot','Stats Table']
        OPTIONS_AGGR = ['Age','Matches','Goals','Assists','Minutes',
                        'Yellow Cards','Red Cards','Total National Caps',
                        'Total National Goals']
    else:
        OPTIONS_PLOT = ['Pie','Bar Chart','Boxplot']
        OPTIONS_AGGR = ['Players Count','Total Goals','Total Assists',
                        'Total Caps','Total Minutes','Total Yellow Cards',
                        'Total Red Cards']
    
    w9.config(values=OPTIONS_PLOT)
    w10.config(values=OPTIONS_AGGR)
    plt_var.set(OPTIONS_PLOT[0]) 
    aggr_var.set(OPTIONS_AGGR[0])

    return
##############################################################################
    

'''
Disable choose Aggregate Combobox for Stats Table 
'''   
###############################################################################
def stats_callback(*args):
    global OPTIONS_AGGR
    a = plt_var.get()

    if a=='Stats Table':
        w10.config(state='disabled')
    else:
        w10.config(state='readonly')


    return
##############################################################################


'''
Print details for player selected
'''
###############################################################################
def select_listbox(event):
    w = event.widget
    try:
        idx = int(w.curselection()[0])
    except IndexError:
        return
    
    if w.get(idx)[0]!='{' and w.get(idx)[0]!='\n':
        key=w.get(idx).split(',')[0]

        result = browser.facts()
    
        for record in result:        
            if record["__fact_key__"]==int(key) :
            
                fact=(record["name"]+"\n"+"National Team: "+
                      record["nat_team"]+"\n"+
                   "Club: "+record["team.club"]+"\n"+
                   "League: "+record["team.league"]+"\n"+
                   "Age: "+record["age.age_ex"]+"\n"+
                   "Position: "+record["position.pos"]+"\n"+
                   "Role: "+record["position.role"]+"\n"+"\n"+
                   "Matches: "+str(record["matches"])+"\n"+
                   "Goals: "+str(record["goals"])+"\n"+
                   "Assists: "+str(record["assists"])+"\n"+
                   "Yellow Cards: "+str(record["ycards"])+"\n"+
                   "Red Cards: "+str(record["rcards"])+"\n"+
                   "Minutes: "+str(record["minutes"])+"\n"+"\n"+
                   "Total National Caps: "+str(record["n-caps"])+"\n"+
                   "Total National Goals: "+str(record["n-goals"])+"\n")
                print(fact)
                
                panel_pie.config(text=fact,font=150,fg='white',image='')               
###############################################################################        
    


'''
Graphical User Interface    
'''
###############################################################################
root = Tk()
root.configure(background='dark green')
root.title("World Cup 2018 ~ Analytics")
root.resizable(False, False)


Frame1 = Label(root,bg='dark green')
Frame1.grid(row=0, column=0,rowspan=12,columnspan=5)

Frame2 = Frame(root,bg='dark green')
Frame2.grid(row=0, column=0,rowspan=12,columnspan=5)

raise_frame(Frame1)

# CONFIGURE 12x5 GRID FOR FRAME 1#######
rows = 0
while rows < 12:
    Frame1.rowconfigure(rows, weight=0, minsize=52) 
    rows += 1   
cols = 0
while cols < 5: 
    Frame1.columnconfigure(cols,weight=0, minsize=127) 
    cols += 1
##################################################
# CONFIGURE 12x5 GRID FOR FRAME 2######
rows = 0
while rows < 12:
    Frame2.rowconfigure(rows, weight=0, minsize=50) 
    rows += 1   
cols = 0
while cols < 5: 
    Frame2.columnconfigure(cols,weight=0, minsize=151) 
    cols += 1
################################################## 


# FRAME 1 ELEMENTS:
###############################################################################    
###############################################################################

# LOGO ######################################
panel_logo = Label(Frame1)
panel_logo.configure(background='dark green')
panel_logo.grid(row=0,column=0,rowspan=3,columnspan=1,sticky=W)
logo = PhotoImage(file="logo_rus18.png")
panel_logo.config(image=logo) 
############################################

# BUTTONS ##################################
but1 = Button(Frame1, text="Aggregate",fg="black",height = 1, width = 20)
but1.bind("<Button-1>",aggregate)
but1.grid(row=1,column=2,sticky=W)

but2 = Button(Frame1, text="Show Players",fg="black",height = 1, width = 20)
but2.bind("<Button-1>",facts)
but2.grid(row=2,column=2,sticky=W)
###############################################

# DRILLDOWN SELECTION BOX #####################
OPTIONS_DRILL = ['None','National Team','League','Club','Exact Age',
                 'Age Group','Position','Role']

drill_var = StringVar(Frame1)
drill_var.set(OPTIONS_DRILL[0]) ##default to None
drill_var.trace("w",plot_boxes_callback)

w1 = ttk.Combobox(Frame1, textvariable=drill_var, 
                  values=OPTIONS_DRILL, state='readonly',width=20)
w1.grid(row=6,column=2,sticky=W)
##################################################

# NATIONAL TEAM SELECTION BOX ####################
OPTIONS_NATEAM = ['None','Argentina','Australia','Belgium','Brazil','Colombia',
                 'Costa Rica','Croatia','Denmark','Egypt','England','France',
                 'Germany','Iceland','Iran','Japan','Mexico','Morocco',
                 'Nigeria','Panama','Peru','Poland','Portugal','Russia',
                 'Saudi Arabia','Senegal','Serbia','South Korea','Spain',
                 'Sweden','Switzerland','Tunisia','Uruguay']

nateam_var = StringVar(Frame1)
nateam_var.set(OPTIONS_NATEAM[0]) ##default to None

w2 = ttk.Combobox(Frame1, textvariable=nateam_var, 
                  values=OPTIONS_NATEAM, state='readonly',width=20)
w2.grid(row=7,column=2,sticky=W)
################################################

# LEAGUE SELECTION BOX #########################
OPTIONS_LEAGUE = ['None','Argentina','Australia','Austria','Belgium','Brazil',
                  'Bulgaria','Canada','Chile','China','Colombia','Costa Rica',
                  'Croatia','Denmark','Egypt','England','Finland','France',
                  'Germany','Greece','Guatemala','Guinea','Honduras','Iceland',
                  'Iran','Israel','Italy','Japan','Mexico','Morocco',
                  'Netherlands','Nigeria','Norway','Panama','Paraguay','Peru',
                  'Poland','Portugal','Qatar','Romania','Russia',
                  'Saudi Arabia','Scotland','Serbia','Slovakia','South Africa',
                  'South Korea','Spain','Sweden','Switzerland','Tunisia',
                  'Turkey','Ukraine','United Arab Emirates','United States',
                  'Uruguay']

league_var = StringVar(Frame1)
league_var.set(OPTIONS_LEAGUE[0]) ##default to None
league_var.trace("w",league_callback)

w3 = ttk.Combobox(Frame1, textvariable=league_var, 
                  values=OPTIONS_LEAGUE, state='readonly',width=20)
w3.grid(row=8,column=2,sticky=W)
################################################

# POSITION SELECTION BOX #######################
OPTIONS_POS = ['None','DF','FW','GK','MF']

pos_var = StringVar(Frame1)
pos_var.set(OPTIONS_POS[0]) ##default to None
pos_var.trace("w",position_callback)

w4 = ttk.Combobox(Frame1, textvariable=pos_var, 
                  values=OPTIONS_POS, state='readonly',width=20)
w4.grid(row=9,column=2,sticky=W)
################################################

# AGE GROUP SELECTION BOX ######################
OPTIONS_AGROUP = ['None','15-20','21-25','26-30','31-35','36+']

agroup_var = StringVar(Frame1)
agroup_var.set(OPTIONS_AGROUP[0]) ##default to None
agroup_var.trace("w",age_callback)

w5 = ttk.Combobox(Frame1, textvariable=agroup_var, 
                  values=OPTIONS_AGROUP, state='readonly',width=20)
w5.grid(row=10,column=2,sticky=W)
################################################

# ROLE SELECTION BOX ###########################
OPTIONS_ROLE = ['None','Centre-Back','Left-Back','Right-Back','Centre-Forward',
                'Left Winger','Right Winger','Second Striker','Goalkeeper',
                'Attacking Midfield','Central Midfield','Defensive Midfield',
                'Left Midfield','Right Midfield']

role_var = StringVar(Frame1)
role_var.set(OPTIONS_ROLE[0]) ##default to None

w6 = ttk.Combobox(Frame1, textvariable=role_var, 
                  values=OPTIONS_ROLE, state='readonly',width=25)
w6.grid(row=9,column=4,sticky=W)
################################################

# EXACT AGE SELECTION BOX ######################
OPTIONS_AGE = ['None','19','20','21','22','23','24','25','26','27','28','29',
               '30','31','32','33','34','35','36','37','38','39','45']

age_var = StringVar(Frame1)
age_var.set(OPTIONS_AGE[0]) ##default to None

w7 = ttk.Combobox(Frame1, textvariable=age_var, 
                  values=OPTIONS_AGE, state='readonly',width=25)
w7.grid(row=10,column=4,sticky=W)
################################################

# CLUB SELECTION BOX ##########################
OPTIONS_CLUB = ['Choose League First']

club_var = StringVar(Frame1)
club_var.set(OPTIONS_CLUB[0]) ##default

w8 = ttk.Combobox(Frame1, textvariable=club_var, 
                  values=OPTIONS_CLUB, state='readonly',width=25)
w8.grid(row=8,column=4,sticky=W)
################################################

# CHECKBOXES ###############################
var_goals = IntVar(value=1)
Checkbutton(Frame1,text="Total Goals", variable=var_goals,
            background='dark green').grid(row=7,column=0, sticky=W+N)

var_assists = IntVar()
Checkbutton(Frame1, text="Total Assists", variable=var_assists,
            background='dark green').grid(row=7,column=0, sticky=W+S)

var_caps = IntVar()
Checkbutton(Frame1, text="Total Caps", variable=var_caps,
            background='dark green').grid(row=8,column=0, sticky=W+N)

var_minutes = IntVar()
Checkbutton(Frame1, text="Total Minutes", variable=var_minutes,
            background='dark green').grid(row=8,column=0, sticky=W+S)

var_ycards = IntVar()
Checkbutton(Frame1, text="Total Yellow Cards", variable=var_ycards,
            background='dark green').grid(row=9,column=0, sticky=W+N)

var_rcards = IntVar()
Checkbutton(Frame1, text="Total Red Cards", variable=var_rcards,
            background='dark green').grid(row=9,column=0, sticky=W+S)

var_sc_count = IntVar(value=1)
Checkbutton(Frame1, text="Scored at least one", variable=var_sc_count,
            background='dark green').grid(row=10,column=0, sticky=W+N)

var_pl_count = IntVar(value=1)
Checkbutton(Frame1, text="Played at least one", variable=var_pl_count,
            background='dark green').grid(row=10,column=0, sticky=W+S)

var_ga_count = IntVar()
Checkbutton(Frame1, text="Goal & Assist", variable=var_ga_count,
            background='dark green').grid(row=11,column=0, sticky=W+N)

var_count = IntVar(value=1)
Checkbutton(Frame1, text="Players Count", variable=var_count,
            background='dark green').grid(row=11,column=0, sticky=W+S)
####################################################

# ENTRIES ##########################################
Lent = Label(Frame1,text="Custom Age Range",bg='dark green',fg='white')
Lent.grid(row=11,column=1,sticky=E)

Lent1 = Label(Frame1,text="from",bg='dark green',fg='white')
Lent1.grid(row=11,column=2,sticky=W)
Ent1 = Entry(Frame1,width=6)
Ent1.grid(row=11,column=2,sticky=W,padx=34)
Lent2 = Label(Frame1,text="to",bg='dark green',fg='white')
Lent2.grid(row=11,column=2,padx=80,sticky=W)
Ent2 = Entry(Frame1,width=6)
Ent2.grid(row=11,column=2,padx=100,sticky=W)
####################################################

# LABELS ###########################################
L0 = Label(Frame1,text="Choose Aggregates",bg='dark green',fg='white')
L0.grid(row=6,column=0,sticky=W)
L1 = Label(Frame1,text="Drilldown by",bg='dark green',fg='white')
L1.grid(row=6,column=1,sticky=E)
L2 = Label(Frame1,text="Select National Team",bg='dark green',fg='white')
L2.grid(row=7,column=1,sticky=E)
L3 = Label(Frame1,text="Select League",bg='dark green',fg='white')
L3.grid(row=8,column=1,sticky=E)
L4 = Label(Frame1,text="Select Position",bg='dark green',fg='white')
L4.grid(row=9,column=1,sticky=E)
L5 = Label(Frame1,text="Select Age Group",bg='dark green',fg='white')
L5.grid(row=10,column=1,sticky=E)
L6 = Label(Frame1,text="Select Role",bg='dark green',fg='white')
L6.grid(row=9,column=3,sticky=E)
L7 = Label(Frame1,text="Select Age",bg='dark green',fg='white')
L7.grid(row=10,column=3,sticky=E)
L8 = Label(Frame1,text="Select Club",bg='dark green',fg='white')
L8.grid(row=8,column=3,sticky=E)
#######################################################


# FRAME 2 ELEMENTS:
############################################################################### 
###############################################################################

# PLOT TYPE SELECTION BOX ######################
OPTIONS_PLOT = ['Boxplot','Stats Table']
plt_var = StringVar(Frame2)
plt_var.set(OPTIONS_PLOT[0]) ##default
plt_var.trace("w",stats_callback)
w9 = ttk.Combobox(Frame2, textvariable=plt_var, 
                  values=OPTIONS_PLOT, state='readonly',width=25)
w9.grid(row=9,column=1,sticky=W)
################################################

# PLOT AGGREGATE SELECTION BOX ##########################
OPTIONS_AGGR = ['Age','Matches','Goals','Assists','Minutes',
                        'Yellow Cards','Red Cards','Total National Caps',
                        'Total National Goals']
aggr_var = StringVar(Frame2)
aggr_var.set(OPTIONS_AGGR[0]) ##default
w10 = ttk.Combobox(Frame2, textvariable=aggr_var, 
                   values=OPTIONS_AGGR, state='readonly',width=25)
w10.grid(row=10,column=1,sticky=W)
################################################   

# SORTING SELECTION BOX ##########################
sort_var = StringVar(Frame2)
sort_var.set(OPTIONS_AGGR[0]) ##default
w11 = ttk.Combobox(Frame2, textvariable=sort_var, 
                   values=OPTIONS_AGGR, state='readonly',width=14)
w11.grid(row=10,column=3,pady=30,sticky=E)
################################################  


# BUTTONS ######################################
but_plot = Button(Frame2, width=15, text='Plot!', command=plot)
but_plot.grid(row=9, column=2, rowspan=2)

but_clear = Button(Frame2, width=15, text='Clear', command=clear)
but_clear.grid(row=11, column=3, columnspan=3)

but_sort = Button(Frame2, width=15, text='Sort', command=sort)
but_sort.grid(row=10, column=4, pady=30, columnspan=2)

but_back = Button(Frame2, width=15, text='Back', 
                  command=lambda:raise_frame(Frame1))
but_back.grid(row=11, column=0)
################################################

# LABELS #######################################
L9 = Label(Frame2,text="Select Plot Type",bg='dark green',fg='white')
L9.grid(row=9,column=0,sticky=E)
L10 = Label(Frame2,text="Select Aggregate",bg='dark green',fg='white')
L10.grid(row=10,column=0,sticky=E)
L11 = Label(Frame2,text="Sort By",bg='dark green',fg='white')
L11.grid(row=10,column=3,sticky=W)

panel_pie = Label(Frame2)
panel_pie.configure(background='dark green')
panel_pie.grid(row=2,column=0,rowspan=7,columnspan=3)

label_title = Label(Frame2)
label_title.configure(background='dark green')
label_title.grid(row=0,column=0,columnspan=4,sticky=W)
#################################################

# LISTBOX #######################################
scrollver = Scrollbar(Frame2)
scrollver.grid(row=1,column=5,rowspan=9,sticky=W+N+S)
scrollhor = Scrollbar(Frame2,orient=HORIZONTAL)
scrollhor.grid(row=10,column=3,columnspan=2,sticky=E+W+N)

listbox = Listbox(Frame2, yscrollcommand=scrollver.set,
                  xscrollcommand=scrollhor.set)
listbox.grid(row=1,column=3,rowspan=9,columnspan=2,sticky=E+W+S+N)

scrollver.config(command=listbox.yview)
scrollhor.config(command=listbox.xview)

listbox.bind('<<ListboxSelect>>', lambda e: select_listbox(e))
###################################################


root.mainloop()
###############################################################################