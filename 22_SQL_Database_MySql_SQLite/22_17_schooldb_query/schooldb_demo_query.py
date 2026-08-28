"""
schooldb_demo_oop.py Sorgu yazma practice
"""

# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız.                      YEAR()
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.


from datetime import datetime
from mysql.connector import Error
from connection import connection


class Student:
    connection = connection

    mycursor = connection.cursor()

    def __init__(self, student_number, name, surname, birth_date, gender):
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender

    @staticmethod
    def student_info():
        sql = "SELECT * FROM students"  # a
        sql = "SELECT student_number, name, surname FROM students"  # b
        sql = "SELECT name, surname FROM students WHERE gender = 'K'"  # c
        sql = "SELECT * FROM students WHERE YEAR(birth_date) = 2003"  # d
        sql = "SELECT * FROM students WHERE name='Ali' and YEAR(birth_date) = 2005"  # e
        sql = (
            "SELECT * FROM students WHERE name LIKE '%an%' OR surname LIKE '%an%'"  # f
        )
        sql = "SELECT COUNT(*) FROM students WHERE gender = 'E'"  # g
        sql = "SELECT * FROM students WHERE gender = 'K' ORDER BY name, surname"  # h
        sql = "SELECT * FROM students LIMIT 5"  # LIMIT

        Student.mycursor.execute(sql)

        try:
            responses = Student.mycursor.fetchall()
            for response in responses:
                print(response)
        except Error as err:
            print("Hata: ", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kapandı.")


Student.student_info()
