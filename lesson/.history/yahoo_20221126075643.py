from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# ヘッドレスモード
# options.add_argument("--headless")
# シークレットモード
# options.add_argument("--incognito")
# User-Agentの設定
# options.add_argument(
    # "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(
    executable_path="/Users/risunjae121/Desktop/lesson/tools/chromedriver",
    options=options,
)
driver.implicitly_wait(10)

driver.get("https://news.yahoo.co.jp")
sleep(3)

e = driver.find_element(By.TAG_NAME, "h2")

for h2_tag in h2_tags:
    print(h2_tag.text)
    print(h2_tag.get_attribute("outerHTML"))

driver.quit()
