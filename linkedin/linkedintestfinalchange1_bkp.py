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
# %%
visitingProfileID = '/in/shirsa-dutta-8301241a3/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)
que = browser.find_element_by_xpath('//*[@id="ember20"]/input')
print(que)
que.send_keys("jadavpur university department of information technology")
que.send_keys(Keys.ENTER)
# time.sleep(random.randint(1, 5))
# link2=browser.current_url
# print('link2@@@@'+link2)


# %%

visitedProfiles = []
profilesQueued = []
profilesID = []


def clean_string(var):
    var = str(var)
    var = var.strip()
    var = var.replace('\n', '')
    return var


def visitProfile(Recdict, link):
    browser.get(link)
    print('Enterd  visited profile')
    html_soup = BeautifulSoup(browser.page_source,'html.parser')
    print(link)
    name = html_soup.find("li", {"class": "inline t-24 t-black t-normal break-words"})
    if name is not None:
        print(name.text)
        IDs = []
        Defaults = {'designation': '', 'company': '',
            'dates_employed': '', 'employ_duration': ''}
        expdict = dict.fromkeys(IDs, Defaults)
        i=0
        # if(html_soup.find("section", {"class": "pv-profile-section experience-section ember-view"})):
        # expsect = (html_soup.find_all("section", {"id":"experience-section"}))
        # # print(expsect)
        # if(html_soup.find("section", {"id":"experience-section"})):
        #     print('hello1')
        #      expsect = html_soup.find("section", {"id": "pv-profile-section experience-section ember-view"})
        #     expsect = (html_soup.find("section", {"id":"experience-section"}))
        #     print(expsect)
        #     for k in expsect.find_all("section", {"pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view"}):
        #                 if k.find("h3", {"class": "t-16 t-black t-bold"}):
        #                     expdict['designation'] = clean_string(
        #                         k.find("h3", {"class": "t-16 t-black t-bold"}).text)
        #                 else:
        #                     expdict['designation'] = ''
        #                 if k.find("p", {"class": "pv-entity__secondary-title t-14 t-black t-normal"}):
        #                     expdict['company'] = clean_string(
        #                         k.find("p", {"class": "pv-entity__secondary-title t-14 t-black t-normal"}).text)
        #                 else:
        #                     expdict['company'] = ''
        #                 if k.find("span", {"class": "pv-entity__bullet-item-v2"}):
        #                     expdict['employ_duration'] = clean_string(
        #                         k.find("span", {"class": "pv-entity__bullet-item-v2"}).text)
        #                 else:
        #                     expdict['employ_duration'] = ''
        #                 if k.find("h4", {"class": "pv-entity__date-range t-14 t-black--light t-normal"}):
        #                     expdict['dates_employed'] = clean_string(k.find(
        #                         "h4", {"class": "pv-entity__date-range t-14 t-black--light t-normal"}).find("span", {"class": ""}).text)
        #                 else:
        #                     expdict['dates_employed'] = ''
        #         i=i+1
        # print(xx)
        
        if(html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})):
            print("@@@@here@@@@@")
            for k in html_soup.find_all("div",{"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"},limit=2) :
                    print("####there@@@@@")
                    expdict={'designation': clean_string(k.find("h3",{"class":"t-16 t-black t-bold"}).text) if k.find("h3",{"class":"t-16 t-black t-bold"}) else '',
                                'company': clean_string(k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text) if k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}) else '',
                                'employ_duration':clean_string(k.find("span",{"class":"pv-entity__bullet-item-v2"}).text) if k.find("span",{"class":"pv-entity__bullet-item-v2"}) else '',
                                'dates_employed': clean_string(k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}) else ''
                                }
            # i=i+1                  
        for x, y in expdict.items():
            print(x,y)                
        IDs = []
        Defaults = {'College': '', 'Degree': '', 'Branch': '', 'duration': ''}
        thisdict = dict.fromkeys(IDs, Defaults)
        print(thisdict)
        if (html_soup.find("section", {"id":"education-section"})):
            edusect=html_soup.find("section", {"id":"education-section"})
            for t in edusect.find_all("li", {"class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"}):
                if(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("jadavpur university",re.IGNORECASE))) :
                    thisdict={'college':clean_string(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).text) if t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}) else '',
                            'degree':t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text if t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}) else '',
                            'branch': clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text) if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}) else '',
                            'duration':clean_string(t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}) else ''
                                } 
        for x, y in thisdict.items():
            print(x,y)
        # edusect = html_soup.find("section", {"id": "education-section"})
        # if edusect:
        #     for t in edusect.find_all("li", {"class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"}):
        #         thisdict[i] = {}
        #         if (t.find("p", {"class": "pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"})):
        #             if (t.find("p", {"class": "pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find(text=re.compile("information technology", re.IGNORECASE))):
        #                 x = 1
        #             else:
        #                 x = 0
        #             if (t.find("h3", {"class": "pv-entity__school-name t-16 t-black t-bold"})):
        #                 if (t.find("h3", {"class": "pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("jadavpur university", re.IGNORECASE))):
        #                     y = 1
        #             else:
        #                 y = 0
        #             if (x == 1 and y == 1):
        #             # if (t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"})):
        #                 if t.find("p", {"class": "pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}):
        #                     thisdict[i]['Degree'] = t.find(
        #                         "p", {"class": "pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span", {"class": "pv-entity__comma-item"})
        #                 else:
        #                     thisdict[i]['Degree'] = ''
        #                 print(thisdict[i]['Degree'])
        #                 if t.find("h3", {"class": "pv-entity__school-name t-16 t-black t-bold"}):
        #                     thisdict[i]['College'] = clean_string(
        #                         t.find("h3", {"class": "pv-entity__school-name t-16 t-black t-bold"}).text)
        #                 else:
        #                     thisdict[i]['College'] = ''
        #                 print(thisdict[i]['College'])
        #                         #  if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}) else ''
        #                 if (t.find("p", {"class": "pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span", {"class": "pv-entity__comma-item"})):
        #                     thisdict[i]['Branch'] = clean_string(t.find(
        #                         "p", {"class": "pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span", {"class": "pv-entity__comma-item"}).text)
        #                 else:
        #                     thisdict[i]['Branch'] = ''
        #                 print(thisdict[i]['Branch'])
        #                 if (t.find("p", {"class": "pv-entity__dates t-14 t-black--light t-normal"}).find("span", {"class": ""})):
        #                     thisdict[i]['Duration'] = clean_string(t.find(
        #                         "p", {"class": "pv-entity__dates t-14 t-black--light t-normal"}).find("span", {"class": ""}).text)
        #                 else:
        #                     thisdict[i]['Duration'] = ''
        #                 print(thisdict[i]['Duration'])
            # else:
            #     pass
            # i=i+1

    #     print(x, y)
    try:
        # 'Edu':thisdict,
        Recdict = {'Name': name.text.strip(), 'Exp': expdict, 'Edu': thisdict}
    except:
            print("Unexpected error:", sys.exc_info()[0])
    return Recdict
#%%
visitingProfileID = '/in/shirsa-dutta-8301241a3/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)
que = browser.find_element_by_xpath('//*[@id="ember16"]/input')
print(que)
que.send_keys("jadavpur university department of information technology")
que.send_keys(Keys.ENTER)

 # %%
# que = browser.find_element_by_xpath('//*[@id="ember20"]/input')
# print(que)
# que.send_keys("jadavpur university department of information technology")
# que.send_keys(Keys.ENTER)
profilesQueued = []
profilesID = []
page = 1
index = 0
limit = 4
ids1 = []
Defaults1 = {'Name': '', 'Edu': '', 'Exp': ''}
Recdict = dict.fromkeys(ids1, Defaults1)
baselink = browser.current_url.partition('page')[0]
print('@@@@@@@@@@@@@baselink@@@@@@@@@@@@@@@@@@',baselink)
while(page < 2):
    # page = page + 1
    next_page = ''
    next_page = ('&page='+str(page))
    print('next_page: '+next_page)
    # print('link:'+link)
    nextlink = baselink+next_page
    print('nextlink:'+nextlink)
    time.sleep(random.randint(1, 5))
    try:
        browser.get(nextlink)
    except NoSuchElementException:
        print('in exception')
        break
    html_source = BeautifulSoup(browser.page_source, 'html.parser')
    excluded_link="https://www.linkedin.com/search/results/all/headless?keywords=jadavpur%20university%20department%20of%20information%20technology&amp;origin=GLOBAL_SEARCH_HEADER\">"
    match_pattern = 'https://www.linkedin.com/in/*'
    for profile in html_source.find_all("div", {"class": "entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"}):
        if profile is not None:
            linkprofile=""
            visited_set = set()
            # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&77')
            for b in profile.find_all("span", {"class": "entity-result__title-line flex-shrink-1 entity-result__title-text--black "}):
                # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&66')
                f=""
                for f in b.find_all("a",{"class":"app-aware-link"}) :
                    # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&55')
                    # print(f)
                    # if re.match(f['href'] ,"https:\/\/www.linkedin.com\/in\/\*") :
                    linkprofile = f['href']
                    if urlmatch.urlmatch(match_pattern,linkprofile):
                        print('linkprofile'+linkprofile)
                    # profileIds=getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
                        Recdict[index]=visitProfile(Recdict,linkprofile)
                        visitedProfiles=linkprofile
            if index is limit:
                print('####limit has reached')
                break
            index=index+1
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

for x, y in Recdict.items():
    print(x, y)    
   



# %%
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["alumni"]
for x,y in Recdict.items():
   print(x) 
   print(y)
   z=mycol.insert_one(y)
# %% 
myquery = {"Name": "Sanghamitra Lahiri" }  
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



