import chromedriver_binary
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(
    "https://www.jomo-news.co.jp/subcategory/%E4%BC%8A%E5%8B%A2%E5%B4%8E%E5%B8%82"
)

h2_list = driver.find_elements(by=By.TAG_NAME, value="h2")
title_list = []

for i in h2_list:
    title_list.append(i.text)
    time_list = driver.find_elements(by=By.CLASS_NAME, value="c-date")
    time_list = driver.find_elements(by=By.TAG_NAME, value="time")
    times_list = []
for i in time_list:
    times_list.append(i.text)
times_list
class_list = driver.find_elements(by=By.CLASS_NAME, value="m-article__link")
href_list = []
for i in class_list:
    b = i.get_attribute("href")
    href_list.append(b)
    href_list
    driver.close()
