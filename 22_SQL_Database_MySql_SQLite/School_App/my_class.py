"""MyClass modeli"""


class MyClass:
    def __init__(self, id, name, teacher_id):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacher_id = teacher_id

    @staticmethod
    def create_class(obj):
        if obj is None:
            return None

        if isinstance(obj, tuple):
            return MyClass(*obj)
        else:
            return [MyClass(*i) for i in obj]
