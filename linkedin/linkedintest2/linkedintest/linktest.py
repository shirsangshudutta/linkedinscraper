
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
time.sleep(random.randint(1, 2))
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()

# visitingProfileID = '/in/shirsa-dutta-8301241a3/'
# fullLink = 'https://www.linkedin.com' + visitingProfileID
# browser.get(fullLink)


que=browser.find_element_by_xpath('//*[@id="ember41"]/input')
#que=browser.find_element_by_class_name('search-global-typeahead__input always-show-placeholder')
que.send_keys("jadavpur university")
que.send_keys(Keys.ENTER)
# time.sleep(random.randint(1, 5))
browser.forward()
link2=browser.refresh()
print('link2@@@@'+link2)
