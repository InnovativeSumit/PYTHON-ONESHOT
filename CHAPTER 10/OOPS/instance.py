class employee:
    salary = 8974 # this is called class attribute
    age = 8

# employee 1
emp1 = employee()
emp1.name = "Sumit"
emp1.salary = 899633 # this is called instance attribute

# employee 2
emp2 = employee()
emp2.name = "Amit"

# employee 3
emp3 = employee()
emp3.name = "Rohit"

# print details
print(emp1.name, emp1.salary, emp1.age)
print(emp2.name, emp2.salary, emp2.age)
print(emp3.name, emp3.salary, emp3.age)
