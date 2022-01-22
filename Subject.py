class Subject:

    def __init__(self, name, time, teacher_name, link):
        self.name = name
        self.time = time
        self.teacher_name = teacher_name
        self.link = link

    def set_name(self, name):
        self.name = name

    def set_time(self, time):
        self.time = time

    def set_teacher_name(self, teacher_name):
        self.teacher_name = teacher_name

    def set_link(self, link):
        self.link = link

    def get_name(self, name):
        self.name = name

    def get_time(self, time):
        self.time = time

    def get_teacher_name(self, teacher_name):
        self.teacher_name = teacher_name

    def get_link(self, link):
        self.link = link
