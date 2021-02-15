import os, random, sys, time
# from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import urllib.request
import random, time
import json


file = open('E:\config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
print(username)
browser = webdriver.Chrome('E:\pyhton\driver\chromedriver.exe')

browser.get('https://www.linkedin.com/uas/login')
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
time.sleep(random.randint(1, 3))

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
time.sleep(random.randint(1, 3))
elementID.submit()
# fullLink = 'https://www.linkedin.com/school/jadavpur-university/people/'
fullLink="https://www.linkedin.com/in/aditya-sengupta-b6374529/"
# fullLink="https://www.linkedin.com/in/surangam-sur-592b3915/"
# fullLink="https://www.linkedin.com/in/sreemoyee-nag-224287a9/"

#%%
def clean_string(var):
    var=str(var)
    var=var.strip()
    var=var.replace('\n','')
    return var
# %%
def visitProfile(Recdict,link):
    #browser.get(liink)
    page_details = browser.get(link)
    html_soup = BeautifulSoup(browser.page_source,'html.parser')
    name = html_soup.find_all("li", {"class": "inline t-24 t-black t-normal break-words"})
    name1=name[0]
    print(name1.text)
    IDs = []
    Defaults = {'designation':'', 'company':'','dates_employed':'','employ_duration':''}
    expdict = dict.fromkeys(IDs, Defaults)
    if (html_soup.find("section", {"id":"experience-section"})):
    # print(expsect)
        expsect=html_soup.find("section", {"id":"experience-section"})
        i=0
        for k in expsect.find_all("section",{"pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view"}):
            expdict[i]={
                    
                    'designation': clean_string(k.find("h3",{"class":"t-16 t-black t-bold"}).text) if k.find("h3",{"class":"t-16 t-black t-bold"}) else '',
                    'company': clean_string(k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text) if k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}) else '',
                    'employ_duration':clean_string(k.find("span",{"class":"pv-entity__bullet-item-v2"}).text) if k.find("span",{"class":"pv-entity__bullet-item-v2"}) else '',
                    'dates_employed': clean_string(k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}) else ''
                    }
            i=i+1        
    IDs =[]
    Defaults = {'College':'','Degree':'','Branch':'','duration':''}
    thisdict = dict.fromkeys(IDs, Defaults)
    if (html_soup.find("section", {"id":"education-section"})):
        edusect=html_soup.find("section", {"id":"education-section"})
    for t in edusect.find_all("li", {"class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"}):
        thisdict={'college':clean_string(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(lambda x: x.text.lower() == 'jadavpur University').text) if t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}) else '',
                'degree':t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text if t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}) else '',
                'branch': clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text) if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}) else '',
                'duration':clean_string(t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}) else ''
                } 
# # for x, y in thisdict.items():
    #     print(x, y)
    try:
        # 'Edu':thisdict,
        Recdict={'Name':name1.text.strip(), 'Exp':expdict,'Edu':thisdict}
    except:
            print ("Unexpected error:", sys.exc_info()[0])
    return  Recdict       
# %% 
browser.get(fullLink)
html1=BeautifulSoup(browser.page_source,'html.parser')
#alum=html1.find("ul",{"class":"org-people-profiles-module__profile-list"})
index = 0
limit=1
ids1=[]
Defaults1 = {'Name':'','Edu':'', 'Exp':''}
Recdict = dict.fromkeys(ids1, Defaults1) 
Recdict[index]=visitProfile(Recdict,fullLink)
print('here')
print (len(Recdict))

# for x, y in Recdict.items():
#     print(x, y)     
# %%
# from  pymongo import MongoClient
# client=MongoClient()
# client=MongoClient('localhost',27017)
# db=client.first
print(json.dumps(Recdict))




# %%
