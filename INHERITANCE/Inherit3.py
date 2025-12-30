class Employee:
    company = "ITC"

    def show(self):
        print(f"Company: {self.company}")


class Coder(Employee):
    language = "Python"

    def printLanguage(self):
        print(f"Company: {self.company} Programming Language: {self.language}")


class Programmer(Employee):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"Programmer works in {self.company}")


a = Employee()
b = Programmer()
c = Coder()

print(a.company, b.company)

a.show()

b.show()
b.showLanguage()

c.show()
c.printLanguage()
