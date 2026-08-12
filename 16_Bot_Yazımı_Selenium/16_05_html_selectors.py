import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = os.path.abspath("kurs.html")
driver.get(f"file://{file_path}")
time.sleep(2)

# find_element() => tekil

header = driver.find_element(By.ID, "header")
print(f"Header: {header.text}")

subheader = driver.find_element(By.TAG_NAME, "h2")
print(f"Subheader: {subheader.text}")

input_field = driver.find_element(By.NAME, "username")
print(f"Input Field Placeholder: {input_field.get_attribute('placeholder')}")

course = driver.find_element(By.CLASS_NAME, "course-card")
course_title = course.find_element(By.TAG_NAME, "h2")
course_description = course.find_element(By.TAG_NAME, "p")
course_price = course.find_element(By.TAG_NAME, "span")

print(f"Course Title: {course_title.text}")
print(f"Course Description: {course_description.text}")
print(f"Course Price: {course_price.text}")
print("**************************************************")

# find_elements() => çoğul
courses = driver.find_elements(By.CLASS_NAME, "course-card")
print(f"Total Courses Found: {len(courses)}")

for index, course in enumerate(courses, start=1):
    course_title = course.find_element(By.TAG_NAME, "h2")
    course_description = course.find_element(By.TAG_NAME, "p")
    course_price = course.find_element(By.TAG_NAME, "span")

    print(f"Course {index}:")
    print(f"Title: {course_title.text}")
    print(f"Description: {course_description.text}")
    print(f"Price: {course_price.text}")
    print("--------------------------------------------------")

driver.quit()
