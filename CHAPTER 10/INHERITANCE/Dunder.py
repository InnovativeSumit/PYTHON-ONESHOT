class Student:
    def __init__(self, name, marks):
        self.name = name         
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

    def __len__(self):
        return len(self.name)


s = Student("Sumit", 85)

print(s)           # calls __str__()
print(len(s))      # calls __len__()
