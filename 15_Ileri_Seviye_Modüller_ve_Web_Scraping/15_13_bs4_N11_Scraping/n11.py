import requests
from bs4 import BeautifulSoup

URL = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=HEADERS).content
soup = BeautifulSoup(response, "html.parser")

product_list = soup.find_all("a", {"class": "product-item"}, limit=5)

print("Products Information:")
print(f"{'No':<3} | {'Product Name':<45} | {'Price':<12}")
print("-" * 65)

for idx, item in enumerate(product_list, start=1):
    name = item.find("h2", {"class": "product-item-title"}).text.strip()
    price = item.find("h3", {"class": "price-currency"}).text.strip()

    short_name = name[:42] + "..." if len(name) > 45 else name

    print(f"{idx:<3} | {short_name:<45} | {price:<12}")
