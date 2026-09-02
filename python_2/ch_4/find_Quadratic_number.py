import math

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def roots(self):
        if self.a == 0:
            return "Not a quadratic equation"

        d = self.b**2 - 4 * self.a * self.c

        if d == 0:
            return -self.b / (2 * self.a)

        elif d > 0:
            return (
                (-self.b + math.sqrt(d)) / (2 * self.a),
                (-self.b - math.sqrt(d)) / (2 * self.a)
            )

        else:
            return "No real roots"


a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))

print(Quadratic(a, b, c).roots())