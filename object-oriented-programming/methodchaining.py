# Method chaining - calling multiple methods sequentially
# Each call perform an action on the same object and returns self

class Car:

    def turn_on(self):
        print("Start the engine!!")
        return self
    def drive(self):
        print("Drive the car!!")
        return self 
    def brake(self):
        print("Step on the brakes!!")
        return self
    def turn_off(self):
        print("Turn off the engine!!")
        return self

car = Car()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()