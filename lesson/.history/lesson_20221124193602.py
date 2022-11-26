# ライブラリのインポート
import requests

# URLの設定
url = "https://www.python.org"

# requests.get()でサイトにアクセス
r = requests.get(url)

print(r.text[:10])
