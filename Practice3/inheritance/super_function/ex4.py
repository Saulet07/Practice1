class Phone:
    def info(self):
        print("Phone")
class Smartphone(Phone):
    def info(self):
        super().info()
        print("Smartphone")
Smartphone().info()