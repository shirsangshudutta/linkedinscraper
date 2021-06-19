    # %%
import time
import sys
import random
import os
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen
from selenium.webdriver.common.by import By

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
elementID=browser.find_element_by_partial_link_text('Sign')   
elementID.submit()

# %%
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pathlib import Path, PurePath

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
visitedProfiles = []
profilesQueued = []
profilesID = []

def clean_string(var):
    var = str(var)
    var = var.strip()
    var = var.replace('\n', '')
    return var
def download_urls(urls):
    paths = []
    file_path="E:\scrapy_test\test"
    print('in downloads',urls)
    file_name = "html_file"
    print(file_name)
    # file_path = path.join(file_name)
    text = ''
    # print('###path',path)
    print('###filepath',file_path)
    try:
        response = requests.get(urls)
        if response.ok:
            text = response.text
        else:
            print('Bad response for', urls, response.status_code)
    except requests.exceptions.ConnectionError as exc:
        print(exc)

    with open(file_path, 'w') as fh:
        fh.write(text)

    # paths.append(file_path)

    return paths

def visitProfile(url):
    browser.get(url)
    print('Enterd  visited profile')
    Defaults1 = {'Name':'','Link':'','College': '', 'Degree': '', 'Branch': '', 'duration': '','designation': '', 'company': '','dates_employed': '', 'employ_duration': ''}
    ids1 = []
    thisdict = dict.fromkeys(ids1, Defaults1)
    print('link',browser.current_url)
    # browser.maximize_window()
    download_urls(url)

    html_soup = BeautifulSoup(browser.page_source,'html.parser')

    name = html_soup.find("li", {"class": "inline t-24 t-black t-normal break-words"})
    if name is not None:
        print(name.text)
    IDs = []
    thisdict['Name']= clean_string(name.text)
    thisdict['Link']= clean_string(link)
    time.sleep(10)
    # element = browser.find_element_by_xpath("//*[@id='ember45']/div[2]/div[2]/div[1]/ul[1]/li[1]")
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "education-section")))
    # browser.execute_script("return arguments[0].scrollIntoView();", element)
    # print('is_displayed element',element.is_displayed())
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(30)
        # element1=browser.find_element_by_xpath("//*[@id='education-section']")
    # print('is_displayed element',element1.is_displayed())
    if (html_soup.find("li", {"class":"pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"})):
        print('section1')
        # edusect=html_soup.find("section", {"class":"pv-profile-section education-section ember-view"})
        try:
            for t in html_soup.find_all("li", {"class": "pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"}):
                print('university',university)
                print('branch',branch)
                if(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("Jadavpur University",re.IGNORECASE))) :
                    print('@@univ')
                    if (html_soup.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).find(text=re.compile("Computer",re.IGNORECASE))) is not None:
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
?link='https://www.linkedin.com/in/shirsangshu-dutta-57a3ab13/'
Recdict=[]
# browser.get(link)
download_urls(link)
# Recdict=visitProfile(link)
# if  Recdict is not None:
#     for x, y in Recdict.items():
#         print(x,y)    
# %%
