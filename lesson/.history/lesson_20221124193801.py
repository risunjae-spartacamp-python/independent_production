# ライブラリのインポート
import requests

# URLの設定
url = "https://www.python.org"

# requests.get()でサイトにアクセス
r = requests.get(url)

print(r.text[:10])
print(type(r.text[:10]))

print(r.content[:10])
