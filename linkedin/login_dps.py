# %%

import time
import sys
import random
import os
from selenium.common.exceptions import NoSuchElementException
import urlmatch
from requests import Response
import re
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
browser = webdriver.Chrome('E:\\pyhton\\driver\\chromedriver.exe')
# browser = webdriver.Chrome(executable_path='E:\\python\\driver\\chromedriver.exe')

# from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Chrome(ChromeDriverManager().install())
username
browser.get('https://www.linkedin.com/uas/login')

elementID = browser.find_element_by_id('login-form-main-message')
elementID.send_keys(username)
time.sleep(random.randint(1, 3))
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)