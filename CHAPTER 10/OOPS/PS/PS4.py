class Area:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def calculate(self):
        if self.b is None:
            # Square
            return self.a * self.a
        else:
            # Rectangle
            return self.a * self.b
    @staticmethod
    def hello():
        print("Hello there")

a1 = Area(23)
a1.hello()
print("Area of the square is:", a1.calculate())

a2 = Area(23, 89)
print("Area of the rectangle is:", a2.calculate())
