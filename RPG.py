import sys
import os
import random
import pickle
#from unicodedata import name

#fix all Player variables

#Entity Classes
class Player:
    def __init__(self):
        self.name = "temp"
        self.inven = [""]
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
f = Player()
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
    os.system('cls')
    print("Hello and welcome to this game \n")
    print("1. Start\n")
    print("2. Load\n")
    print("3. Exit\n")
    option = input("-> ")
    if option == "1" or option == "one":
        start()
    elif option == "2" or option == "two":
        if os.path.exists("data.pkl") == True:
            os.system('cls')
            infile = open('data.pkl', 'rb')
            z = pickle.load(infile)
            print ("Loaded Save State...\n")
            Player.name = z
            option = input(' ')
            start1()
        else:
            print("No save data located")
            input("")
            main()
    elif option == "3" or option == "three":
        sys.exit()
    else:
        main()

def inventory():
    playerinv = Player.inven
    os.system('cls')
    print("Type the name of the item to use\n\n")
    print("Items in inventory:\n")
    print("Health pots: %i" % Player.hPots)
    for i in Player.weap:
        print(i)
    #write code for the rest of possbile items when they're implemented
    print("Back")
    option = input("-->")
    if option.lower() == "back":
        start1()

#Character creator (maybe add skill point system?)
def start():
    os.system('cls')
    print ("Hello, what is your name?")
    option = input("--> ")
    Player.name = option
    start1()

#start of the adventure
def start1():
    os.system('cls')
    print(Player.name)
    input("")
    
    

#save the game
def save():
    os.system('cls')
    outfile = open('data.pkl', 'wb')
    pickle.dump(f, outfile)
    outfile.close()
    print ("\nGame has been saved!\n")
    input("Press Enter to continue")
    main()

def shop():

    items = ["Iron Sword", "Leather Armor", "Health Potion"]
    os.system('cls')
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    for i in items:
        print(items)
    option = input("-->")

    if option in items:
        if Player.gold >= items[option]:
            os.system('cls')
            Player.gold -= items[option]
            Player.weap.append(option)
            print ("You have bought %s" % option)
            option = input(' ')
            shop()

        else:
            os.system('cls')
            print ("You don't have enough gold")
            option = input(' ')
            shop()

    elif option == "back":
        start1()
    else:
        os.system('cls')
        print ("That item does not exist")
        option = input(' ')
        shop()

if __name__ == "__main__":
    main()
