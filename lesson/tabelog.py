import requests
from bs4 import BeautifulSoup
import pandas as pd


# 食べログのURL
url = "https://tabelog.com/iwate/C3402/rstLst/?SrtT=rt&svd=20221126&svt=1900&svps=2&select_sort_flg=1&Srt=D&sort_mode=1"

# タグ取得
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
restrants = soup.find_all("div", class_="list-rst__wrap js-open-new-window")

# テーブル作成
table = []

for restrant in restrants:
    shopname = restrant.find(
        "a", class_="list-rst__rst-name-target cpy-rst-name js-ranking-num"
    )
    star = restrant.find("span", class_="list-rst__rating-val")
    table.append([shopname.get_text(), shopname["href"], star.text])


Column = ["店舗名", "URL", "点数"]

# データフレームを作成
df = pd.DataFrame(table, columns=Column)

# CSV ファイル出力
df.to_csv(r"tabelog.csv", encoding="utf_8_sig")
