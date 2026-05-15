from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, speed):
        self._brand = brand
        self.__speed = speed

    # Encapsulation (getter & setter)
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed

    # Abstract method
    @abstractmethod
    def move(self):
        pass


# Inheritance
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    # Polymorphism (method override)
    def move(self):
        return f"{self._brand} Car is driving on road 🚗"


class Plane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude

    def move(self):
        return f"{self._brand} Plane is flying in sky ✈️"


# Polymorphism in action
def vehicle_status(vehicle):
    print(vehicle.move())
    print("Speed:", vehicle.get_speed())
    print("-" * 30)


# Main program
car = Car("Toyota", 120, "Petrol")
plane = Plane("Boeing", 900, 30000)

vehicle_status(car)
vehicle_status(plane)