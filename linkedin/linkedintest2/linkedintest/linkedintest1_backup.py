# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%

file = open('E:\config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
print(username)

import os, random, sys, time
# from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import requests
import re
#browser = webdriver.Chrome(ChromeDriverManager().install())
# import chromedriver_install as cdi
# path = cdi.install(file_directory='c:\\data\\chromedriver\\', verbose=True, chmod=True, overwrite=False, version=None)
# print('Installed chromedriver to path: %s' % path)
# browser = webdriver.Chrome("c:\\data\\chromedriver\\chromedriver.exe")
browser = webdriver.Chrome('E:\pyhton\driver\chromedriver.exe')
browser.get('https://www.linkedin.com/uas/login')

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
time.sleep(random.randint(1, 3))
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()

visitingProfileID = '/in/shirsa-dutta-8301241a3/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)


que=browser.find_element_by_xpath('//*[@id="ember41"]/input')
#que=browser.find_element_by_class_name('search-global-typeahead__input always-show-placeholder')
que.send_keys("jadavpur university")
que.send_keys(Keys.ENTER)
# time.sleep(random.randint(1, 5))
# link2=browser.current_url
# print('link2@@@@'+link2)



# %%


visitedProfiles = []
profilesQueued = []
profilesID = []



# %%
def clean_string(var):
    var=str(var)
    var=var.strip()
    var=var.replace('\n','')
    return var
def visitProfile(Recdict,link):
    browser.get(link)
    print('Enterd  visitprofile')
    html_soup = BeautifulSoup(browser.page_source,'html.parser')
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    name = html_soup.find("li", {"class": "inline t-24 t-black t-normal break-words"})
    if name is not None :
        print(name.text)
        IDs = []
        Defaults = {'designation':'', 'company':'','dates_employed':'','employ_duration':''}
        expdict = dict.fromkeys(IDs, Defaults)
        i=0
        xx=html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})
        print('ttt'+xx.text)
        if(html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})):
            expsect=html_soup.find("section", {"class":"pv-profile-section experience-section ember-view"})
            for k in expsect.find_all("section",{"pv-profile-section__card-item-v2 pv-profile-section pv-position-entity ember-view"}):
                expdict[i]={'designation': clean_string(k.find("h3",{"class":"t-16 t-black t-bold"}).text) if k.find("h3",{"class":"t-16 t-black t-bold"}) else '',
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
                if(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).find(text=re.compile("jadavpur university",re.IGNORECASE))) :
                    thisdict={'college':clean_string(t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).text) if t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}) else '',
                                'degree':t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text if t.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal"}) else '',
                                'branch': clean_string(t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}).text) if t.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}).find("span",{"class":"pv-entity__comma-item"}) else '',
                                'duration':clean_string(t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}).text) if t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"}).find("span",{"class":""}) else ''
                                } 
# # for x, y in thisdict.items():
    #     print(x, y)
    try:
        # 'Edu':thisdict,
        Recdict={'Name':name.text.strip(), 'Exp':expdict,'Edu':thisdict}
    except:
            print ("Unexpected error:", sys.exc_info()[0])
    return  Recdict

# %%
import requests
import  pprint
from requests import Response
from urllib.request import urlopen

profilesQueued = []
profilesID = []
page =0
index = 0
limit=30 
ids1=[]
Defaults1 = {'Name':'','Edu':'', 'Exp':''}
Recdict = dict.fromkeys(ids1, Defaults1) 
base_url="https://www.linkedin.com/search/results/all/?keywords=jadavpur%20university&origin=GLOBAL_SEARCH_HEADER"

while(page<2):
    page=page + 1
    next_page=''     
    next_page=(base_url+'&page='+str(page))
    
    print('next_page: '+next_page)
    #print('link:'+link)
    # link=browser.current_url.partition('page')[0]
    # link1=link+next_page
    # print('link1:'+link1)
    time.sleep(random.randint(1, 5))
    browser.get(next_page)
    html_source=BeautifulSoup(browser.page_source,'html.parser')
    for profile in html_source.find_all("div",{"class":"search-result__info pt3 pb4 ph0"}):
        if profile is not None:
            print('here2')
            if profile.find("a",{"class":"search-result__result-link ember-view"}) is not None:
                print('here3')
                link1=profile.find("a",{"class":"search-result__result-link ember-view"})
            # print(link1)
                # if link1 is not None:
                link='https://www.linkedin.com'+link1['href']
                print(link)
                # link="https://www.linkedin.com/in/abhijan-bhattacharyya-59b1a019/"
                index=index+1
    # profileIds=getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
                Recdict[index]=visitProfile(Recdict,link)
    

    # for key, val in profileIds.items():
    # print( 'Name',key,'Value',val)
# for i in profileIds:
#         print(i)        
print('here')
print (len(Recdict))

for x, y in Recdict.items():
    print(x, y)    
   



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



