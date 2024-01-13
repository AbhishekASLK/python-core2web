class Vehicle:
    def __init__(self,brand,model,year,speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        print("accelerate")

    def brake(self):
        print("break")

    def honk(self):
        print("honk")

    def info(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.speed)

class Car(Vehicle):
    def accelerate(self):
        print("accelerate of Car")

    def honk(self):
        print("honk of Car")

v = Vehicle("BMW","X-Series",2024,120.6)
c = Car("Audi","Y-Series",1990,40.6)
v.info()
c.info()
