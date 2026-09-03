class Animal:
    def eat(self):
        print("Animal is's eating and")

class Dog(Animal):
    def sound(self):
        print("gow gow!! ")
        
d = Dog()
d.eat()
d.sound()