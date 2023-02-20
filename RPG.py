import sys
import os
import random
import pickle
import items
import enemies
import player
       
Player = player.Player()
factions = ["1. one", "2. two", "3. three"]
startStats = ["1. Rich", "2. Strong", "3. Resilient"]

#Declarations of the classes
ironSword = items.ironSword()
leatherArmor = items.leatherArmor()
goblin = enemies.goblin()
rat = enemies.rat()
peasant = enemies.peasant()
currentEnemy = rat
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
    print("Current Weapon: %s" % Player.curweap)
    print("Health pots: %i\n" % Player.hPots)
    for i in Player.inven:
        #print(i)
        curinv = i
    print("Items in inventory: %s\n" % curinv)
    print("\nBack\n")
    option = input("-->")
    #write code for the rest of possbile items when they're implemented v
    if option == "iron sword" or option == "Iron Sword":
        Player.curweap = "Iron Sword"
        Player.attack = ironSword.attack
        print("You equip the Iron Sword!")
        input("-->")
        inventory()
    if option == "leather armor" or option == "leather armor":
        Player.curarm = "Leather Armor"
        Player.maxHealth = leatherArmor.maxHealth
        print("You equip the leather armor!")
        input("-->")
        inventory()
    if option == "back":
        gameMain()
    if option == "health" or option == "potion" or option == "pot":
        Player.health = Player.maxHealth
        Player.hPots -= 1
        print("You feel healthy and renewed!")
        input("-->")
        inventory()

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
        Player.faction = "two"
        playerStat()
    elif option == "three" or option == "3":
        Player.faction = "three"
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
    global currentEnemy
    currentEnemy.health = currentEnemy.maxHealth
    os.system('cls')
    if Player.health <= 0:
        Player.health = 1
    locations = ["town", 'forest']
    townNear = ['blacksmith', "tailor", 'tavern']
    forestNear = ['witchs home ', ' creek ']
    playerNear = townNear
    print("Location: %s" % Player.loc)
    print("")
    print("Near by: %s" % playerNear)
    print("")
    print("Health: %i / %i" % (Player.health, Player.maxHealth))
    print("")
    print("Gold: %i" % Player.gold)
    print("\n")
    print("what would you like to do?")
    option = input("-->")

    if option in locations:
        if option == "town" or option == "Town":
            playerNear = townNear
            Player.loc = "Town"
            chance = random.randint(1, 10)
            if chance <= 3:
                currentEnemy = rat
                combatTest()
            if chance >= 4:
                gameMain()
            #gameMain()
        elif option == "forest" or option == "Forest":
            playerNear = forestNear
            Player.loc = "Forest"
            chance = random.randint(1, 10)
            if chance <= 3:
                currentEnemy = goblin
                combatTest()
            if chance >= 4:
                gameMain()
            #gameMain()
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
            Tavern()
        elif option == "witchs home" or option == "witch":
            os.system('cls')
            print("This area is not made yet :(")
            input("-->")
            gameMain() #same function as the mayor but different dialog and quests
        elif option == "creek" or option == "Creek":
            os.system('cls')
            print("This area is not made yet :(")
            input("-->")
            gameMain() # add a function for looking around(maybe find items for a quest) and random enemies
        else:
            print("Unknown action")
            input("\nPress any key")
            gameMain()
    if option == "":
        os.system('cls')
        print("\nPlease enter an action\n")
        print("use the help command if you need assistance :)\n")
        input("-->")
        gameMain()
    if option == "help":
        mainhelp()
    if option == "Inventory" or option == "inven" or option == "bag":
        inventory()
    if option == "stats":
        playerStats()
    if option.lower == "save":
        save()
    if option == "help":
        mainhelp()
    if option == "look":
        look()
    if option == "exit":
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
    print("Inventory, bag, inven - access your inventory\n")
    print("stats - Opens up the stat screen\n")
    print("look - Look around you surroundings\n")
    print("town, forest, etc - typing the name of a location will take you there\n")
    print("Save - saves the game\n")
    print("Exit - exits the game\n")
    input("-->")
    gameMain()

def look():
    chance = random.randint(1, 6)
    if chance <= 2:
        gold = random.randint(1,3)
        os.system('cls')
        print("You found %i gold!" % gold)
        Player.gold += gold
        print("Press Enter to continue")
        input('-->')
        gameMain()
    if chance == 3 or chance == 4:
        os.system('cls')
        print("You find nothing")
        print("\nPress Enter to continue")
        input('-->')
        gameMain()
    if chance == 5 or chance == 6:
        global currentEnemy
        os.system('cls')
        enemyChance = random.randint(1,2)
        if enemyChance == 1:
                currentEnemy = rat
        if enemyChance == 2:
                currentEnemy = peasant
        print("You come across a %s!" % currentEnemy.name)
        print("\nWould you like to fight it?    y/n")
        option = input('-->')
        if option == "y" or option == "yes":
            combatTest()
        if option == "n" or option == "no":
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

def playerStats():
    os.system('cls')
    print(Player.name + "'s stats!\n")
    print("Faction: %s\n" % Player.faction)
    print("Max health: %i\n" % Player.maxHealth)
    print("Attack: %i\n" % Player.attack)
    print("\nPress Enter to return\n")
    input('-->')
    gameMain()

def Tavern():
    os.system('cls')
    print("Work in progress")
    input('-->')
    gameMain()

def combatTest():
    os.system('cls')
    print("\n%s has appeared!\n" % currentEnemy.name)
    print("Enemy health: %i\n" % currentEnemy.health)
    print("Your health: %i\n" % Player.health)
    print("What do you want to do?\n")
    option = input('-->')

    if option == "attack":
        hitChance = random.randint(1, 10)
        enemyHitChance = random.randint(1, 10)
        os.system('cls')
        if hitChance <= 7:
            currentEnemy.health -= Player.attack
            print("You hit an enemy for %i damage!\n" % Player.attack)
            if currentEnemy.health <= 0:
                os.system('cls')
                Player.gold += currentEnemy.worth
                print("You have defeated %s!\n" % currentEnemy.name)
                print("You have earned %i gold!\n" % currentEnemy.worth)
                if currentEnemy.dialogue != none:
                    print(currentEnemy.dialogue)
                print("Press Enter to continue")
                input('-->')
                gameMain()
        if hitChance >= 8:
            print("Your attack missed!\n")
        if enemyHitChance <= 5:
            Player.health -= currentEnemy.attack
            print(currentEnemy.name + " has hit you for %i damage!" % currentEnemy.attack)
            if Player.health <= 0:
                os.system('cls')
                Player.gold -= 5
                print("You have died\n")
                print("You have lost some gold\n")
                print("Press Enter to continue")
                input('-->')
                gameMain()
            print("\nPress Enter to continue")
            input('-->')
            combatTest()
        if enemyHitChance >= 6:
            print("%s missed their attack!\n" % currentEnemy.name)
            if currentEnemy.health <= 0:
                os.system('cls')
                Player.gold += currentEnemy.worth
                print("You have defeated %s!\n" % currentEnemy.name)
                print("You have earned %i gold!\n" % currentEnemy.worth)
                if currentEnemy.dialogue != none:
                    print(currentEnemy.dialogue)
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
            print("\nPress Enter to continue")
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
        if chance <= 7:
            print("You were unable to run away!\n")
            input('-->')
            combatTest()
        if chance >= 8:
            print("You have ran away successfully!\n")
            input('-->')
            gameMain()
    
    if currentEnemy.health <= 0:
        os.system('cls')
        Player.gold += currentEnemy.worth
        print("You have defeated %s!\n" % currentEnemy.name)
        print("You have earned %i gold!\n" % currentEnemy.worth)
        if currentEnemy.dialogue != none:
            print(currentEnemy.dialogue)
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
    prices = [" 20 gp "]
    os.system('cls')
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    for i in items:
        print(i)
    for i in prices:
        print(i)
    option = input("-->")
    for i in range(len(items)):
        items[i] = items[i].lower()
    if option in items:
        if option == "iron sword" and Player.gold >= 20:
            os.system('cls')
            Player.gold -= 15
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
    items = ["Leather Armor: 20gp"]
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    for i in items:
        print(i)
    option = input("-->")
    for i in range(len(items)):
        items[i] = items[i].lower()
    
    if option in items:
        if option == "leather armor" or option == "Leather Armor" and Player.gold >= 20:
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
    main()
