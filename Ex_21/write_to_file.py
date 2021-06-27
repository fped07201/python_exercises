import requests
from bs4 import BeautifulSoup

filename = input("Please specify filename to store website content: ")

url = "http://www.marca.com"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
titles = soup.find_all(class_=["mod-title","flex-article__heading","block-list__item"])
with open(filename, 'w') as open_file:
    for title in titles:
        open_file.write("* " + title.a.get_text().strip() + "\n")
