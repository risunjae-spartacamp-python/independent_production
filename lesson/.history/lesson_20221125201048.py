import requests
from bs4 import BeautifulSoup

url = "https://www.nikkei.com/"


html = requests.get(url)
soup = BeautifulSoup(html.content, "lxml")

chapter = soup.find(__build_class__ = "k-hub-list")
for items in chapter.find_all("a")

