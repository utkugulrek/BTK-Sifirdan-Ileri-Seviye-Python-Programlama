"""
Cheapest iPhone 17 Pro Max finder in the Amazon TR market.
Checks prices every 10 minutes, prints the list to the terminal and highlights the cheapest option,
saves the data sorted from lowest to highest price to "product_tracking.csv".
"""

import time
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MIN_PRICE = 90000
MAX_PRICE = 170000
CHECK_PERIOD = 60 * 10  # 10 minutes
EXCLUDED_KEYWORDS = ["kılıf", "koruyucu", "kablo", "kılıfı", "cam", "lens", "adapter"]

options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode (without a GUI)
options.add_argument(
    "--disable-gpu"
)  # Disable GPU acceleration (optional, but can improve performance in headless mode) | Only in Windows
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
)


def save_data(product_list):
    file_name = "product_tracking.csv"
    save_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:  # If file is empty
            writer.writerow(
                [
                    "Date/Time".center(19),
                    "Product Name".center(156),
                    "Product Price".center(10),
                    "Link",
                ]
            )

        for product in product_list:
            writer.writerow(
                [
                    save_time,
                    product["name"][:156],
                    str(product["price"]).center(10),
                    product["link"],
                ]
            )

        file.write("-" * 200 + "\n")


driver = webdriver.Chrome(options=options)

try:
    while True:
        try:
            driver.get("https://www.amazon.com.tr")

            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            search_box.send_keys("iphone 17 pro max" + Keys.ENTER)

            # Is first product correctly found?
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "div.s-main-slot div[data-component-type='s-search-result']",
                    )
                )
            )

            product_cards = driver.find_elements(
                By.CSS_SELECTOR,
                "div.s-main-slot div[data-component-type='s-search-result']",
            )
            print(
                f"Found {len(product_cards)} product cards on the search results page."
            )
            products = []

            for index, product in enumerate(product_cards, start=1):
                try:
                    product_name = product.find_element(By.CSS_SELECTOR, "h2 span").text
                    product_price_whole = product.find_element(
                        By.CLASS_NAME, "a-price-whole"
                    ).text
                    product_price_fraction = product.find_element(
                        By.CLASS_NAME, "a-price-fraction"
                    ).text
                    product_link = product.find_element(
                        By.CLASS_NAME, "a-link-normal"
                    ).get_attribute("href")
                    product_number_price = float(
                        f"{product_price_whole.replace(".", "")}.{product_price_fraction}"
                    )

                    # Validation
                    if (
                        "17 pro max" in product_name.lower()
                        and MIN_PRICE <= product_number_price <= MAX_PRICE
                        and not any(
                            keyword in product_name.lower()
                            for keyword in EXCLUDED_KEYWORDS
                        )
                    ):
                        products.append(
                            (
                                {
                                    "name": product_name,
                                    "price": product_number_price,
                                    "link": product_link,
                                }
                            )
                        )
                        print(
                            f"Product {index}: {product_name[:40]}... - Price: {product_number_price} TL"
                        )

                except Exception as e:
                    print(f"Could not retrieve product information for product {index}")

            products.sort(key=lambda x: x["price"])
            if len(products) > 0:
                print("Cheapest One".center(50, "*"))
                print(
                    f"Cheapest Product Name:{products[0]["name"]} Price: {products[0]["price"]} Link: {products[0]["link"]}"
                )
                print("*" * 50)
                save_data(products)
        except Exception as e:
            print(f"Error: {e}")
        print("Search ended.".center(50, "-"))
        print(f"Wait for {CHECK_PERIOD // 60} minutes.")
        print("-" * 50)
        time.sleep(CHECK_PERIOD)
except KeyboardInterrupt:
    print("Process Interrupted.")
finally:
    driver.quit()
