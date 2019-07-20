import random

colors = ["Black","Blue","Green","Red","White"]
mechanics = ["Spells","Amass","Hexproof","Mill"
            ,"Self-Mill","Deathtouch","Lifelink"
            ,"*Strike","Instant/Flash/Haste"
            ,"Flying","Trample","Vigilance"
            ,"Kicker","Convoke","Menace"
            ,"Afterlife","Ascend","Proliferate"
            ,"Mentor","Riot","Spectacle"]
creature = ["Sphinx","Pirate","Dragon","Merfolk"
            ,"Human","Zombie","Vampire","Spirit"
            ,"Elemental","Dinosaur","Beast","Angel"
            ,"Knight","Cleric","Wizard","Shaman"
            ,"Demonic","Horror","Insect","Orc"
            ,"Assassin","Fungus","Artifact"
            ,"Goblin","Wall","Elf"]

def RandomColor():
    index = random.randint(0,len(colors)-1)
    return colors[index]

def RandomMechanic():
    index = random.randint(0,len(mechanics)-1)
    return mechanics[index]

def RandomCreautre():
    index = random.randint(0,len(creature)-1)
    return creature[index]

def ColorOrOther():
    magicnumber = random.randint(1,10)
    if magicnumber % 2 == 0:

        return "Color"

    else:
        mNumber2 = random.randint(1,10)

        if mNumber2 % 2 == 0:

            return "Mechanic"

        else:

            return "Creature"

def CheckForDupe(nItem,array):

    for item in array:

        if (nItem == item):

            return True

    return False

def GetColors():

    numColors = random.randint(1,5)

    colorList = []

    if numColors == 5:

        return "Prismatic"
    
    else:

        if numColors != 1:
            
            colorList.append(RandomColor())
            numColors = numColors - 1

            while numColors != 0:

                color = RandomColor()
                if (not CheckForDupe(color,colorList)):

                    numColors = numColors - 1
                    colorList.append(color)

            return colorList

        else:

            return RandomColor()

def Main():

    choice = ColorOrOther()

    Rules()

    print("You will be playing deck type: " + choice)
    print("Requirements: ")

    if choice == "Color":
        
        choiceList = GetColors()

        if type(choiceList) is list:

            for color in choiceList:
                print("    " + color)

        else:

            print("    " + choiceList)

    elif choice == "Mechanic":

        choiceList = RandomMechanic()

        print("    " + choiceList)

    elif choice == "Creature":

        choiceList = RandomCreautre()

        print("    " + choiceList)

    input("Press any key to continue...")

def Rules():
    print("The rules are simple")
    print("1. The randomizer will run and select either a color combo,\n    a mechanic type,\n    or creature type\n    and you must build a deck around what is chosen")
    print("2. Deck choices will be made without the others knowledge to prevent building against the other person\n")


Main()