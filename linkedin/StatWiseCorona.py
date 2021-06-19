import datetime
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup



# url='https://www.worldometers.info/coronavirus/#countries'
page=requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
page=requests.get(url)
df=pd.DataFrame()
Defaults1 = {'State':'','Total':'','Deaths':''}
ids1 = []
thisdict = dict.fromkeys(ids1, Defaults1)
thisdict=[]
for a in soup.find("div",{"class":"field field-name-field-covid-statewise-data field-type-field-collection field-label-above"}).find_all("div",{"class":"content"}):
    thisdict.append({
    'State':a.find("div",{"class":"field field-name-field-select-state field-type-list-text field-label-above"}).find("div",{"class":"field-items"}).text.replace('\xa0', ''),
    'Total':int(a.find("div",{"class":"field field-name-field-total-confirmed-indians field-type-number-integer field-label-above"}).find("div",{"class":"field-items"}).text.replace('\xa0', '')),
    'Deaths':int(a.find("div",{"class":"field field-name-field-deaths field-type-number-integer field-label-above"}).find("div",{"class":"field-items"}).text.replace('\xa0', ''))
    })
# for i in thisdict:
#     print(i)
df=pd.DataFrame(thisdict)
print(df.sort_values(by=['Deaths'],ascending=False))
print(df) 
print(df.columns)
# for b in soup.find_all("a",{"class","mt_a"}) :
#     print("link",b.)