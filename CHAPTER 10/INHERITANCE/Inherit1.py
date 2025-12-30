class Employee:
    company = "ITC"

    def show(self):
        print(f"Company: {self.company}")


class Coder:
    language = "Python"

    def printLanguage(self):
        print(f"Programming Language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"Programmer works in {self.company} using {self.language}")


a = Employee()
b = Programmer()

print(a.company, b.company)

a.show()
b.show()
b.printLanguage()
b.showLanguage()
