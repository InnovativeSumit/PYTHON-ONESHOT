class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


class Name:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        return self.text + " " + other.text


n1 = Name("Sumit")
n2 = Name("Pal")

print(n1 + n2)
