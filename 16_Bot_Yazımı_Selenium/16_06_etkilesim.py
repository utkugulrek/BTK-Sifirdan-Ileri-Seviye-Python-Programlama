import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
file_path = os.path.abspath("kurs.html")
driver.get(f"file://{file_path}")
time.sleep(1)

# course = driver.find_elements(By.CLASS_NAME, "course-card")
courses = driver.find_elements(By.CSS_SELECTOR, ".course-card")
courses[0].click()  # Click on the first course card
time.sleep(1)

driver.switch_to.alert.accept()  # Accept the alert that appears after clicking
time.sleep(1)

username_input = driver.find_element(By.ID, "username")
btn = driver.find_element(By.ID, "submit-btn")
username_input.send_keys("testuser")  # Enter a username
time.sleep(2)
btn.click()  # Click the submit button
time.sleep(1)
driver.switch_to.alert.accept()

username_input.clear()  # Clear the input field
time.sleep(1)
username_input.send_keys("sadikturan")  # Enter another username
time.sleep(2)

driver.find_element(By.ID, "password").send_keys("123456")  # Enter a password
btn.click()  # Click the submit button again
time.sleep(2)


driver.quit()
