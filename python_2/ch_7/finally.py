try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input")
else:
    print(age)
finally:
    print("End The code")