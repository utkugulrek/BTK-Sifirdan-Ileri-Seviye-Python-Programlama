"""3 isteri karşılayan database oluşturma"""

# İsterler:
"""
# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)
# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.
    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
"""

from datetime import datetime
import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="1234", use_pure=True, database="school_db"
)

mycursor = connection.cursor()

sql = "INSERT INTO students(student_number, name, surname, birth_date, gender) VALUES (%s, %s, %s, %s, %s)"
ogrenciler = [
    ("301", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
    ("302", "Ali", "Can", datetime(2005, 6, 17), "E"),
    ("303", "Canan", "Tan", datetime(2005, 7, 7), "K"),
    ("304", "Ayşe", "Taner", datetime(2005, 9, 23), "K"),
    ("305", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
    ("306", "Ali", "Cenk", datetime(2003, 8, 25), "E"),
]

mycursor.executemany(sql, ogrenciler)

try:
    connection.commit()
    print(f"{mycursor.rowcount} tane kayıt eklendi.")
except mysql.connector.Error as err:
    print("Hata", err)
finally:
    connection.close()
