class Animal:
    alive = True

    def eat(self):
        print("This animal is eating!!")

    def sleep(self):
        print("This animal is sleeping!!")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running!")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying!")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print("Rabbit is Alive? "+str(rabbit.alive))
# print("Fish is Alive? "+str(fish.alive))
# print("Hawk is Alive? "+str(hawk.alive))

# fish.eat()
# hawk.sleep()

fish.swim()
hawk.fly()
rabbit.run()
