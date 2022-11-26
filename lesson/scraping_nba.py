import requests
from bs4 import BeautifulSoup

url = "https://nba.rakuten.co.jp/news"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

post = soup.find("a", class_="NewsCard1-link")

for i, a in enumerate(post.find_all("a")):
    print("=" * 30, i, "=" * 30)
    print(a.find("a").text)
    print(a.find("time").text)
