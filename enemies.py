class goblin():
    def __init__(self):
        self.name = "Goblin"
        self.health = 20
        self.attack = 5
        self.worth = 10
        self.maxHealth = 20

class rat():
    def __init__(self):
        self.name = "Rat"
        self.health = 10
        self.attack = 1
        self.worth = 2
        self.maxHealth = 10

class peasant():
    def __init__(self):
        self.name = "Defenseless Peasant"
        self.health = 20
        self.attack = 0
        self.worth = 5
        self.maxHealth = 20
        self.died = dialogue("Ohhh I'm dead!")
        def dialogue(dName):
            print(dName)

