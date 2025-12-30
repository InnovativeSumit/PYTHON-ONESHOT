class Student:
    school = "ABC School"   # class attribute

    @classmethod
    def changeSchool(cls, new_school):
        cls.school = new_school   # modifies class attribute


s1 = Student()
s2 = Student()
print(s1.school)
print(s2.school)
Student.changeSchool("XYZ School")
print(s1.school)
print(s2.school)
