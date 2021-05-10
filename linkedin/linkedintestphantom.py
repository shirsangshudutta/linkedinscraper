# # 
# from selenium import webdriver

# from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"]= ( "Mozilla/5.0 (Windows NT 6.3; WOW64) Applewebkit/537.36 (KHTML, like Gecko) Chrome/34.8.1847.137 Safari/537.36")
# driver= webdriver.PhantomJS(desired capabilities-dcap)
# driver.set_window_size(1024, 768) driver.get('https://google.com/">
# driver.save_screenshot('testing.png')
# element driver.find_element_by_xpath('//*[@id="input"]")
# element.send_keys('testing') element.send_keys (Keys.ENTER)
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
driver.quit()