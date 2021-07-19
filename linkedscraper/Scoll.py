
#%%
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
time.sleep(random.randint(1, 3))
elementID.send_keys(password)
elementID.submit()

#%%
from selenium.webdriver.common.action_chains import ActionChains

visitedProfiles = []
profilesQueued = []
profilesID = []
exp=[]


def clean_string(var):
    var = str(var)
    var = var.strip()
    var = var.replace('\n', '')
    return var


def visitProfile(link):
    browser.get(link)
    time.sleep(random.randint(1,5))
    print('Enterd  visited profile')
    Defaults1 = {'Name':'','Current_location':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'latestcompany': '','dates_employed': '', 'employ_duration': '','duration':''}
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
    thisdict['Current_location']=clean_string(html_soup.find("span",{"class":"text-body-small inline t-black--light break-words"}).text)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # browser.implicitly_wait(10)
    # element=browser.find_element_by_xpath('//*[@id="education-section"]')
    # # browser.execute_script("document.getElementById('education-section').scrollIntoView()")
    # # js.executeScript("arguments[0].scrollIntoView();", Element);
    # action.moveToElement(element).click().build().perform()
    if (html_soup.find("section", {"class":"pv-profile-section education-section ember-view"})):
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
            k=0
            if (html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})):
                print("@@@@here@@@@@")
                for k in html_soup.find_all("div",{"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"}) :
                        print("####there@@@@@")
                        thisdict['designation']= clean_string(k.find("h3",{"class":"t-16 t-black t-bold"}).text) if k.find("h3",{"class":"t-16 t-black t-bold"}) else ''
                        thisdict['company']=clean_string(k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}).text) if k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"}) else ''
                        thisdict['employ_duration'] =clean_string(k.find("span",{"class":"pv-entity__bullet-item-v2"}).text) if k.find("span",{"class":"pv-entity__bullet-item-v2"}) else ''
                        thisdict['dates_employed'] =clean_string(k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"}) else ''
                        sub_str= "yr" 
                        res = thisdict['employ_duration'][:thisdict['employ_duration'].index(sub_str) + len(sub_str)] 
                        exp.append(res) 
                        print("k",k)
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
    print('exp',exp)                
    return thisdict 
#%%
link='https://www.linkedin.com/in/shirsangshu-dutta-57a3ab13/'
visitProfile(link)
# %%
