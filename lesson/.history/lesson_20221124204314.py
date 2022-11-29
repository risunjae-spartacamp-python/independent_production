# ライブラリのインポート
import requests

# URLの設定


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

url = "https://yahoo.co.jp"
r = requests.get(url, headers=headers)

# requests.get()でサイトにアクセス
# r = requests.get(url, params={"s": "python"})
# header
# どんなシステムからアクセスがあるのか　    --> User-Agent
# どんな形でデータが欲しいのか


# print(r.text[:10])
# print(type(r.text[:10]))

# print(r.content[:10])
# print(type(r.content[:10]))

# print(r.text)
# print(r.status_code)

# print(r.history[0].url)
# r.raise_for_status()
# print("Success!!!!")
