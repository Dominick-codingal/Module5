class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.milage = mileage
        
class Bus(vehicle):
    pass
School_bus = Bus(" school Scania", 180, 10) 
print("vehicle Name: ", School_bus.name, " .Speed: ", School_bus.max_speed, "mileage: ", School_bus.milage)       