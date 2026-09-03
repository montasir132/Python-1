try:
    a = int(input("Enter a value 1st:"))
    b = int(input("Enter a value 2nd:"))
    result = a/b
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print(result)
finally:
    print("program end")