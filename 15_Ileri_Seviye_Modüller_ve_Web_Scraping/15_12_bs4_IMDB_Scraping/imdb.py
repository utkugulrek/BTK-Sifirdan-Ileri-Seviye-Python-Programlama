# IMDB Siteyi koruduğu için eski kodu ekledim.
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("ul", {"class": "ipc-metadata-list"}).find_all("li", limit=10)

for item in liste:
    filmadi = item.find("h3", {"class": "ipc-title__text"}).text
    puan = item.find("span", {"class": "ipc-rating-star"}).text
    print(filmadi, puan)
