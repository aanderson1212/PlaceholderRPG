class Player:
    def __init__(self):
        self.name = "temp"
        self.inven = []
        self.hPots = 1
        self.curweap = " "
        self.curarm = " "
        self.gold = 15
        self.faction = " "
        self.attack = 5
        self.health = 30
        self.loc = "Town"
        self.near = "-Blacksmith -Tailor -Tavern"
        self.maxHealth = 30
        self.accuracy = 90
        self.drunk = 0
        
        if self.faction == "one":
            self.attack += 5
        elif self.faction == "two":
            self.maxHealth += 5
        elif self.faction =="three":
            self.accuracy +=5
        
