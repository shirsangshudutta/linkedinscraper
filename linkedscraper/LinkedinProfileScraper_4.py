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
elementID.submit()

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
    browser.get(link)
    print('Enterd  visited profile')
    Defaults1 = {'Name':'','Current_location':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration':'','updated_on':''}
    ids1 = []
    thisdict = dict.fromkeys(ids1, Defaults1)
    total_height = int(browser.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 50):
     browser.execute_script("window.scrollTo(0, {});".format(i))
    html_soup = BeautifulSoup(browser.page_source,'html.parser')
    name = html_soup.find("h1", {"class": "text-heading-xlarge inline t-24 v-align-middle break-words"})
    if name is not None:
        print(name.text)
    IDs = []
    thisdict['Name']= clean_string(name.text)
    thisdict['link']= clean_string(link)
    thisdict['Current_location']=clean_string(html_soup.find("span",{"class":"text-body-small inline t-black--light break-words"}).text)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    thisdict['updated_on']=datetime.now()
    time.sleep(random.randint(1,5))

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
Defaults1 = {'Name':'','Current_location':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': ''}
Recdict = []
Recdict = dict.fromkeys(ids1, Defaults1)
baselink = browser.current_url.partition('page')[0]
print('@@@@@@@@@@@@@baselink@@@@@@@@@@@@@@@@@@',baselink)
start_time=time.time()

filename = Path('visitedProfiles.txt')

filename.touch(exist_ok=True)
with open('visitedProfiles.txt', 'r') as filehandle:
    visitedProfiles = [current_link.rstrip() for current_link in filehandle.readlines()]
print('length  at start @@visitedProfiles',len(visitedProfiles))
while(page <7):
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
end_time=time.time()
print ('total time spent scraping ',index,'profiles is',end_time-start_time)
print ('@@length of frontier ',len(frontier))
print ('@@length of visitedProfiles now ',len(visitedProfiles))

# if (len(visitedProfiles)>0):
#     with open('visitedProfiles.txt', 'a') as filehandle:
#         filehandle.writelines("%s\n" % link for link in frontier)

#%%
frontier

#%%
index=0
start_time=time.time()
if len(frontier)>0:
    for i in frontier:
        Recdict[index]=visitProfile(i)
        time.sleep(random.randint(1,5))
        index=index+1
visitedProfiles=visitedProfiles+frontier
with open('visitedProfiles.txt', 'a') as filehandle:
    filehandle.writelines("%s\n" % link for link in frontier)             
if  Recdict is not None:
    for x, y in Recdict.items():
        print(x,y)
end_time=time.time() 
print ('@@length of visitedProfiles now after adding frontier ',len(visitedProfiles))
print ('total time spent scraping ',len(frontier),'profiles is',end_time-start_time)

#%%    
link='https://www.linkedin.com/in/koustav-mandal-14b244168/'
Recdict=[]
# browser.get(link)
# download_urls(link)
Recdict=visitProfile(link)
if  Recdict is not None:
    for x, y in Recdict.items():
        print(x,y)         
#%%Convert to  list 
import pandas as pd
values=Recdict.values()
values_list = list(values)
print(values_list,type(values_list))
#%%
df=pd.json_normalize(values_list)
df.to_csv("emp_list_ju_cse_2606.csv")
#%%
scraping_time=end_time-start_time       
print ('total time spent scraping profile',index,'profiles is',scraping_time.seconds)
total_time=(time_frontier+scraping_time).seconds
print('total time spent for ',index,'profiles is',total_time,'seconds')
#%%
import pymysql
import numpy as np
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='times82!',
                             db='linkedin')

cursor = connection.cursor()

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
profile=visitProfile('https://www.linkedin.com/in/shirsangshu-dutta-57a3ab13/')
lst=list(profile.values())
print(lst)
# df = pd.DataFrame(lst)
# print(df)
# df1 = df.replace(np.nan, '', regex=True)
# cols = "`,`".join([str(i) for i in df.columns.tolist()])
# df1

# %% select data into df
import pandas as pd
links=[]
ids1 = []
dataframe = {}
query="select Name,Current_location,Link,College,Degree,Branch,duration,designation,company ,dates_employed ,employ_duration ,updated_on from linkedin.pagesvisited WHERE link=%s"
link='https://www.linkedin.com/in/sourav-barua-248b58103/'
cursor = connection.cursor()
dataframe = pd.read_sql(query,connection,params=[link])
dataframe
# browser.get(link)
# download_urls(link)
#%%
import pandas as pd
IDs = []
Defaults1 = {'Name':'','Current_location':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': '','updated_on':''}
Recdict = []
Recdict = dict.fromkeys(ids1, Defaults1)
link='https://www.linkedin.com/in/sourav-barua-248b58103/'
Recdict=visitProfile(link)
df1 = pd.DataFrame(Recdict,index=[0])
df1
#%%
dataframe.compare(df,keep_equal=True)

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