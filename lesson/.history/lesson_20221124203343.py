# ライブラリのインポート
import requests

# URLの設定
url = "https://tech-diary.net/"

# requests.get()でサイトにアクセス
r = requests.get(url, params={"s": "python"})
# header
# どんなシステムからアクセスがあるのか　    -->
# どんな形でデータが欲しいのか



# print(r.text[:10])
# print(type(r.text[:10]))

# print(r.content[:10])
# print(type(r.content[:10]))

print(r.url)
print(r.status_code)

# print(r.history[0].url)
# r.raise_for_status()
# print("Success!!!!")
