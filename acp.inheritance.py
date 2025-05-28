class vehicle:
    def __init__(vehicletype):
        print("Vehicles is a ",vehicletype)

class car(vehicle):
    def __init__(self):
        vehicle. __init__("car")
print(issubclass(car,vehicle))
