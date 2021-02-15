# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%


file = open('E:\config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
print(username)



# %%


import os, random, sys, time
# from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests



# %%


# https://pypi.org/project/selenium/
# https://selenium-python.readthedocs.io/api.html
# Download Google Chrome Drive -> https://chromedriver.chromium.org/downloads
# Driver is also included in my github repository
# Don't forget to edit config.txt file -> put your email and linkedin password



# %%
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
##browser = webdriver.Chrome(executable_path='E:\pyhton\driver\chromedriver.exe')



# %%


browser.get('https://www.linkedin.com/uas/login')



# %%


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)



# %%


elementID = browser.find_element_by_id('password')
elementID.send_keys(password)



# %%


elementID.submit()



# %%


visitingProfileID = '/in/shirsa-dutta-8301241a3/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)



# %%

  #que=browser.find_element_by_xpath('//*[@id="ember17"]/input')
que=browser.find_element_by_xpath('//*[@id="ember41"]/input')
#que=browser.find_element_by_class_name('search-global-typeahead__input always-show-placeholder')
que.send_keys("jadavpur university")
que.send_keys(Keys.RETURN)
home_url=browser.current_url
print (home_url)
#link2='https://www.linkedin.com/search/results/all/?keywords=jadavpur%20university&origin=GLOBAL_SEARCH_HEADER&page=2'
#browser.get(link2)
# link=browser.current_url.partition('&')[0]
# print(link)
# from selenium.webdriver.common.action_chains import ActionChains

# elementID = browser.find_element_by_xpath('//*[@id="ember17"]/input')
# print(elementID)
# actions = ActionChains(browser)
# actions.move_to_element(elementID).send_keys("jadavpur university").perform()
# ##username = driver.find_element_by_xpath





# %%


visitedProfiles = []
profilesQueued = []
profilesID = []



# %%
import re
import urllib.request
def visitProfile(liink,profilesID):
    browser.get(liink)
    #page_details = browser.get(liink)
    html_soup = BeautifulSoup(browser.page_source,'html.parser')
    print(html_soup)
    name = html_soup.find_all("li", {"class": "inline t-24 t-black t-normal break-words"})
    name1=name[0]
    profilesID.append(name1.text)
    exp=html_soup.find_all("div", {"class":"pv-entity__summary-info pv-entity__summary-info--background-section mb2"})
    #print(exp)
    IDs = []
    Defaults = {'id':'','designation':'', 'company':'','dates_employed':'','employ_duration':''}
    expdict = dict.fromkeys(IDs, Defaults)
    print(len(exp))
    j=0
    while(j<len(exp)):
        k=exp[j]  
        designation=k.find("h3",{"class":"t-16 t-black t-bold"})
        #print(designation.text)
        company=k.find("p",{"class":"pv-entity__secondary-title t-14 t-black t-normal"})
        #print(company.text)
        dates_employed=k.find("h4",{"class":"pv-entity__date-range t-14 t-black--light t-normal"})
        #print(dates_employed)
        #dates_employed1=dates_employed.find("span",{"class":"visually-hidden"})
        employ_duration=k.find("span",{"class":"pv-entity__bullet-item-v2"})
        #print(employ_duration)
        expdict[j]={'id':j,'designation': designation.text, 'company': company.text.strip(),'employ_duration':employ_duration.text}
        j=j+1
    IDs =[]
    Defaults = {'id':'','College':'', 'Degree':'','start':''}
    thisdict = dict.fromkeys(IDs, Defaults)
    i=0
    insti = html_soup.find_all("div", {"class": "pv-entity__summary-info pv-entity__summary-info--background-section"})
    while(i<len(insti)):
        t=insti[i]  
        college=t.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"})
        degree=t.find("span",{"class":"pv-entity__comma-item"})
        duration=t.find("p",{"class":"pv-entity__dates t-14 t-black--light t-normal"})
        thisdict[i]={'id':i,'college': college.text, 'degree': degree.text,'start':duration.text.strip()}
        i=i+1        
    # for x, y in thisdict.items():
    #     print(x, y)
    ids1=[]
    Defaults1 = {'Name':'','Edu':'', 'Exp':''}
    Recdict = dict.fromkeys(ids1, Defaults1) 
    Recdict={'Name':name1.text.strip(),'Edu':thisdict, 'Exp':expdict}
    for x, y in Recdict.items():
        print(x, y) 
    profilesID.append(Recdict)
    # profilsID.append('Exp':expdict)
def getNewProfileIDs(soup, profilesQueued):
    #profilesID = []
    print('hello')
    #print(soup)
    for ultag in soup.find_all('div', {'class': 'search-results-page core-rail'}):
        for litag in ultag.find_all('div',{'class': 'search-result__wrapper'}):
            name=litag.find('span',{'class':'name actor-name'})
            edu  =litag.find('p',{'subline-level-1 t-14 t-black t-normal search-result__truncate'})
            proflinkall=litag.find_all('a',{'class':'search-result__result-link ember-view'},href=True)
            #print(proflink)
            #print(proflink.attrs)
            #proflink=[a['href'] for a in litag.find('a',{'class':'search-result__result-link ember-view'}, href=True)]
            #proflink=litag.find('a',{'class':'search-result__result-link ember-view'},attrs={'href': re.compile("^/in")})
            for tag in proflinkall:
                    liink='https://www.linkedin.com'+tag.get('href')
                    


            if name is not None :
                #print('Name:'+name.text+'\tEdu:'+edu.text)
                name1=name.text
                profilesID.append(name1)
                edu1=edu.text
                #profilesID.append(edu1)
                profilesID.append(liink)
                visitProfile(liink,profilesID)

    #           mydict = {'Name': name1, 'Edu': edu1}

    return profilesID 
           

# %%
import requests
from requests import Response
from urllib.request import urlopen

profilesQueued = []
profilesID = []
page =0



while(page<2):
    page=page + 1
    next_page=''     
    next_page=('&page='+str(page))
    print('next_page: '+next_page)
    #print('link:'+link)
    link=browser.current_url.partition('page')[0]
    link1=link+next_page
    print('link1:'+link1)
    time.sleep(2)
    browser.get(link1)
    #getNewProfileIDs(BeautifulSoup(browser.source), profilesQueued)
    profileIds=getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
    # for key, val in profileIds.items():
    # print( 'Name',key,'Value',val)
    for i in profileIds:
        print(i)    

   



# In[ ]:


# profilesQueued = getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)
# for i in profilesQueued: 
#     print(i)    


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



