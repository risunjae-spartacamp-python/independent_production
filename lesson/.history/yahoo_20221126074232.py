from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# ヘッドレスモード
# options.add_argument("--headless")
# シークレットモード
options.add_argument("--incognito")
# User-Agentの設定
options.add_argument(
    "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(
    executable_path="/Users/risunjae121/Desktop/lesson/tools/chromedriver",
    options=options)

driver.get("https://news.yahoo.co.jp")
sleep(3)

print(driver.title)
print(driver.current_url)

driver.quit()
