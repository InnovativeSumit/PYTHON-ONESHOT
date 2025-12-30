class Employee:
    def __init__(self, company):
        self.company = company
        print("Employee constructor called")

    def show(self):
        print(f"Company: {self.company}")


class Coder(Employee):
    def __init__(self, company, language):
        super().__init__(company)   # Call Employee constructor
        self.language = language
        print("Coder constructor called")

    def printLanguage(self):
        print(f"Programming Language: {self.language}")


class Programmer(Coder):
    def __init__(self, company, language, level):
        super().__init__(company, language)  # Call Coder constructor
        self.level = level
        print("Programmer constructor called")

    def showLanguage(self):
        print(
            f"{self.level} Programmer works in {self.company} using {self.language}"
        )



p = Programmer("ITC Infotech", "Python", "Senior")
p.show()
p.printLanguage()
p.showLanguage()
