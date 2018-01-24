#    Some heroes
#    A way to perform automatic fight sequence until one of heroes is dead
#    Heroes may want to have some very basic stats (health, agility, strength) and skills (dodge, block)
#    Heroes may want to be able to use some items that influence stats
#    Jakies cos
from random import randint
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

    def recieve_damage(self, damage):
        damage = damage - self.backpack["armor"]
        if damage >= 0:
            self.hp -= damage

    def calculate_dmg(self):
        return self.strength + self.backpack["weapon"]

    def calculate_hit(self, dodge_value):
        return self.agility - dodge_value + randint(0, 75)

    def calculate_dodge(self):
        return self.dodge + self.backpack["boots"]

    def calculate_block(self):
        return self.block + self.backpack["shield"]

    @property
    def is_alive(self):
        return self.hp > 0

    def __repr__(self):
        return '<Warrior name={}>'.format(self.name)

ziutek = Warrior('wiran')
