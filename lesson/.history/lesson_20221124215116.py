import requests
from bs4 import BeautifulSoup

url = "https://www.anaconda"
soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
