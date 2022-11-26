from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import datetime

options = Options()
# 以下のコメントアウトを解除すると、ヘッドレスモードが有効になります。
# options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="/Users/risunjae121/Desktop/lesson/tools/chromedriver",
    options=options,
)
driver.get("https://www.google.co.jp")

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("히라이즈미")
search_bar.submit()

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "google_python_" + csv_date + ".csv"
f = open(csv_file_name, "w", encoding="utf-8-sig", errors="ignore")

writer = csv.writer(f, lineterminator="\n")
csv_header = ["検索順位", "タイトル", "URL"]
writer.writerow(csv_header)

i = 0
item = 1
while True:
    i = i + 1
    sleep(1)
    for elem_h3 in driver.find_elements(By.XPATH, "//a/h3"):
        elem_a = elem_h3.find_element(By.XPATH, "..")
        print(elem_h3.text)
        print(elem_a.get_attribute("href"))
        csvlist = []
        csvlist.append(str(item))
        csvlist.append(elem_h3.text)
        csvlist.append(elem_a.get_attribute("href"))
        writer.writerow(csvlist)
        item = item + 1
    next_link = driver.find_element(By.ID, "pnnext")
    driver.get(next_link.get_attribute("href"))
    if i > 4:
        break
f.close()
