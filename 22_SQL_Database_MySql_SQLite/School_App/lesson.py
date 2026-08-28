"""Lesson modeli"""


class Lesson:

    def __init__(self, id, name):
        self.id = 0 if id is None else id
        self.name = name

    @staticmethod
    def create_lesson(obj):
        if obj is None:
            return None

        if isinstance(obj, tuple):
            return Lesson(*obj)
        else:
            return [Lesson(*i) for i in obj]
