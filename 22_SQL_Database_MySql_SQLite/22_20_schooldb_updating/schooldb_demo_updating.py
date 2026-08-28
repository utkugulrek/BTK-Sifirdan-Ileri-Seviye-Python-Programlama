"""
schooldb_demo_query.py Updating practice
"""

# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.


from datetime import datetime
from mysql.connector import Error
from connection import connection


class Student:
    connection = connection

    mycursor = connection.cursor()

    def __init__(self, id, student_number, name, surname, birth_date, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender

    @staticmethod
    def get_student_by_id(id):
        sql = "SELECT * FROM students WHERE id = %s"
        values = (id,)

        Student.mycursor.execute(sql, values)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])

        except Error as err:
            print(("Hata: ", err))

    def update_student(self):
        sql = "UPDATE students SET student_number=%s,name=%s,surname=%s,birth_date=%s,gender=%s WHERE id=%s"
        values = (
            self.student_number,
            self.name,
            self.surname,
            self.birth_date,
            self.gender,
            self.id,
        )

        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except Error as err:
            print("Hata: ", err)

    @staticmethod
    def update_students(liste):
        sql = "UPDATE students SET student_number=%s,name=%s,surname=%s,birth_date=%s,gender=%s WHERE id=%s"
        values = []
        order = [1, 2, 3, 4, 5, 0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except Error as err:
            print("Hata: ", err)

    @staticmethod
    def get_students_by_gender(gender):
        sql = "SELECT * FROM students WHERE gender = %s"
        values = (gender,)

        Student.mycursor.execute(sql, values)

        try:
            return Student.mycursor.fetchall()

        except Error as err:
            print(("Hata: ", err))


# Bilgileri almak
# id = input("Güncellemek istediğiniz kaydın ID numarası: ")
# obj = Student.get_student_by_id(id)

# Student objesi oluşturmak
# Obje return edecek şekilde güncellendi
# student = Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
# student = Student.get_student_by_id(id)

# # Obje üzerinde update
# student.name = "Veli"
# student.surname = "Kavlak"

# # Veri tabanına update
# student.update_student()

# # Erkek öğrencileri çekmek
students_e = Student.get_students_by_gender("E")
for student_e in students_e:
    print(student_e)


# Birden fazla güncelleme için update_students() metodu
liste = []
for std in students_e:
    std = list(std)
    std[2] = "Mr. " + std[2]
    liste.append(std)

Student.update_students(liste)
