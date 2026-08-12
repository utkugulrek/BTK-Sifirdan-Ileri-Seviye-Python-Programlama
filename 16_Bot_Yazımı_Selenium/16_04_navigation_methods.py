import time
from selenium import webdriver

driver = webdriver.Chrome()

URL = "https://www.github.com"

### Siteye giriş
driver.get(URL)
driver.maximize_window()
# driver.set_window_size(800, 600)
# time.sleep(2)
# driver.minimize_window()
# time.sleep(2)

### Sayfa Bilgilerini Alma
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
# driver.save_screenshot("github_screenshot.png")

### Sayfalar Arasında Geçiş Yapma
TARGET_USER = "utkugulrek_"
driver.get(f"{URL}/{TARGET_USER}")
time.sleep(2)

### Doğrulama
if TARGET_USER.lower() in driver.title.lower():
    print(f"{TARGET_USER} kullanıcısının sayfasına başarıyla geçiş yapıldı.")
    driver.save_screenshot(f"github_screenshot_{TARGET_USER}_screenshot.png")
else:
    print(f"{TARGET_USER} kullanıcısının sayfasına geçiş başarısız oldu.")
    driver.back()
    print("Önceki sayfaya geri dönüldü.", driver.current_url)
time.sleep(2)

TARGET_USER = "utkugulrek"
driver.get(f"{URL}/{TARGET_USER}")
driver.refresh()
print("Sayfa yenilendi.", driver.current_url)

driver.quit()
