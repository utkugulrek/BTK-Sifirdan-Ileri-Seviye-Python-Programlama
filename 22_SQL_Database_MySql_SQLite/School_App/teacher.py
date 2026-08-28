"""Teacher modeli"""


class Teacher:
    def __init__(self, id, branch, name, surname, birth_date, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender

    @staticmethod
    def create_teacher(obj):
        if obj is None:
            return None
        liste = []

        if isinstance(obj, tuple):  # fetchone ile tekil kayıt gelirse
            return Teacher(*obj)
        else:  # fetchall ile liste gelirse
            for i in obj:
                liste.append(Teacher(*i))
            return liste
