import requests
from bs4 import BeautifulSoup

url = "https://www.anaconda.com/"
r = requests.get(url)


soup = BeautifulSoup(r.text, "html.l")
print(soup.h1.text)
