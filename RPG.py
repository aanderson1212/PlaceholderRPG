import sys
import os
import random
import pickle



#Entity Classes
class Player:
    def __init__(self, Hname, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hhealth, pGold):
        inven = [""]
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.gold = pGold
        self.hPots = 0
        self.weap = ["Bread Knife"]
        self.curweap = ["Bread Knife"]
    
        def setName(self, newName):
            self.name = newName
        def addGold(self, moreGold):
            self.gold += moreGold
        def lessGold(self, noGold):
            self.gold -= noGold
        def getWeap(self, weap):
            return self.curweap

class Goblin():
    def __init__(self):
        self.health = 100
        self.attack = 5
    #get statements
    def getHealth(self, health):
        return self.health
    def getAttack(self, attack):
        return self.attack
    #set statements
    def setHealth(self, newHealth):
        self.health = newHealth

class Rat():
    def __init__(self):
        self.health = 10
        self.attack = 1
    #get statements
    def getHealth(self, health):
        return self.health
    def getAttack(self, attack):
        return self.attack
    #set statements
    def setHealth(self, newHealth):
        self.health = newHealth

#Start of game code
def main():
    os.system('clear')
    print("Hello and welcome to this game \n")
    print("1. Start\n")
    print("2. Load\n")
    print("3. Exit\n")
    option = raw_input("-> ")
    if option == "1" or option == "one":
        start()
    elif option == "2" or option == "two":
        if os.path.exists("savefile") == True:
            os.system('clear')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print ("Loaded Save State...")
            option = raw_input(' ')
            start1()
    elif option == "3" or option == "three":
        sys.exit()
    else:
        main()

def inventory():
    player = Player()
    os.system('clear')
    print("Type the name of the item to use\n\n")
    print("Items in inventory:\n")
    print("Health pots: %i" % PlayerIG.hPots)
    for i in PlayerIG.weap:
        print(weap)
    #write code for the rest of possbile items when they're implemented
    print("Back")
    option = raw_input("-->")
    if option.lower() == "back":
        start1()

#Character creator (maybe add skill point system?)
def start():
    os.system('clear')
    print ("Hello, what is your name?")
    option = raw_input("--> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()

#start of the adventure
def start1():
    print("Start1")

#save the game
def save():
    os.system('clear')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print ("\nGame has been saved!\n")
        option = raw_input(' ')
        start1()

def shop():
    items = ["Iron Sword", "Leather Armor", "Health Potion"]
    os.system('clear')
    print "Welcome to the shop!"
    print "\nWhat would you like to buy?\n"
    for i in items:
        print(items)
    option = raw_input("-->")

    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            os.system('clear')
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print ("You have bought %s" % option)
            option = raw_input(' ')
            store()

        else:
            os.system('clear')
            print ("You don't have enough gold")
            option = raw_input(' ')
            store()

    elif option == "back":
        start1()
    else:
        os.system('clear')
        print ("That item does not exist")
        option = raw_input(' ')
        store()

if __name__ == "__main__":
    main()