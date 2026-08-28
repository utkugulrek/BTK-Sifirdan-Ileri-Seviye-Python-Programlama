"""Veri tabanı ile iletişim"""

import mysql.connector

from connection import connection
from student import Student
from teacher import Teacher
from my_class import MyClass


class DbManager:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def __enter__(self):  # with bloğuna girildiğinde cursor oluşturulur
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with bloğundan çıkıldığında (işlem bitince) her şey güvenle kapatılır
        if self.cursor:
            self.cursor.close()

    def get_student_by_id(self, id):
        sql = "SELECT * FROM students WHERE id = %s"
        value = (id,)
        try:
            self.cursor.execute(sql, value)
            obj = self.cursor.fetchone()
            if obj is not None:
                return Student.create_student(obj)
            return None
        except mysql.connector.Error as err:
            print("Hata: ", err)
            return None

    def get_classes(self):
        sql = "SELECT * FROM classes"
        try:
            self.cursor.execute(sql)
            obj = self.cursor.fetchall()
            if obj is not None:
                return MyClass.create_class(obj)
            return None
        except mysql.connector.Error as err:
            print("Hata: ", err)
            return None

    def get_students_by_class_id(self, class_id):
        sql = "SELECT * FROM students WHERE class_id = %s"
        value = (class_id,)
        try:
            self.cursor.execute(sql, value)
            obj = self.cursor.fetchall()
            if obj is not None:
                return Student.create_student(obj)
            return None
        except mysql.connector.Error as err:
            print("Hata: ", err)
            return None

    def add_student(self, student: Student):
        sql = "INSERT INTO students(student_number, name, surname, birth_date, gender, class_id) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (
            student.student_number,
            student.name,
            student.surname,
            student.birth_date,
            student.gender,
            student.class_id,
        )

        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata", err)

    def edit_student(self, student: Student):
        sql = "UPDATE students SET student_number=%s,name=%s,surname=%s,birth_date=%s,gender=%s, class_id=%s WHERE id=%s"
        value = (
            student.student_number,
            student.name,
            student.surname,
            student.birth_date,
            student.gender,
            student.class_id,
            student.id,
        )

        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata", err)

    def delete_student(self, student_id):
        sql = "DELETE FROM students WHERE id=%s"
        value = (student_id,)

        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi.")
        except mysql.connector.Error as err:
            print("Hata", err)

    def add_teacher(self, teacher: Teacher):
        pass

    def edit_teacher(self, teacher: Teacher):
        pass

    def get_teacher_by_id(self, id):
        sql = "SELECT * FROM teachers WHERE id = %s"
        value = (id,)
        try:
            self.cursor.execute(sql, value)
            obj = self.cursor.fetchone()
            if obj is not None:
                return Teacher.create_teacher(obj)
            return None
        except mysql.connector.Error as err:
            print("Hata: ", err)
            return None

    def get_teachers(self):
        sql = "SELECT * FROM teachers"
        try:
            self.cursor.execute(sql)
            obj = self.cursor.fetchall()
            if obj is not None:
                return Teacher.create_teacher(obj)
            return None
        except mysql.connector.Error as err:
            print("Hata: ", err)
            return None

    def add_teacher(self, teacher: Teacher):
        sql = "INSERT INTO teachers(branch, name, surname, birth_date, gender) VALUES (%s, %s, %s, %s, %s)"
        value = (
            teacher.branch,
            teacher.name,
            teacher.surname,
            teacher.birth_date,
            teacher.gender,
        )
        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane öğretmen eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)

    def edit_teacher(self, teacher: Teacher):
        sql = "UPDATE teachers SET branch=%s, name=%s, surname=%s, birth_date=%s, gender=%s WHERE id=%s"
        value = (
            teacher.branch,
            teacher.name,
            teacher.surname,
            teacher.birth_date,
            teacher.gender,
            teacher.id,
        )
        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane öğretmen güncellendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)

    def delete_teacher(self, teacher_id):
        sql = "DELETE FROM teachers WHERE id=%s"
        value = (teacher_id,)
        try:
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane öğretmen silindi.")
        except mysql.connector.Error as err:
            print("Hata:", err)


# with ile açarak sağlıklı bağlantı sonlandırma
# with DbManager(connection) as db:
#     student = db.get_student_by_id(1)

#     if student:
#         print(f"Öğrenci Adı: {student[0].name}")

#         student[0].name = "Utku"
#         db.edit_student(student[0])
