
from bs4 import BeautifulSoup


soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
