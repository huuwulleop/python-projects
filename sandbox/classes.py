
class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def talk(self):
        print(f"Hi! My name is {self.name}!")


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


if __name__ == "__main__":
    print("")
    person = Person("Vuong")
    person.talk()
