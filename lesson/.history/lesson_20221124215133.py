import requests
from bs4 import BeautifulSoup

url = "https://www.anaconda.com/"
r = re
soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
