from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# ヘッドレスモード
# options.add_argument("--headless")
# シークレットモード
options.add_argument("--incognito")
# User-Agentの設定
# options.add_argument(
#     "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# )

driver = webdriver.Chrome(
    executable_path="/Users/risunjae121/Desktop/lesson/tools/chromedriver",
    options=options,
)
driver.implicitly_wait(10)

driver.get("https://news.yahoo.co.jp")
sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, "input.sc-kgoBCf")
sleep(3)

search_box.send_keys("平泉")
sleep(3)

search_box.submit()
sleep(3)

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)

    button = driver.find_elements(By.CSS_SELECTOR, "div.newsFeed > div > span > button")
    sleep(3)

    if button:
        button[0].click()
    else:
        break

a_tags = driver.find_elements(By.CSS_SELECTOR, "a.newsFeed_item_link")

for i, a_tag in enumerate(a_tags):
    print("=" * 30, i, "=" * 30)
    print(a_tag.find_element(By.CSS_SELECTOR, ".newsFeed_item_title").text)
    print(a_tag.get_attribute("href"))

# height = driver.execute_script("return document.body.scrollHeight")
# sleep(3)

# sleep(3)

driver.quit()
