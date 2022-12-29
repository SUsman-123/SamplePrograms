class Student:
    marks_bouns = 1.5
    def __init__(self,first,last,marks):
        self.first = first
        self.last = last
        self,marks = marks
    @property
    def email(self):
        return  '{}.{}@gmail.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return  '{}.{}'.format(self.first,self.last)
    def apply_bouns(self):
        self.marks = int(self.marks * self.marks_bouns)





