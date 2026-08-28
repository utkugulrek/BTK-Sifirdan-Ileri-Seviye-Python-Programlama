"""ClassLesson modeli"""


class ClassLesson:

    def __init__(self, class_id, lesson_id, teacher_id, id=None):
        self.id = 0 if id is None else id
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.teacher_id = teacher_id

    @staticmethod
    def create_class_lesson(obj):
        if obj is None:
            return None

        if isinstance(obj, tuple):
            return ClassLesson(*obj)
        else:
            return [ClassLesson(*i) for i in obj]
