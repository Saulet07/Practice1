class Camera:
    def shoot(self):
        print("Photo")

class Phone:
    def call(self):
        print("Calling")

class Smartphone(Camera, Phone):
    pass

sp = Smartphone()
sp.shoot()
sp.call()