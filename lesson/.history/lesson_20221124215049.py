import requests
from bs4 import BeautifulSoup

url =
soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
