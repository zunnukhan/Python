class Vehicle:
    def __init__(self,max_speed,mileage):

        self.max_speed=max_speed
        self.mileage=mileage

modelx=Vehicle(240,18)
print("Model max speed",modelx.max_speed)
print("Model mileage",modelx.mileage)