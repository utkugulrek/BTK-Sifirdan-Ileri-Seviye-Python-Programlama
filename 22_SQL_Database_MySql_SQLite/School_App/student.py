"""Student modeli"""


class Student:
    def __init__(self, id, student_number, name, surname, birth_date, gender, class_id):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.student_number = student_number
        if len(name) > 45:
            raise Exception("Name için maksimum 45 karakter giriniz.")
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
        self.class_id = class_id

    @staticmethod
    def create_student(obj):
        if obj is None:
            return None

        if isinstance(obj, tuple):  # Tekil gelirse
            return Student(*obj)
        else:
            return [Student(*i) for i in obj]
