]# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%

import time
import sys
import random
import os
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen
import urlmatch
from requests import Response
import re
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
file = open('E:\config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
branch=lines[2]
university=lines[3]

print(username)

browser = webdriver.Chrome('E:\\pyhton\\driver\\chromedriver.exe')
browser.get('https://www.linkedin.com/uas/login')

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
time.sleep(random.randint(1, 3))
elementID = browser.find_element_by_id('password')
time.sleep(random.randint(1, 3))
elementID.send_keys(password)


#%% 
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

visitedProfiles = []
profilesQueued = []
profilesID = []


def clean_string(var):
    var = str(var)
    var = var.strip()
    var = var.replace('\n', '')
    return var


def visitProfile(link):
    print(link)
    browser.get(link)
    print('Enterd  visited profile')
    Defaults1 = {'Name':'','Current_location':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration':''}
    ids1 = []
    thisdict = dict.fromkeys(ids1, Defaults1)
    total_height = int(browser.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 50):
     browser.execute_script("window.scrollTo(0, {});".format(i))
    time.sleep(random.randint(1,5))
    html_soup = BeautifulSoup(browser.page_source,'html.parser')
    name = html_soup.find("h1", {"class": "text-heading-xlarge inline t-24 v-align-middle break-words"})
    if name is not None:
        print(name.text)
    IDs = []
    thisdict['Name']= clean_string(name.text)
    thisdict['link']= clean_string(link.partition("?")[0])
    thisdict['current_location']=clean_string(html_soup.find("span",{"class":"text-body-small inline t-black--light break-words"}).text)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # thisdict['updated_on']=datetime.now()

    if (html_soup.find("li", {"class":"pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"})):
        print('section1')
        # edusect=html_soup.find("section", {"class":"pv-profile-section education-section ember-view"})
        try:
            for t in html_soup.find_all("li", {"class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"}):
                print('university',university)
                print('branch',branch)
                if(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("Jadavpur University",re.IGNORECASE))) :
                    print('@@univ')
                    # if (html_soup.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer Science",re.IGNORECASE))) is not None:
                    if (html_soup.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find_all(text=re.compile("Computer",re.IGNORECASE))) is not None:
                        thisdict['college']=t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).text if t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}) else ''
                        thisdict['degree']=t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text if t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}) else ''
                        # thisdict['branch']=clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text) if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer Science",re.IGNORECASE)) else '',
                        thisdict['branch']=clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text) if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer",re.IGNORECASE)) else ''
                        thisdict['duration']=clean_string(t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}) else ''
                # else:
                #     thisdict['college']=''
                #     thisdict['degree']=''
                #     thisdict['branch']=''
                #     thisdict['duration']=''                  
            # for x, y in thisdict.items():
            #     print(x,y)
            # IDs = []
            # Defaults = {}
            # expdict = dict.fromkeys(IDs, Defaults)
            i=0

            if (html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})):
                print("@@@@here@@@@@")
                for k in html_soup.find_all("div",{"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"},limit=2) :
                        print("####there@@@@@")
                        thisdict['designation']= clean_string(k.find("h3",{"class":"t-16 t-black t-bold"}).text) if k.find("h3",{"class":"t-16 t-black t-bold"}) else ''
                        thisdict['company']=clean_string(k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text) if k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}) else ''
                        thisdict['employ_duration'] =clean_string(k.find("span",{"class":"pv-entity__bullet-item-v2"}).text) if k.find("span",{"class":"pv-entity__bullet-item-v2"}) else ''
                        thisdict['dates_employed'] =clean_string(k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}) else ''
                                        # i=i+1                  
                # for x, y in thisdict.items():
                #     print(x,y)  
                # return thisdict                  
        #         else :
        #             thisdict=''

        #             # 'Edu':thisdict,

        # else :
        #         thisdict=''
        
        except  :     
            print("Oops!", sys.exc_info()[0], "occurred.")  
            pass                     
    for x, y in thisdict.items():
                    print(x,y)
    return thisdict 
#%%
from pathlib import Path
from datetime import datetime
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
 
fullLink="https://www.linkedin.com/search/results/all/?keywords=jadavpur%20university%20computer%20science&origin=GLOBAL_SEARCH_HEADER"
browser.get(fullLink)
profilesQueued = []
profilesID = []
visitedProfiles=[]
page = 0
index = 0
limit = 100
ids1 = []
frontier=[]
# Defaults1 = {'Name': '', 'Edu': '', 'Exp': ''}
IDs = []
Defaults1 = {'Name':'','current_location':'','link':'','college': '', 'degree': '', 'branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': ''}
Recdict = []
Recdict = dict.fromkeys(ids1, Defaults1)
baselink = browser.current_url.partition('page')[0]
print('@@@@@@@@@@@@@baselink@@@@@@@@@@@@@@@@@@',baselink)
start_time=datetime.now()

filename = Path('visitedProfiles.txt')

filename.touch(exist_ok=True)
with open('visitedProfiles.txt', 'r') as filehandle:
    visitedProfiles = [current_link.rstrip() for current_link in filehandle.readlines()]
print('length  at start @@visitedProfiles',len(visitedProfiles))
while(page <50):
    if page==0:
        nextlink=baselink
        print('page 0 nextlink:'+nextlink)
    else:    
        page = page + 1
        next_page = ''
        next_page = ('&page='+str(page))
        print('next_page: '+next_page)
        # print('link:'+link)
        nextlink = baselink+next_page
        print('nextlink:'+nextlink)
    browser.get(nextlink)
    time.sleep(random.randint(1,5))
    html_source = BeautifulSoup(browser.page_source, 'html.parser')
    excluded_link="https://www.linkedin.com/search/results/all/headless?keywords=jadavpur%20university%20department%20of%20information%20technology&amp;origin=GLOBAL_SEARCH_HEADER\">"
    match_pattern = 'https://www.linkedin.com/in/*'
    for profile in html_source.find_all("div", {"class": "entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"}):
        if profile is not None:
            linkprofile=""
            visited_set = set()
            for b in profile.find_all("span", {"class": "entity-result__title-text t-16"}):
                f=""
                for f in b.find_all("a",{"class":"app-aware-link"}) :
                    linkprofile = f['href']
                    if urlmatch.urlmatch(match_pattern,linkprofile):
                        print('linkprofile'+linkprofile,index)
                        if (len(visitedProfiles)<1):
                            visitedProfiles.append(linkprofile)
                        else:
                            if (linkprofile  not in visitedProfiles):
                                # visitedProfiles.append(linkprofile)
                                frontier.append(linkprofile)
                        # if len(Recdict[index])>0:
                        index=index+1
            if index is limit:
                print('####limit has reached')
                break
    page = page + 1
    time.sleep(random.randint(1,5))
# for i in profileIds:
#         print(i)        
print('here')
end_time=datetime.now()
time_frontier=end_time-start_time
print ('total time spent creating frontier ',len(frontier),'profiles is',time_frontier.seconds,"seconds")
# print ('@@length of frontier ',len(frontier))
# if (len(visitedProfiles)>0):
#     with open('visitedProfiles.txt', 'a') as filehandle:
#         filehandle.writelines("%s\n" % link for link in frontier)
#%%
frontier

#%%run frontier
index=0
start_time=datetime.now()
if len(frontier)>0:
    for i in frontier:
        Recdict[index]=visitProfile(i)
        time.sleep(random.randint(1,5))
        index=index+1
visitedProfiles=visitedProfiles+frontier
print ('@@length of visitedProfiles now ',len(visitedProfiles))
# with open('visitedProfiles.txt', 'w') as filehandle:
#     filehandle.writelines("%s\n" % link for link in visitedProfiles)
with open('visitedProfiles.txt', 'a') as filehandle:
    filehandle.writelines("%s\n" % link for link in frontier)                
if  Recdict is not None:
    for x, y in Recdict.items():
        print(x,y)     
end_time=datetime.now() 
scraping_time=end_time-start_time       
print ('total time spent scraping profile',index,'profiles is',scraping_time.seconds)
total_time=(time_frontier+scraping_time).seconds
print('total time spent for ',index,'profiles is',total_time,'seconds')
# #%%    
# link='https://www.linkedin.com/in/koustav-mandal-14b244168/'
# Recdict=[]
# # browser.get(link)
# # download_urls(link)
# Recdict=visitProfile(link)
# if  Recdict is not None:
#     for x, y in Recdict.items():
#         print(x,y)         
#%%Convert to  list 
import pandas as pd
values=Recdict.values()
values_list = list(values)
print(values_list,type(values_list))
df=pd.json_normalize(values_list)

#%%save dataframe o excel

df.to_excel("excelfilename.xls")
#%%
# df = pd.read_excel('excelfilename.xls')
df
#%%
import pymysql
import numpy as np
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='times82!',
                             db='linkedin')

cursor = connection.cursor()
#%%
df
#%%
df1 = df.replace(np.nan, '', regex=True)
cols = "`,`".join([str(i) for i in df.columns.tolist()])
df1
for i,row in df1.iterrows():
    sql = "INSERT INTO linkedin.pagesvisited (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    print(sql)
    cursor.execute(sql, tuple(row))
    # the connection is not autocommitted by default, so we must commit to save our changes
sql1 ="INSERT INTO linkedin.stats(date1,visitedprofile,count,time_taken) values(%s,%s,%s,%s)"
data = (datetime.now(),len(visitedProfiles),len(frontier),total_time)
cursor.execute(sql1,data)
connection.commit() 
print(cursor.rowcount, "record(s) onserted")


# %%
import numpy as np
profile=visitProfile('https://www.linkedin.com/in/soham-mukherjee-5b955914b')
# print(lst)
# df = pd.DataFrame.from_dict(profile,orient = 'index')
df_prof=pd.DataFrame(data={k: [v] for k, v in profile.items()})
df_prof1=df_prof[['Name','link','Current_location']]
#%%
df_prof1

# df1 = df.replace(np.nan, '', regex=True)
# cols = "`,`".join([str(i) for i in df.columns.tolist()])
# df1
# %% select data into df
links=[]
ids1 = []
dataframe = {}
# query="select Name,Link,Current_location,updated_on,college,degree,branch,duration,designation,company ,dates_employed ,employ_duration ,updated_on from linkedin.pagesvisited WHERE link=%s"
query="select Name,Link as link,Current_location from linkedin.pagesvisited WHERE link=%s"
link='https://www.linkedin.com/in/soham-mukherjee-5b955914b'

cursor = connection.cursor()
dataframe = pd.read_sql(query,connection,params=[link])
dataframe
# download_urls(link)
# #%%
# import pandas as pd
# IDs = []
# Defaults1 = {'Name':'','Current_location':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': '','updated_on':''}
# Recdict = []
# Recdict = dict.fromkeys(ids1, Defaults1)
# link='https://www.linkedin.com/in/sourav-barua-248b58103/'
# Recdict=visitProfile(link)
# df1 = pd.DataFrame(Recdict,index=[0])
# df1
#%%
eq1=dataframe.eq(df_prof1)
if (eq1.all(axis=None)==False):
    sqldel="delete from linkedin.pagesvisited   where link=%s"
    link='https://www.linkedin.com/in/soham-mukherjee-5b955914b'
    print(sqldel)
    cursor.execute(sqldel,link)
    connection.commit()
    print(cursor.rowcount, "record(s) deleted")
#%%

df_prof2 = df_prof1.replace(np.nan, '', regex=True)
df_prof2
cols = "`,`".join([str(i) for i in df_prof2.columns.tolist()])
for i,row in df_prof2.iterrows():
    sql = "INSERT INTO linkedin.pagesvisited (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    print(sql)
    cursor.execute(sql, tuple(row))
    connection.commit()
    print(cursor.rowcount, "record(s) onserted")
#%%
print(dataframe_t)
# print(df)
#%%

filesFrame = pd.DataFrame(Recdict.items(), columns=['Name','college'])
print(filesFrame)


# %%
#%%

###############Vizualizaions###

dfgrp=df.groupby(['duration']).size().to_frame('count')
type(dfgrp)
dfgrp['count'].plot.bar(x='duration', y='size', rot=0)
dfgrpcmp=df.groupby(['company']).size().to_frame('count')
dfgrpcmp
# dfgrpcmp['count'].plot.bar(x='company', y='size', rot=0)

#sort by no
# x = df.groupby('start_station_name')['duration'].mean().sort_values().tail(15)

# pd.merge(df,dfgrp,on=['duration','B','C'])
# dfgrp.hist(column ='size')
# ax = dfgrp.plot.bar(x='duration', y='size', rot=0)
#%%
x = df.groupby('company').size().to_frame()
type(x)
ax = x.plot(kind='barh', figsize=(8, 10), color='#86bf91', zorder=2, width=0.85)

  # Despine
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_visible(False)

# # Switch off ticks
# ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# # Draw vertical axis lines
# vals = ax.get_xticks()
# for tick in vals:
#     ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

# Set x-axis label
ax.set_xlabel("Number ", labelpad=20, weight='bold', size=12)

# Set y-axis label
ax.set_ylabel("Company", labelpad=20, weight='bold', size=12)

plt.savefig('foo.png')

# Format y-axis label
# ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
#%%
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
text = df['designation'].values 
wordcloud = WordCloud().generate(str(text))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
#%%
import matplotlib.pyplot as plt
df1=df['designation'].str.contains('Research|research', regex=True, na=True)
# df.query('classd.str.contains("research")', engine='python')

df1.value_counts(sort=False).plot( y = 'total_research',kind='pie',autopct='%1.1f%%')
plt.show()


#%%ending here

 #print only values having non null
import bson
recdict1={k:v for k,v in Recdict.items() if  v}
for x, y in recdict1.items():
    print(x,y) 
print (len(Recdict))
# print(Recdict)
#%%
list1=[]
for link in visitedProfiles[:2]:
    profile=visitProfile(link)
    df1 = pd.DataFrame(profile,columns =['Name', 'link']) 
df1     
# df_prof_link1    
# %%
# import pandas as pd
# df_prof_list=pd.DataFrame(list1)
# df_prof_list
# %%
#%%
import pymysql
import numpy as np
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='times82!',
                             db='linkedin')

cursor = connection.cursor()
print(len(visitedProfiles))
#%%
# visitedProfiles1=['https://www.linkedin.com/in/shirsangshu-dutta-57a3ab13/']
import pandas as pd
for link in visitedProfiles[:1]:
    print(link)
    profile=visitProfile(link)
    df_prof=pd.DataFrame(data={k: [v] for k, v in profile.items()})
    # df_prof=df_prof[['Name','current_location']]
    df_prof=df_prof[['Name','current_location']]

    print('###')
    print(df_prof) 
    ids1 = []
    dataframe = {}
    # query="select Name,link,current_location,college ,degree,branch,duration,designation,company ,dates_employed ,employ_duration ,updated_on from linkedin.pagesvisited WHERE link=%s"
    query="select Name,current_location from  linkedin.pagesvisited WHERE link=%s"

    cursor = connection.cursor()
    link=link.partition("?")[0]
    print(link)
    # link='https://www.linkedin.com/in/soham-mukherjee-5b955914b'
    dataframe = pd.read_sql(query,connection,params=[link])
    print('######')
    print(dataframe)
    eq1=dataframe.eq(df_prof)
    print(eq1)
    if (eq1.all(axis=None)==False):
        sqldel="delete from linkedin.pagesvisited   where link=%s"
        # link='https://www.linkedin.com/in/soham-mukherjee-5b955914b'
        print(sqldel)
        cursor.execute(sqldel,link)
        connection.commit()
        print(cursor.rowcount, "record(s) deleted")
        df_prof2 = df_prof.replace(np.nan, '', regex=True)
        df_prof2
        cols = "`,`".join([str(i) for i in df_prof2.columns.tolist()])
        for i,row in df_prof2.iterrows():
            sql = "INSERT INTO linkedin.pagesvisited (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            print(sql)
            cursor.execute(sql, tuple(row))
            connection.commit()
            print(cursor.rowcount, "record(s) onserted")
        sql1 ="INSERT INTO linkedin.stats(date1,visitedprofile,count,time_taken) values(%s,%s,%s,%s)"
        data = (datetime.now(),len(visitedProfiles),len(frontier),total_time)
        cursor.execute(sql1,data)
        connection.commit() 
        print(cursor.rowcount, "record(s) onserted")    
    else:
        print('no changes for',link)
# %%
# %%
# print(eq1)
# df_prof1=df_prof[['Name','link','current_location','updated_on','college ','degree','branch','duration','designation','company' ,'dates_employed' ,'employ_duration' ,'updated_on']]
print(eq1)
# recdict1={k:v for k,v in profile.items()}
# for x, y in recdict1.items():
#     print(x,y) 

# %% data visualizaion2
query="select * from  linkedin.pagesvisited"
df = pd.read_sql(query,connection)
df
# dfgrp=df.groupby(['duration']).size().to_frame('count')
# type(dfgrp)
# dfgrp['count'].plot.bar(x='duration', y='size', rot=0)
# dfgrpcmp=df.groupby(['company']).size().to_frame('count')
# dfgrpcmp

# %%
import matplotlib as plt
x = df.groupby('company').size().reset_index(name='count').sort_values(by=['count'],ascending=False)[:10]
x.plot.barh(x='company',y='count')
# ax1=plt.subplot(1,1,1)
# ax1.barh(x.company,x.count)
# .sort_values(by=['col1'])
# x1=x[['company','count']]
# x2=x1.reset_index(drop=True)
# x2 
# ax = x2.plot(kind='barh', figsize=(8, 10), color='#86bf91', zorder=2, width=0.85)

 # Despine
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_visible(False)

# # Switch off ticks
# ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# # Draw vertical axis lines
# vals = ax.get_xticks()
# for tick in vals:
#     ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

# Set x-axis label
# ax.set_xlabel("Count", labelpad=20, weight='bold', size=12)

# # # Set y-axis label
# ax.set_ylabel("company", labelpad=20, weight='bold', size=12)

# plt.savefig('foo.png')

# %%
import pymysql
import pandas as pd
import numpy as np

import time
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='times82!',
                             db='linkedin')

cursor = connection.cursor()

changed=0
with open('remaining.txt','r') as filehandle:
    remain = [current_link.rstrip() for current_link in filehandle.readlines()]
for link in remain:
    link = link.replace("'", "")
    # link = link.encode('ascii', 'ignore').decode('unicode_escape')
    print(link)
    # time.sleep(2)
    # browser.get(link)
    profile=visitProfile(link)
    df_prof=pd.DataFrame(data={k: [v] for k, v in profile.items()})
#%%   
def SQL_SELECT_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET):
    sql_texts = ''
    # for index, row in SOURCE.iterrows():       
    sql_texts='SELECT  '+ str(', '.join(SOURCE.columns))+ 'FROM linkedin.pagesvisited where link='+'\''+str(link)+'\''   
    return sql_texts

#     
#%%
import pandas as pd   
link='https://www.linkedin.com/in/soham-mukherjee-5b955914b'
profile=visitProfile(link)
df_prof=pd.DataFrame(data={k: [v] for k, v in profile.items()})
#%%
sql=SQL_SELECT_STATEMENT_FROM_DATAFRAME(df_prof,link)
print(sql)
#%%
import time
from datetime import datetime

import pymysql
import numpy as np

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='times82!',
                             db='linkedin')

cursor = connection.cursor()

changed=0
start_time=datetime.now()
with open('remaining.txt','r') as filehandle:
    frontier = [current_link.rstrip() for current_link in filehandle.readlines()]
for link in frontier[:1]:
    link = link.replace("'", "")
    # link = link.encode('ascii', 'ignore').decode('unicode_escape')
    link='https://www.linkedin.com/in/shirsangshu-dutta-57a3ab13/'
    # time.sleep(2)
    # browser.get(link)
    profile=visitProfile(link)
    df_prof=pd.DataFrame(data={k: [v] for k, v in profile.items()})
    print('###')
    query='SELECT  '+ str(', '.join(df_prof.columns))+ ' FROM linkedin.pagesvisited where link='+'\''+str(link)+'\''      
    # ids1 = []
    # dataframe = {}
    # query="select Name,link,current_location,college,degree,branch,duration,designation,company ,dates_employed ,employ_duration  from linkedin.pagesvisited WHERE link='%s"
    # # query="select Name,current_location from  linkedin.pagesvisited WHERE link=%s"
    cursor = connection.cursor()
    # link=link.partition("?")[0]
    print(query)
    # dataframe = pd.read_sql(query,connection,params=[link])
    dataframe = pd.read_sql(query,connection)
    print('######')
    print(dataframe)
    eq1=dataframe.eq(df_prof)
    print(eq1)
    if (eq1.all(axis=None)==False):
        changed=changed+1
        sqldel="delete from linkedin.pagesvisited   where link=%s"
        # link='https://www.linkedin.com/in/soham-mukherjee-5b955914b'
        print(sqldel)
        cursor.execute(sqldel,link)
        connection.commit()
        print(cursor.rowcount, "record(s) deleted")
        df_prof2 = df_prof.replace(np.nan, '', regex=True)
        df_prof2
        cols = "`,`".join([str(i) for i in df_prof2.columns.tolist()])
        for i,row in df_prof2.iterrows():
            sql = "INSERT INTO linkedin.pagesvisited (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            print(sql)
            cursor.execute(sql, tuple(row))
            connection.commit()
            print(cursor.rowcount, "record(s) onserted")
    else:
        print('no changes for',link)
end_time=datetime.now()
total_time=end_time-start_time       
sql1 ="INSERT INTO linkedin.stats(date1,visitedprofile,count,time_taken,changed) values(%s,%s,%s,%s)"
data = (datetime.now(),len(visitedProfiles),null,total_time,changed)
cursor.execute(sql1,data)
connection.commit() 
print(cursor.rowcount, "record(s) onserted")            
# %%
