class Person:
    def speak(self):
        print("Hello")

class Teacher(Person):
    def speak(self):
        print("Good morning")

Teacher().speak()