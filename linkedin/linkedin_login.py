import requests
from bs4 import BeautifulSoup

email = ""
password = ""

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')

login_information = {
    'session_key': 'shirsangshudutta@gmail.com',
    'session_password': 'times82!',
    'loginCsrfParam': csrf,
    'trk': 'guest_homepage-basic_sign-in-submit'
}

client.post(LOGIN_URL, data=login_information)

# response = client.get('')