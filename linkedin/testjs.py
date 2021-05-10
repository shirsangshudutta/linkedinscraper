from selenium import webdriver
from bs4 import BeautifulSoup
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke #actual browser
driver = webdriver.Chrome(executable_path="E:\\pyhton\\driver\\chromedriver.exe")
# to maximize the browser window
#get method to launch the URL
# driver.get("https://in.yahoo.com//")
# element = driver.find_element_by_xpath("//*[@id='stream_item_title_8']")
# driver.execute_script("return arguments[0].scrollIntoView();", element)
# print('hello')
# #to refresh the browser
# driver.refresh()
# # identifying the link with the help of Javascript executor
# javaScript = "document.getElementsByClassName('tp-logo')[0].click();"
# driver.execute_script(javaScript)
# #to close the browser
# driver.quit()
url ='https://www.worldometers.info/coronavirus/country/india/'
driver.get(url)
page = driver.execute_script('return document.body.innerHTML')
soup = BeautifulSoup(''.join(page), 'html.parser')
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