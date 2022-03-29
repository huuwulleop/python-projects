
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass

if __name__ == "__main__":
    dog1 = Dog()
    dog1.walk()
