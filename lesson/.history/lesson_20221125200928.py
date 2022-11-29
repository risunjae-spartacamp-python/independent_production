import requests
from bs4 import BeautifulSoup

url = "https://www.nikkei.com/"


html = requests.get(url)
soup = BeautifulSoup(html.content, "lxml")

chapter = sou
