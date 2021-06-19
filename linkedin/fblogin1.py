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
username = 'shirsangshudutta@gmail.com'
password = '5082cris!'
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('E:\\pyhton\\driver\\chromedriver.exe')

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By., "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.id, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("my_username")
password.clear()
password.send_keys("my_password")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
