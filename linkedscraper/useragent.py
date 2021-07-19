# from bs4 import BeautifulSoup
# import requests

# client = requests.Session()

# HOMEPAGE_URL = 'https://www.linkedin.com'
# LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

# html = client.get(HOMEPAGE_URL).content
# soup = BeautifulSoup(html, "html.parser")
# csrf = soup.find(id="loginCsrfParam-login")['value']

# login_information = {
#     'session_key':'shirsangshud@gmail.com',
#     'session_password':'times82!',
#     'loginCsrfParam': csrf,
# }

# client.post(LOGIN_URL, data=login_information)

# client.get('https://www.linkedin.com/in/john-raffaeli-7b269711/')
import requests
from bs4 import BeautifulSoup

email = "shirsangshud@gmail.com"
password = "times82!"

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')

login_information = {
    'session_key': email,
    'session_password': password,
    'loginCsrfParam': csrf,
    'trk': 'guest_homepage-basic_sign-in-submit'
}

client.post(LOGIN_URL, data=login_information)

response = client.get('https://www.linkedin.com/in/john-raffaeli-7b269711/')
# print(response.text)
html1 = client.get('https://www.linkedin.com/in/john-raffaeli-7b269711/').content

soup1 = BeautifulSoup(html1, "html.parser")
print(soup1)
# name = soup1.find("h1", {"class": "text-heading-xlarge inline t-24 v-align-middle break-words"})
# print(name)
