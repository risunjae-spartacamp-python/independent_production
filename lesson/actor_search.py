import csv
import requests
from bs4 import BeautifulSoup

HEADER = ["name", "age", "occupation", "url"]

url = "https://talent-dictionary.com/s/jobs/3/20"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
actors = soup.find("ul", class_="list").find_all("li")

with open("actors.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for actor in actors:
        prof = actor.find("div", class_="right")

        name = prof.find("a", class_="title").text
        url = prof.find("a", class_="title").get("href")
        occupation = prof.find("a", class_="job").text
        age = prof.find("span", class_="age").text

        row = [name, age, occupation, url]
        writer.writerow(row)
