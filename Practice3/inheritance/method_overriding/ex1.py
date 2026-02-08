class Animal:
    def sound(self):
        print("Animal")

class Cat(Animal):
    def sound(self):
        print("Meow")

Cat().sound()