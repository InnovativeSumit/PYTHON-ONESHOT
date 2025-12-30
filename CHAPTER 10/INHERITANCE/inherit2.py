class Employee:
    company = "ITC"

    def show(self):
        print(f"Company: {self.company}")



class Programmer(Employee):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"Programmer works in {self.company}")


a = Employee()
b = Programmer()

print(a.company, b.company)

a.show()
b.show()
b.showLanguage()
