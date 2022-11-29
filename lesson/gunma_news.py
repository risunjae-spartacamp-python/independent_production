import requests
from bs4 import BeautifulSoup

url = "https://www.jomo-news.co.jp/subcategory/%E4%BC%8A%E5%8B%A2%E5%B4%8E%E5%B8%82"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")
# print(soup.find("h2", class_="m-article__ttl").text)
post = soup.find("h2", class_="m-article__ttl")

for h2 in soup.find_all("h2", class_="m-article__ttl"):
    print(h2.text)
