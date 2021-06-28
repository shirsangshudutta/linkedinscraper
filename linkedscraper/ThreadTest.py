#%%
from selenium import webdriver
from time import sleep


# browser = webdriver.Firefox()
browser = webdriver.Chrome('E:\\pyhton\\driver\\chromedriver.exe')
browser.get('https://www.google.com/')
inputs = browser.find_elements_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input') 
print
for i in inputs:
    if i.is_displayed(): 
        search_bar = i 
        break


search_bar.send_keys('web scraping with python') 
search_bar.send_keys(Keys.ENTER)


browser.implicitly_wait(10)
results = browser.find_elements_by_css_selector('div h3 a') 

for r in results:
    action = webdriver.ActionChains(browser)
    action.move_to_element(r)
    action.perform()
    sleep(2)

browser.quit()
# %%
