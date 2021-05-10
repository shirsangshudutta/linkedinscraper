# To add a new cell, type '# %%'
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

# from urllib.parse import urlparse
# from webdriver_manager.chrome import ChromeDriverManager

# from webdriver_manager.chrome import ChromeDriverManager

# browser = webdriver.Chrome(ChromeDriverManager().install())
# import chromedriver_install as cdi
# path = cdi.install(file_directory='c:\\data\\chromedriver\\', verbose=True, chmod=True, overwrite=False, version=None)
# print('Installed chromedriver to path: %s' % path)
# browser = webdriver.Chrome("c:\\data\\chromedriver\\chromedriver.exe")
browser = webdriver.Chrome('E:\\pyhton\\driver\\chromedriver.exe')
# browser = webdriver.Chrome(executable_path='E:\\python\\driver\\chromedriver.exe')

# from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.linkedin.com/uas/login')

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
time.sleep(random.randint(1, 3))
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

#%%
from selenium.webdriver import ActionChains
browser.get("https://www.linkedin.com/in/arjun-murmu-82073b159/")
# identify element
# l=browser.("//*[@id="ember125"]/div[2]/div/h3")
# # action object creation to scroll
# a = ActionChains(driver)
# a.move_to_element(l).perform()

# %%
from selenium.webdriver.common.action_chains import ActionChains

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
    time.sleep(random.randint(1,5))
    print('Enterd  visited profile')
    Defaults1 = {'Name':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': ''}
    ids1 = []
    thisdict = dict.fromkeys(ids1, Defaults1)
    # element = browser.find_elements_by_css_selector('#education-section')
    # actions = ActionChains(browser)
    # actions.move_to_element(element).perform()
    html_soup = BeautifulSoup(browser.page_source,'html.parser')
    print('link',browser.current_url)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # browser.execute_script("window.scrollTo(0,1200)")

    # name = html_soup.find("li", {"class": "inline t-24 t-black t-normal break-words"})
    # print(name.text)
#     SCROLL_PAUSE_TIME=5
# #Get scroll height
#     last_height = browser.execute_script("return document.body.scrollHeight")
#     for i in range(3): 
#     #Scroll down to bottom
#         browser.execute_script("window. scrollTo(0, document.body.scrollHeight);")
#         #Woit to Load page
#         time.sleep(SCROLL_PAUSE_TIME)
#         # Calculate new scroll height and compare with Last seroll height

#         new_height=browser.execute_script("return document.body.scrollHeight;")

#         if new_height==last_height:

#             break

#         last_height = new_height
    # element=browser.find_elements_by_id("ember262")
   
    # test1=html_soup.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"})
    # print(test1)
    # element = browser.find_elements_by_css_selector('#ember140 > div.pv-entity__summary-info.pv-entity__summary-info--background-section > div > h3')
    # browser.execute_script("arguments[0].scrollIntoView();", element)
   
    # if (html_soup.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("Jadavpur University",re.IGNORECASE))) is not None:
    #         print("@@@@edu@@@@")
    #         if (html_soup.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer Science",re.IGNORECASE))) is not None:
    #             print("@@@@comp@@@@")
    name = html_soup.find("li", {"class": "inline t-24 t-black t-normal break-words"})
    if name is not None:
        print(name.text)
    IDs = []
    # Defaults = {'Name':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': ''}
    # thisdict = dict.fromkeys(IDs, Defaults)
    thisdict['Name']= clean_string(name.text)
    # thisdict['Link']= clean_string(link)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # browser.execute_script("window.scrollTo(0,700)")
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
# from selenium.webdriver.common.action_chains import ActionChains
# link='https://www.linkedin.com/in/shanawaz-alam-ju/'
# link='https://www.linkedin.com/in/chandreyee-chowdhury-56244263/'
# link='https://www.linkedin.com/in/arjun-murmu-82073b159/'
# link='https://www.linkedin.com/in/anjali-c-806186158/'

# Recdict=visitProfile(link)
if  Recdict is not None:
    for x, y in Recdict.items():
        print(x,y) 
# browser.find_element()
# elem.send_keys(Keys.ARROW_DOWN)
# for webelem in elem:
#  actions = ActionChains(browser)
#  actions.move_to_element(webelem).perform()
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


# browser.execute_script("arguments[0].scrollIntoView();", element)
#%%
# visitingProfileID = '/in/shirsa-dutta-8301241a3/'
# fullLink = 'https://www.linkedin.com' + visitingProfileID
fullLink="https://www.linkedin.com/search/results/all/?keywords=jadavpur%20university%20computer%20science&origin=GLOBAL_SEARCH_HEADER"
browser.get(fullLink)
# que = browser.find_element_by_xpath('//*[@id="ember20"]/input')
# print(que)
# que.send_keys("jadavpur university computer science")
# que.send_keys(Keys.ENTER)

 # %%
# que = browser.find_element_by_xpath('//*[@id="ember20"]/input')
# print(que)
# que.send_keys("jadavpur university department of information technology")
# que.send_keys(Keys.ENTER)
profilesQueued = []
profilesID = []
page = 0
index = 0
limit = 100
ids1 = []
# Defaults1 = {'Name': '', 'Edu': '', 'Exp': ''}
IDs = []
Defaults1 = {'Name':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': ''}
Recdict = []
Recdict = dict.fromkeys(ids1, Defaults1)
baselink = browser.current_url.partition('page')[0]
print('@@@@@@@@@@@@@baselink@@@@@@@@@@@@@@@@@@',baselink)
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
            # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&77')
            for b in profile.find_all("span", {"class": "entity-result__title-text t-16"}):
                # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&66')
                f=""
                for f in b.find_all("a",{"class":"app-aware-link"}) :
                    # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&55')
                    # print(f)
                    # if re.match(f['href'] ,"https:\/\/www.linkedin.com\/in\/\*") :
                    linkprofile = f['href']
                    # linkprofile="https://www.linkedin.com/in/shanawaz-alam-ju/"
                    if urlmatch.urlmatch(match_pattern,linkprofile):
                        print('linkprofile'+linkprofile,index)
                    # profileIds=getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
                        Recdict[index]=visitProfile(linkprofile)
                        visitedProfiles=linkprofile
                        if len(Recdict[index])>0:
                         index=index+1
            if index is limit:
                print('####limit has reached')
                break
        #     if f is not None:
        #         print('linkprofile'+linkprofile)
        # # profileIds=getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
        #         Recdict[index]=visitProfile(Recdict,linkprofile)
        #         visitedProfiles=linkprofile
    page = page + 1
# for i in profileIds:
#         print(i)        
print('here')
print (len(Recdict))
# print(Recdict)
for x, y in Recdict.items():
    print(x, y)  
#%%Convert to  list 
import pandas as pd
values=Recdict.values()
values_list = list(values)
print(values_list,type(values_list))
#%%
df=pd.json_normalize(values_list)
df.to_csv("emp_list.csv")

#%%insert into Mongod
import pymongo
import itertools
import bson
from bson import BSON
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["alumni"]
mycol.delete_many({})
x = mycol.insert_many(values_list)
print('ids of inserted documents\n---------------------')
for id in x.inserted_ids:
	print(id)
for doc in mycol.find():
    #Print each document
    print(doc)

#%%ending here

 #print only values having non null
import bson
recdict1={k:v for k,v in Recdict.items() if  v}
for x, y in recdict1.items():
    print(x,y) 
print (len(Recdict))
# print(Recdict)


    #%%
import bson
from bson import json_util
Recdict1=Recdict.values()
for y in Recdict1:
    print(y)    
Rect1=json.dumps(Recdict, indent=4, default=json_util.default)
print(Rect1)
#%%
import pymongo
import bson
import itertools
import json
from bson import ObjectId,json_util
from json import JSONEncoder
import pandas as  pd


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["alumni"]
mycol.delete_many({})
# Recdict1=JSONEncoder.encode(Recdict,o)
new_rectdict = {k:v for k,v in Recdict.items() if v}
Rect1=json.dumps(new_rectdict, indent=4, default=json_util.default)
print(Rect1)
with open("sample.json", "w") as outfile: 
    outfile.write(Rect1) 
#%%    
pd.read_json("sample.json").to_excel("sample.xlsx")
# df_json.to_excel("sample.xlsx")
# %%
df=pd.DataFrame(new_rectdict) 
print(list(df.columns))


# print(df.Name.to_string(index=False))

# %%

# %% 
print(z)
myquery = {"Name": "Chandreyee Chowdhury" }  
a = mycol.find(myquery)   
for q in a:
  print(q)    

# %%   
collections = db.getCollectionNames();
for(var i = 0; i< collections.length; i++) {    
   print('Collection: ' + collections[i]); // print the name of each collection
   db.getCollection(collections[i]).find().forEach(printjson); //and then print     the json of each of its elements
}   
# %%
from pymongo import MongoClient

# Create connection to MongoDB
client = MongoClient('localhost', 27017)
db = client['name_of_database']
collection = db['name_of_collection']

# Build a basic dictionary
d = {'website': 'www.carrefax.com', 'author': 'Daniel Hoadley', 'colour': 'purple'}

# Insert the dictionary into Mongo
collection.insert(d)

# %%
# mydict = { "name": "John", "address": "Highway 37" }
import bson
import collections
# x = mycol.insert_one(mydict)
for x,y in Recdict.items():
   # print(x) 
   print(y)
   z=mycol.insert_one(y) 
   
# In[ ]:


# profilesQueued = getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
# for i in profilesQueued: 
#     print(i)    
# import urllib.request
# weburl=urllib.request.urlopen('https://www.linkedin.com/school/jadavpur-university/people/')
# print("result code"+str(weburl.getcode())
# data=weburl.read()
# print(data)


# %%


while profilesQueued:
    try:
        visitingProfileID = profilesQueued.pop()
        visitedProfiles.append(visitingProfileID)
        fullLink = 'https://www.linkedin.com' + visitingProfileID
        browser.get(fullLink)

        browser.find_element_by_class_name('pv-s-profile-actions').click()

        browser.find_element_by_class_name('mr1').click()

        customMessage = "Hello, I have found mutual interest area and I would be more than happy to connect with you. Kindly, accept my invitation. Thanks!"
        elementID = browser.find_element_by_id('custom-message')
        elementID.send_keys(customMessage)

        browser.find_element_by_class_name('ml1').click()

        # Add the ID to the visitedUsersFile
        with open('visitedUsers.txt', 'a') as visitedUsersFile:
            visitedUsersFile.write(str(visitingProfileID)+'\n')
        visitedUsersFile.close()

        # Get new profiles ID
        soup = BeautifulSoup(browser.page_source)
        try: 
            profilesQueued.extend(getNewProfileIDs(soup, profilesQueued))
        except:
            print('Continue')

        # Pause
        time.sleep(random.uniform(3, 7)) # Otherwise, sleep to make sure everything loads

        if(len(visitedProfiles)%50==0):
            print('Visited Profiles: ', len(visitedProfiles))

        if(len(profilesQueued)>100000):
            with open('profilesQueued.txt', 'a') as visitedUsersFile:
                visitedUsersFile.write(str(visitingProfileID)+'\n')
            visitedUsersFile.close()
            print('100,000 Done!!!')
            break;
    except:
        print('error')



