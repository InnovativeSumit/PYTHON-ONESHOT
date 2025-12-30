class employee:
    language = "java"
    salary = 120000   # class attribute
    age = 20

    def __init__(self, name=None, salary=None, age=None):
        if name is None:
            print("Hello I am a default constructor")
        else:
            self.name = name
            self.salary = salary
            self.age = age
            print("Hello I am a parameterized constructor")


# default constructor
emp1 = employee()

# parameterized constructors
emp2 = employee("sohini", 120000, 20)
print(emp2.name, emp2.salary, emp2.age)

emp3 = employee("sumit", 150000, 20)
print(emp3.name, emp3.salary, emp3.age)
