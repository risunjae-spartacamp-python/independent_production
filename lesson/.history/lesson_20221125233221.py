from time import sleep
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path = "/Users/risunjae121/Desktop/lesson/tools/chromedriver")

driver.get("https://www.google.co.jp")
sleep(3)

search_bar = driver.find_element_by_name("q")
sleep(3)

search_bar.send_keys("python")
sleep(3)

search_bar.submit()
sleep(5)

driver.quit()
