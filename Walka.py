#    Some heroes
#    A way to perform automatic fight sequence until one of heroes is dead
#    Heroes may want to have some very basic stats (health, agility, strength) and skills (dodge, block)
#    Heroes may want to be able to use some items that influence stats

from Postacie import gladiators
from random import randint


def walka(char1,char2):

    while char1["health"] > 0 and char2["health"] > 0:
        uderzenie(char1,char2)


def arena(char1,char2):
    print ("Fight between %s and %s !" % (char1["name"], char2["name"]))
    return True


def uderzenie(char1,char2):
    hit_chance1 = char1["agility"] + randint(0,100)
    dodge_chance1 = char1["dodge"] + randint(0,25)
    block_chance1 = char1["block"] + randint(0,25)
    hit_chance2 = char1["agility"] + randint(0,100)
    dodge_chance2 = char1["dodge"] + randint(0,25)
    block_chance2 = char2["block"] + randint(0,25)

    if hit_chance1-dodge_chance2 > hit_chance2-dodge_chance1:
        if block_chance2 > hit_chance1/2:
            print("%s blocked the hit and lost %s health!" % (char2["name"], (char1["strength"]/2)))
            char2["health"] -= (char1["strength"]/2)
            print ("%s has %s health left!" % (char2["name"],char2["health"]))
        else:
            print("%s got hit for %s!" % (char2["name"],char1["strength"]))
            char2["health"]-= char1["strength"]
            print ("%s has %s health left!" % (char2["name"],char2["health"]))
    if hit_chance1-dodge_chance2 < hit_chance2-dodge_chance1:
        if block_chance1 > hit_chance2/2:
            print("%s blocked the hit and lost %s health!" % (char1["name"], (char2["strength"]/2)))
            char1["health"] -= (char2["strength"]/2)
            print ("%s has %s health left!" % (char1["name"],char1["health"]))
        else:
            print("%s got hit for %s!" % (char1["name"],char2["strength"]))
            char1["health"]-= char2["strength"]
            print ("%s has %s health left!" % (char1["name"],char1["health"]))


arena(gladiators[0],gladiators[1])