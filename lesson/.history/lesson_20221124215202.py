import requests
from bs4 import BeautifulSoup

url = "https://www.anaconda.com/"
r = requests.get(url)


soup = BeautifulSoup(r.te, "html.parser")
print(soup.h1.text)
