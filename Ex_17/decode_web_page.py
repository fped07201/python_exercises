import requests
from bs4 import BeautifulSoup

url = "http://www.marca.com"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
# print(soup.prettify()
titles = soup.find_all(class_=["mod-title","flex-article__heading","block-list__item"])
for title in titles:
    print("* " + title.a.get_text().strip())
