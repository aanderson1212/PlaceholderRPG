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
        self.gold = 0
        self.faction = " "
        self.attack = 5
        self.health = 30
        self.loc = [""]
    
        def setName(self, newName):
            self.name = newName
        def addGold(self, moreGold):
            self.gold += moreGold
        def lessGold(self, noGold):
            self.gold -= noGold
        def getWeap(self, weap):
            return self.curweap
        
        if self.faction == "one":
            pass
        elif self.faction == "two":
            pass
        elif self.faction =="three":
            pass
f = Player()
factions = ["1. one", "2. two", "3. three"]
startStats = ["1. Rich", "2. strong", "3. Resilient"]
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
    os.system('cls')
    playerinv = Player.inven
    print("Type the name of the item to use\n\n")
    print("Items in inventory:\n")
    print("Health pots: %i" % Player.hPots)
    for i in Player.weap:
        print(i)
    #write code for the rest of possbile items when they're implemented ^
    print("Back")
    option = input("-->")
    if option.lower() == "back":
        gameMain()

#Character creator (maybe add skill point system?)
def start():
    os.system('cls')
    print ("Hello, what is your name?")
    option = input("--> ")
    Player.name = option
    playerFac()

#start of the adventure
def start1():
    os.system('cls')
    print(Player.name)
    input("")

def playerFac():
    os.system('cls')
    print("Choose your faction:")
    for i in factions:
        print(i)
        print(" ")
    option = input("-->")
    if option == "one" or option == "1":
        Player.faction = "one"
        playerStat()
    elif option == "two" or option == "2":
        Player.faction == "two"
        playerStat()
    elif option == "three" or option == "3":
        Player.faction == "three"
        playerStat()
    else:
        print("Please choose an available faction")
        playerStat()

def playerStat():
    os.system('cls')
    print("Which would descibe you best?")
    for i in startStats:
        print(i)
        print(" ")
    option = input("-->")
    if option == "one" or option == "1":
        Player.gold += 30
        gameStart()
    elif option == "two" or option == "2":
        Player.attack += 10
        gameStart()
    elif option == "three" or option == "3":
        Player.health += 20
        gameStart()
    else:
        print("Please choose from the available traits")
        playerStat()

def gameStart():
    #change list to have the introduction text
    os.system('cls')
    introText = ["a", "b", "c", "d"]
    print(introText[0])
    input("Press Enter -->")
    os.system('cls')
    print(introText[1])
    input("Press Enter -->")
    os.system('cls')
    print(introText[2])
    input("press Enter -->")
    os.system('cls')
    print(introText[3])
    input("Press Enter to enter the world")
    gameMain()
    
def gameMain():
    locations = ['town', 'forest']
    townNear = ['blacksmith', 'tailor', 'mayor']
    forestNear = [' witchs home ', ' creek ']
    playerNear = townNear
    os.system('cls')
    print(Player.loc"\n")
    print(Player.health"\n")
    print(Player.gold"\n")
    print("\n\n")
    print("Near by: " + playerNear)
    print("what would you like to do?")
    option.lower = input("-->")
    if option in locations:
        if option == "town":
            playerNear = townNear
            Player.loc = "Town"
            gameMain()
        elif option == "forest":
            playerNear = forestNear
            Player.loc = "Forest"
            gameMain()
        else:
            print("Unknown action")
            input("\nPress any key")
            gameMain()
    if option in playerNear: #for shops just copy and change the shop()
        if option == "blacksmith":
            pass
        elif option == "tailor":
            pass
        elif option == "mayor":
            pass #add a function for talking to and maybe getting quests from the mayor
        elif option == "witchs home" or option == "witch":
            pass #same function as the mayor but different dialog and quests
        elif option == "creek":
            pass # add a function for looking around(maybe find items for a quest) and random enemies
        else:
            print("Unknown action")
            input("\nPress any key")

    if option == "inventory" or "inven" or "bag"
        inventory()
    if option == "save":
        save()


#save the game
def save():
    os.system('cls')
    outfile = open('data.pkl', 'wb')
    pickle.dump(f, outfile)
    outfile.close()
    print ("\nGame has been saved!\n")
    print("\nExit game? y/n\n")
    option.lower = input("-->")
    if option == "yes" or "y":
        sys.exit()
    elif option == "no" or "n":
        gameMain()

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
            option = input('-->')
            shop()

    elif option == "back":
        start1()
    else:
        os.system('cls')
        print ("That item does not exist")
        option = input('-->')
        shop()

if __name__ == "__main__":
    main()
