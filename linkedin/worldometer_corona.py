#%%
import requests
from bs4 import BeautifulSoup
import datetime 
import re

url ='https://www.worldometers.info/coronavirus/country/india/'
page=requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
for a  in soup.find_all("div",{"class":"maincounter-number"}):
 if (a.find_parent("div").find("h1").find(text=re.compile("Deaths"))):
    # print(a.find_parent("div").find("h1").find(re.compile("Deaths")))
    # t=a.find_parent("div").find("h1")
    # .find(re.compile("Deaths:"))
    # if(t.get_text())
    Defaults1 = {'Date':'','Deaths':''}
    ids1 = []
    t= dict.fromkeys(ids1, Defaults1)
    t=(datetime.datetime.today().strftime('%m/%d/%Y'),a.text)
    print(t,type(t))
# t1=soup.find_all(re.compile("Deaths:"))
# print(t1)
#%%
import pymongo
import itertools
import bson
from bson import BSON
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["coronavirus"]
# mycol.delete_many({})
x = mycol.insert_many(t)
print('ids of inserted documents\n---------------------')
for id in x.inserted_ids:
	print(id)
for doc in mycol.find():
    #Print each document
    print(doc)