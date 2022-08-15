import sys
import os
import random
import pickle

#SAVE STATE CODE (cannot yet be implemented)
#os.system('clear')
#        with open('savefile', 'wb') as f:
#            pickle.dump(PlayerIG, f)
#            print "\nGame has been saved!\n"
#        option = raw_input(' ')
#        start1()


class Player:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname

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

def main():
    os.system('clear')
    print("Hello and welcome to this game \n")
    print("1. Start\n")
    print("2. Load\n")
    print("3. Exit\n")
    option = raw_input("-> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('clear')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print "Loaded Save State..."
            option = raw_input(' ')
            start1()
    elif option == "3":
        sys.exit()
    else:
        main()

def start():
    pass

def start1():
    pass
