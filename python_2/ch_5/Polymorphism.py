class Cat:
    def sound(self):
        print("cat says meow meow...")
class Bird:
    def sound(self):
        print("bird says Kockcuruku...")
class Dog:
    def sound(self):
        print("Dog says Gaew gaew...")

for animal in [Cat(),Bird(),Dog()]:
    animal.sound()