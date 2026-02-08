class Device:
    def on(self):
        print("Device on")

class Laptop(Device):
    def on(self):
        print("Laptop on")

Laptop().on()