# -*- coding: utf-8 -*-

#    Some heroes
#    A way to perform automatic fight sequence until one of heroes is dead
#    Heroes may want to have some very basic stats (health, agility, strength) and skills (dodge, block)
#    Heroes may want to be able to use some items that influence stats
from warriors import Warrior
from random import randint


def walka(char1, char2):
    turn = 1;  # licznik tur
    while True:
        # walka, wymiana ciosów do smierci
        print("%s turn." % turn)
        uderzenie(char1, char2)
        if char1.hp <= 0 or char2.hp <= 0:
            break
        uderzenie(char2, char1)
        if char1.hp <= 0 or char2.hp <= 0:
            break
        turn += 1


def arena(char1, char2):  # funkcja glowna
    print ("Fight between %s and %s !" % (char1.name, char2.name))
    walka(char1, char2)
    print ("Zwyciężca = %s !" % (wygrany(char1, char2)))
    return True


def uderzenie(char1, char2):  # atak wojownika char1
    hit = char1.agility + randint(0, 75)  # szansa na trafienie
    damage = char1.backpack["weapon"] + char1.strength - char2.backpack["armor"]  # obrazenia
    block = char2.block + char2.backpack["shield"]  # szansa na blok
    dodge = char2.dodge + char2.backpack["boots"]  # szansa na unik

    if hit > dodge:
        if block > hit / 1.5:
            char2.hp -= damage / 2
            print("%s blocked the hit for half damage! ( %s hp)" % (char2.name, char2.hp))

        else:
            char2.hp -= damage
            print ("%s got hit! ( %s hp)" % (char2.name, char2.hp))
    else:
        print("%s dodged!" % char2.name)


def wygrany(char1, char2):  # zwraca imie wygranego
    if char1.hp > char2.hp:
        return char1.name
    else:
        return char2.name


arena(Warrior('a'), Warrior('b'))
