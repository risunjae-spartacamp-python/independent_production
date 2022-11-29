from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# ヘッドレスモード
options.add_argument("--headless")
# 
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="/Users/risunjae121/Desktop/lesson/tools/chromedriver"
)

driver.get("https://www.google.co.jp")
sleep(3)

search_bar = driver.find_element(By.NAME, "q")
sleep(3)

search_bar.send_keys("python")
sleep(3)

search_bar.submit()
sleep(5)

driver.quit()
