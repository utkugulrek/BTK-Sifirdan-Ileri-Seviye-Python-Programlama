"""
22_10_schooldb_demo.py dosyasının oop uygun versiyonu
"""

from datetime import datetime
from mysql.connector import Error
from connection import connection


class Student:
    connection = connection  # Sağdaki, import edilmiş olan

    mycursor = connection.cursor()

    def __init__(self, student_number, name, surname, birth_date, gender):
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender

    def save_student(self):
        sql = "INSERT INTO students(student_number, name, surname, birth_date, gender) VALUES (%s, %s, %s, %s, %s)"
        value = (
            self.student_number,
            self.name,
            self.surname,
            self.birth_date,
            self.gender,
        )
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except Error as err:
            print("Hata", err)
        finally:
            Student.connection.close()

    @staticmethod
    def save_students(students_list):
        sql = "INSERT INTO students(student_number, name, surname, birth_date, gender) VALUES (%s, %s, %s, %s, %s)"
        values = students_list
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except Error as err:
            print("Hata", err)
        finally:
            Student.connection.close()


# # Örnek: Tekil öğrenci kaydı
# mert = Student("202", "Mert", "D", datetime(1990, 5, 10), "E")
# mert.save_student()

# # Örnek: Çoğul öğrendi kaydı
ogrenciler = [
    ("401", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
    ("402", "Ali", "Can", datetime(2005, 6, 17), "E"),
    ("403", "Canan", "Tan", datetime(2005, 7, 7), "K"),
    ("404", "Ayşe", "Taner", datetime(2005, 9, 23), "K"),
    ("405", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
    ("406", "Ali", "Cenk", datetime(2003, 8, 25), "E"),
]

Student.save_students(ogrenciler)
