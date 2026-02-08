class Read:
    def read(self):
        print("Reading")

class Write:
    def write(self):
        print("Writing")

class Student(Read, Write):
    pass

s = Student()
s.read()
s.write()