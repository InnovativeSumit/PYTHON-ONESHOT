class employee:
    language = "java"
    salary = 120000 # this is called class attribute
    age = 8

    def getinfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greeting():
        print("Good morning")

    def greet(self):
        print("Good afternoon")


emp1 = employee()
emp1.name = "Sumit"
emp1.salary = 1000000 # this is called instance attribute

print(emp1.name, emp1.salary, emp1.age)


emp1.greeting()
emp1.getinfo()
employee.getinfo(emp1)
emp1.greet()



