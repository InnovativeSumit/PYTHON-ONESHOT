class Student:
    def __init__(self, marks):
        self._marks = marks   # protected attribute

    @property
    def marks(self):
        return self._marks    # getter

    @marks.setter
    def marks(self, value):
        if value < 0:
            print("Marks cannot be negative")
        else:
            self._marks = value

    @marks.deleter
    def marks(self):
        del self._marks
        print("Marks deleted")


s = Student(80)
print(s.marks)     # getter

s.marks = 90       # setter
print(s.marks)

s.marks = -10      # validation
del s.marks        # deleter
