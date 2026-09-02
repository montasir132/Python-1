class largestNumber:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def largest(self):
        if(self.a > self.b and self.a > self.c):
            return self.a, "largest number"
        elif(self.b> self.a and self.b > self.c ):
            return self.b, "largest number"
        else:
            return self.c, "largest number"
a = int(input("inter your first number:"))
b = int(input("inter your second number:"))
c = int(input("inter your third number:"))
larges_num = largestNumber(a,b,c)
print(larges_num.largest())

