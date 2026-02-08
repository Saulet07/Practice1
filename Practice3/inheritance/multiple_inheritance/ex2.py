class Fly:
    def fly(self):
        print("Fly")

class Swim:
    def swim(self):
        print("Swim")

class Duck(Fly, Swim):
    pass

Duck().fly()
Duck().swim()