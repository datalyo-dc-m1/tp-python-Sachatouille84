class Monkey:
    def __init__(self, name):
        self.name = name
    def eat(self, banana):
        print(self.name, 'a mangé une banane', banana.color)
    def reproduction(self, monkey, enfant):
        print(self.name, " et ", monkey.name, " reproduisent ", enfant.name)

class Banana:
    def __init__(self, color):
        self.color = color

class Enfant:
    def __init__(self, name):
        self.name = name


pierre = Monkey("Pierre")
marie = Monkey("Marie")
robert = Enfant("Robert")
banane_jaune = Banana("Jaune")
banane_verte = Banana("Verte")

pierre.eat(banane_jaune)
marie.eat(banane_verte)
pierre.reproduction(marie, robert)