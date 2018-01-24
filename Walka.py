# -*- coding: utf-8 -*-

#    Some heroes
#    A way to perform automatic fight sequence until one of heroes is dead
#    Heroes may want to have some very basic stats (health, agility, strength) and skills (dodge, block)
#    Heroes may want to be able to use some items that influence stats
from warriors import Warrior
from random import randint


class Walka(object):

    def walka(self, attacker, defender):
        turn = 1  # licznik tur
        # walka, wymiana ciosów do smierci

        while attacker.is_alive and defender.is_alive:
            print("%s turn." % turn)
            attacker, defender = defender, attacker
            self.uderzenie(attacker, defender)
            turn += 1
            if turn > 100:
                return

    def arena(self, attacker, defender):  # funkcja glowna
        print ("Fight between %s and %s !" % (attacker.name, defender.name))
        self.walka(attacker, defender)
        print ("Zwyciężca = %s !" % (self.wygrany(attacker, defender)))
        return True

    def uderzenie(self, attacker, defender):  # atak wojownika attacker
        block = defender.calculate_block()  # szansa na blok
        dodge = defender.calculate_dodge()  # szansa na unik
        hit = attacker.calculate_hit(dodge)
        damage = attacker.calculate_dmg()

        if hit > dodge:
            if block > hit / 1.5:
                defender.recieve_damage(damage / 2)
                print("%s blocked the hit for half damage! ( %s hp)" % (defender.name, defender.hp))

            else:
                defender.recieve_damage(damage)
                print ("%s got hit! ( %s hp)" % (defender.name, defender.hp))
        else:
            print("%s dodged!" % defender.name)

    def wygrany(self, attacker, defender):  # zwraca imie wygranego
        if attacker.hp > defender.hp:
            return attacker.name
        else:
            return defender.name


fight_inst = Walka()
fight_inst.arena(Warrior('a'), Warrior('b'))
