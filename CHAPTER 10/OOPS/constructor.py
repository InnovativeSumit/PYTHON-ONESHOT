class employee:
    language = "java"
    salary = 120000 # this is called class attribute
    age = 20



    def __init__(self,name ,language, salary ,age ):
        self.name = name
        self.language = language
        self.salary = salary
        self.age = age
        print("Hello i ama a  parametarized constructor")






emp2 = employee("sohini","java",120000, 20)
print(emp2.name,emp2.language, emp2.salary,emp2.age)

emp2 = employee("sumit","python",150000, 20)
print(emp2.name,emp2.language, emp2.salary,emp2.age)


