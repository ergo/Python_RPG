#    Some heroes
#    A way to perform automatic fight sequence until one of heroes is dead
#    Heroes may want to have some very basic stats (health, agility, strength) and skills (dodge, block)
#    Heroes may want to be able to use some items that influence stats
#    Jakies cos

import sys

print sys.version_info


class Warrior(object):
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.agility = 10
        self.hp = 100
        self.block = 10
        self.dodge = 10
        self.backpack = {"weapon": 4, "armor": 2, "boots": 5, "shield": 4}


warrior1 = Warrior(name='Wiran')

