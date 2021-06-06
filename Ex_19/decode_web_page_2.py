import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
article_text = soup.find_all('p')
for text in article_text[6:-6]:
    print(text.get_text())
