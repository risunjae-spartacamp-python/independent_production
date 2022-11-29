import chromedriver_binary
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path="/Users/risunjae121/Desktop/lesson/tools/chromedriver",
    options=options,
)
driver.get("https://nba.rakuten.co.jp/news/")

class_list = driver.find_elements(by=By.CLASS_NAME, value="NewsCard1-link")

href_list = []
for i in class_list:
    b = i.get_attribute("href")
    href_list.append(b)

print(href_list)

driver.close()
