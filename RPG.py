from math import comb
from operator import inv
import sys
import os
import random
import pickle
import logging

from pytest import Item
#from unicodedata import name

#fix all Player variables

#Entity Classes
class Player:
    def __init__(self):
        self.name = "temp"
        self.inven = []
        self.hPots = 0
        self.curweap = ""
        self.curarm = ""
        self.gold = 15
        self.faction = " "
        self.attack = 5
        self.health = 30
        self.loc = "Town"
    
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

        #Statements for the equipped items vv
        if self.curweap == "iron sword":
            self.attack += 4
        if self.curarm == "leather armor":
            self.health += 3
Player = Player()
factions = ["1. one", "2. two", "3. three"]
startStats = ["1. Rich", "2. strong", "3. Resilient"]
class Goblin():
    def __init__(self):
        self.health = 100
        self.attack = 5
        self.worth = 10
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
        self.name = "Rat"
        self.health = 10
        self.attack = 1
        self.worth = 2
    #get statements
    def getHealth(self, health):
        return self.health
    def getAttack(self, attack):
        return self.attack
    #set statements
    def setHealth(self, newHealth):
        self.health = newHealth
goblin = Goblin()
rat = Rat()
currentEnemy = Rat()
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
    curinv = ' '
    playerinv = Player.inven
    print("Type the name of the item to use\n\n")
    print("Health pots: %i\n" % Player.hPots)
    for i in Player.inven:
        #print(i)
        curinv = i
    print("Items in inventory: %s\n" % curinv)
    print("\nBack\n")
    option = input("-->")
    #write code for the rest of possbile items when they're implemented v
    if option == "Iron Sword":
        Player.curweap = "iron sword"
    if option == "Leather Armor":
        Player.curarm = "leather armor"
    if option == "back":
        gameMain()

#Character creator (maybe add skill point system?)
def start():
    os.system('cls')
    print ("Hello, what is your name?")
    option = input("--> ")
    Player.name = option
    playerFac()

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
    os.system('cls')
    locations = ["town", 'forest']
    townNear = ['blacksmith', "tailor", 'tavern']
    forestNear = [' witchs home ', ' creek ']
    playerNear = townNear
    print("Location: %s" % Player.loc)
    print("")
    print("Near by: %s" % playerNear)
    print("")
    print("Health: %i" % Player.health)
    print("")
    print("Gold: %i" % Player.gold)
    print("\n")
    print("what would you like to do?")
    option = input("-->")

    if option in locations:
        if option == "town" or option == "Town":
            playerNear = townNear
            Player.loc = "Town"
            gameMain()
        elif option == "forest" or option == "Forest":
            playerNear = forestNear
            Player.loc = "Forest"
            gameMain()
        else:
            print("Unknown action")
            input("\nPress any key")
            gameMain()
    if Player.loc == "Town":
        playerNear = townNear
    if Player.loc == "Forest":
        playerNear = forestNear
    if option in playerNear: #for shops just copy and change the shop()
        if option == "blacksmith" or option == "Blacksmith":
            blacksmith()
        elif option == "tailor" or option == "Tailor":
            tailor()
        elif option == "tavern" or option == "Tavern":
            pass #add a function for talking to and maybe getting quests from the mayor
        elif option == "witchs home" or option == "witch":
            pass #same function as the mayor but different dialog and quests
        elif option == "creek" or option == "Creek":
            pass # add a function for looking around(maybe find items for a quest) and random enemies
        else:
            print("Unknown action")
            input("\nPress any key")
            gameMain()
    if option == " ":
        os.system('cls')
        print("\nPlease enter an action\n")
        print("use the help command if you need assistance :)\n")
        input("-->")
        gameMain()
    if option == "help":
        mainhelp()
    if option == "Inventory" or option == "inven" or option == "bag":
        inventory()
    if option.lower == "save":
        save()
    if option == "help":
        mainhelp()
    if Player.loc == "Town":
        playerNear = townNear
    if Player.loc == "Forest":
        playerNear = forestNear 
    if option == "exit" or option == "Exit":
        os.system('exit')
    else:
        os.system('cls')
        print("\nLocation or action not found\n")
        print("Press enter to continue\n")
        print("Note: many of the locations are case sensitive, this will hopefully be patched")
        input("-->")
        gameMain()
        
def mainhelp():
    os.system('cls')
    print("Commands: \n")
    print("Inventory, bag, inven - access your inventory")
    print("Save - saves the game")
    print("Exit - exits the game")
    input("-->")
    gameMain()

#save the game
def save():
    os.system('cls')
    outfile = open('data.pkl', 'wb')
    pickle.dump(Player, outfile)
    outfile.close()
    print ("\nGame has been saved!\n")
    print("\nExit game? y/n\n")
    option = input("-->")
    if option.lower == "yes" or "y":
        sys.exit()
    elif option.lower == "no" or "n":
        gameMain()

def combatTest():
    os.system('cls')
    print("\n%s has appeared!\n" % currentEnemy.name)
    print("Enemy health: %i\n" % currentEnemy.health)
    print("Your health: %i\n" % Player.health)
    print("What do you want to do?\n")
    option = input('-->')

    if option == "attack":
        os.system('cls')
        currentEnemy.health -= Player.attack
        Player.health -= currentEnemy.attack
        print("You hit and enemy for %i damage!\n" % Player.attack)
        print(currentEnemy.name + " has hit you for %i damage!" % currentEnemy.attack)
        if currentEnemy.health <= 0:
            os.system('cls')
            Player.gold += currentEnemy.worth
            print("You have defeated %s!\n" % currentEnemy.name)
            print("You have earned %i gold!\n" % currentEnemy.worth)
            print("Press Enter to continue")
            input('-->')
            gameMain()
        if Player.health <= 0:
            os.system('cls')
            Player.gold -= 5
            print("You have died\n")
            print("You have lost some gold\n")
            print("Press Enter to continue")
            input('-->')
            gameMain()
            input('-->')
            combatTest()
        input("-->")
        combatTest()
    if option == "block":
        os.system('cls')
        print("You have blocked the enemy attack!\n")
        input('-->')
        combatTest()
    if option == "flee" or option == "run":
        os.system('cls')
        chance = random.randint(1, 10)
        if chance <= 6:
            print("You were unable to run away!\n")
            input('-->')
            combatTest()
        if chance >= 5:
            print("You have ran away successfully!\n")
            input('-->')
            gameMain()
    
    if currentEnemy.health <= 0:
        os.system('cls')
        Player.gold += currentEnemy.worth
        print("You have defeated %s!\n" % currentEnemy.name)
        print("You have earned %i gold!\n" % currentEnemy.worth)
        print("Press Enter to continue")
        input('-->')
        gameMain()
    if Player.health <= 0:
        os.system('cls')
        Player.gold -= 5
        print("You have died\n")
        print("You have lost some gold\n")
        print("Press Enter to continue")
        input('-->')
        gameMain()

def blacksmith():

    items = ["Iron Sword"]
    os.system('cls')
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    for i in items:
        print(i)
    option = input("-->")
    for i in range(len(items)):
        items[i] = items[i].lower()
    if option in items:
        if option == "iron sword" or option == "Iron Sword" and Player.gold >= 15:
            os.system('cls')
            Player.gold - 15
            Player.inven.append("Iron Sword")
            print ("You have bought %s!" % option)
            print("\nPress Enter to continue")
            option = input('-->')
            blacksmith()

        else:
            os.system('cls')
            print ("You don't have enough gold")
            option = input('-->')
            blacksmith()

    elif option == "back":
        gameMain()
    else:
        os.system('cls')
        print ("That item does not exist")
        print("\nYou may need to spell the item exactly as presented")
        option = input('-->')
        blacksmith()

def tailor():
    os.system('cls')
    items = ["Leather Armor"]
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    for i in items:
        print(i)
    option = input("-->")
    for i in range(len(items)):
        items[i] = items[i].lower()
    
    if option in items:
        if option == "leather Armor" or option == "Leather armor" and Player.gold >= 20:
            os.system('cls')
            Player.gold -= 20
            Player.weap.append(option)
            print ("You have bought %s!" % option)
            option = input(' ')
            tailor()

        else:
            os.system('cls')
            print ("You don't have enough gold")
            option = input('-->')
            tailor()

    elif option == "back":
        gameMain()
    else:
        os.system('cls')
        print ("That item does not exist")
        option = input('-->')
        tailor()

if __name__ == "__main__":
    combatTest()
