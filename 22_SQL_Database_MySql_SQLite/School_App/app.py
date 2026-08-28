"""Konsolda kullanıcı arayüzü"""

import datetime

from connection import connection
from db_manager import DbManager
from student import Student
from teacher import Teacher


class App:

    def __init__(self, connection):
        self.connection = connection

    def get_student(self):
        student_id = int(input("Öğrenci ID giriniz: "))

        with DbManager(self.connection) as db:
            student = db.get_student_by_id(student_id)
            if student:
                std = student[0] if isinstance(student, list) else student
                print(f"Öğrenci Adı: {std.name} {std.surname}")
            else:
                print("Öğrenci bulunamadı.")

    def display_classes(self):
        with DbManager(self.connection) as db:
            classes = db.get_classes()
            if classes:
                for c in classes:
                    print(f"{c.id}: {c.name}")
            else:
                print("Kayıtlı sınıf bulunamadı.")

    def display_students(self):
        self.display_classes()
        with DbManager(self.connection) as db:
            class_id = int(input("Hangi Sınıf ID: "))
            students = db.get_students_by_class_id(class_id)

            print("Öğrenci Listesi".center(50, "*"))
            if students:
                for std in students:
                    print(f"{std.id}- {std.name} {std.surname}")
            else:
                print("Bu sınıfta henüz öğrenci yok.")

        return class_id

    def add_student(self):
        self.display_classes()
        class_id = int(input("Hangi sınıf ID: "))
        number = input("Numara: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Doğum yılı: "))
        month = int(input("Doğum ayı: "))
        day = int(input("Doğum günü: "))
        birth_date = datetime.date(year, month, day)
        gender = input("Cinsiyet (E/K): ")

        student = Student(None, number, name, surname, birth_date, gender, class_id)
        with DbManager(self.connection) as db:
            db.add_student(student)

    def edit_student(self):
        self.display_students()
        student_id = int(input("Güncellenecek Öğrenci ID: "))

        with DbManager(self.connection) as db:
            student = db.get_student_by_id(student_id)

            if not student:
                print("Öğrenci bulunamadı!")
                return

            std = student[0] if isinstance(student, list) else student

            print("\n(Değiştirmek istemediğiniz alanları Enter ile boş geçebilirsiniz)")
            std.student_number = (
                input(f"Numara ({std.student_number}): ") or std.student_number
            )
            std.name = input(f"Ad ({std.name}): ") or std.name
            std.surname = input(f"Soyad ({std.surname}): ") or std.surname
            std.gender = input(f"Cinsiyet ({std.gender}): ") or std.gender

            class_id_input = input(f"Sınıf ID ({std.class_id}): ")
            std.class_id = int(class_id_input) if class_id_input else std.class_id

            year_input = input(f"Doğum yılı ({std.birth_date.year}): ")
            month_input = input(f"Doğum ayı ({std.birth_date.month}): ")
            day_input = input(f"Doğum günü ({std.birth_date.day}): ")

            year = int(year_input) if year_input else std.birth_date.year
            month = int(month_input) if month_input else std.birth_date.month
            day = int(day_input) if day_input else std.birth_date.day

            std.birth_date = datetime.date(year, month, day)

            db.edit_student(std)

    def delete_student(self):
        self.display_students()
        student_id = int(input("Silinecek Öğrenci ID: "))

        with DbManager(self.connection) as db:
            db.delete_student(student_id)

    def add_teacher(self):
        branch = input("Branş: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Doğum yılı: "))
        month = int(input("Doğum ayı: "))
        day = int(input("Doğum günü: "))
        birth_date = datetime.date(year, month, day)
        gender = input("Cinsiyet (E/K): ")

        teacher = Teacher(None, branch, name, surname, birth_date, gender)
        with DbManager(self.connection) as db:
            db.add_teacher(teacher)

    def get_courses_by_class(self):
        self.display_classes()
        class_id = int(input("Derslerini görmek istediğiniz Sınıf ID: "))
        with DbManager(self.connection) as db:
            courses = (
                db.get_courses_by_class_id(class_id)
                if hasattr(db, "get_courses_by_class_id")
                else None
            )
            if courses:
                for course in courses:
                    print(f"- {course.name}")
            else:
                print("Bu sınıfa tanımlı ders bulunamadı.")

    def run(self):
        while True:
            print(
                "\n1- Öğrenci Getir (ID ile)"
                "\n2- Sınıfa Göre Öğrencileri Listele"
                "\n3- Öğrenci Ekle"
                "\n4- Öğrenci Güncelle"
                "\n5- Öğrenci Sil"
                "\n6- Öğretmen Ekle"
                "\n7- Sınıflara Göre Dersler"
                "\n8- Çıkış"
            )
            secim = input("Seçiminiz: ")

            match secim:
                case "1":
                    self.get_student()
                case "2":
                    self.display_students()
                case "3":
                    self.add_student()
                case "4":
                    self.edit_student()
                case "5":
                    self.delete_student()
                case "6":
                    self.add_teacher()
                case "7":
                    self.get_courses_by_class()
                case "8":
                    if self.connection and self.connection.is_connected():
                        self.connection.close()
                        print("Database bağlantısı güvenle kapatıldı.")
                    print("Çıkış yapılıyor...")
                    break
                case _:
                    print("Geçersiz seçim! Lütfen 1-8 arasında bir değer giriniz.")


if __name__ == "__main__":
    app = App(connection)
    app.run()
