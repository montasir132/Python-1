import math
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your third number : "))
class Triangle_area:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        if(self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b):
            s = (self.a + self.b + self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        else: return "It's not a triangle"


# areaOfTriangle = Triangle_area(a,b,c)
print(Triangle_area(a,b,c).area())