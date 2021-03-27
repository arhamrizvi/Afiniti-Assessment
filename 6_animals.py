
class Animals:
    def __init__(self,name):
        self.name = name

    def whoami(self):
        return self.name

    def speak(self):
        return "The animal refuses to speak"


class Cat(Animals):
    def speak(self):
        return "Meow!"


class Dog(Animals):
    def speak(self):
        return "Woof!"


class Fish(Animals):
    pass


if __name__=='__main__':

    animals = []

    dog = Dog("Rover")
    cat = Cat("Hank")
    fish = Fish("Fred")

    animals.append(dog)
    animals.append(cat)
    animals.append(fish)

    for item in animals:
        print("This animal's name is "+item.name)
        if item.speak():
            print(item.speak())
