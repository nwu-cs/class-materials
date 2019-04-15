class Vehicle():
    def __init__(self, name="", wheels = 4, l=0, w=0, h=0):
        self.wheels = wheels
        self.length = l
        self.height = h
        self.width = w
        self.name = name

    def __str__(self):
        return "%s" % self.name

    def set_dim(self,l=0,w=0,h=0):
        self.length = l
        self.height = h
        self.width = w

    def __repr__(self):
        return str(self)


class Bike(Vehicle):
    def __init__(self,name="bike", wheels = 2, l=0, w=0, h=0):
        super().__init__(name,wheels,l,w,h)

class PedalBike(Bike):
    def __init__(self,name="pedalbike", wheels = 2, l=0, w=0, h=0):
        super().__init__(name,wheels,l,w,h)

class MotorCycle(Bike):
    def __init__(self,name="motorcycle", wheels = 2, l=0, w=0, h=0):
        super().__init__(name,wheels,l,w,h)

class Car(Vehicle):
    def __init__(self,name="car", wheels = 4, l=0, w=0, h=0):
        super().__init__(name,wheels,l,w,h)

class Convertible(Car):
    def __init__(self,name="convertible", wheels = 4, l=0, w=0, h=0):
        super().__init__(name,wheels,l,w,h)

class Pickup(Car):
    def __init__(self,name="pickup", wheels = 4, l=0, w=0, h=0):
        super().__init__(name,wheels,l,w,h)

class Bus(Vehicle):
    def __init__(self,name="bus", wheels = 4, l=0, w=0, h=0):
        super().__init__(name,wheels,l,w,h)
