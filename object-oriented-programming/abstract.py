# Prevents a user from creating an object of Abstract class
# It compels a user to override abstract methods in a child class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod 
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("Drive the car!!")
    
    def stop(self):
        print("Car is stopped!!")

class Motorcycle(Vehicle):
    
    def go(self):
        print("Ride the motorcycle!!")

    def stop(self):
        print("Motorcycle is stopped!!")


# vehicle = Vehicle()
car = Car()

car.go()
car.stop()