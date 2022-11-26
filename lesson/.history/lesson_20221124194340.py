# ライブラリのインポート
import requests

# URLの設定
url = "https://www.python.org"

# requests.get()でサイトにアクセス
r = requests.get(url)

print(r.text[:10])
print(type(r.text[:10]))

print(r.content[:10])
print(type(r.content[:10]))

print(r.url)
print(r.status_code)

r.raise_for_status()
print(Success!!!!)
