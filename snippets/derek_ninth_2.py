import random
import math


class Warrior(object):
    def __init__(self, name="Warrior", health=0, attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        attackAmount = self.attackMax * (random.random() * 0.5)
        return attackAmount

    def block(self):
        blockAmount = self.blockMax * (random.random() * 0.5)
        return blockAmount


class Battle(object):
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print "Game Over"
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print "Game Over"
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttackAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        damage2WarriorB = math.ceil(warriorAAttackAmt - warriorBBlockAmt)
        warriorB.health -= damage2WarriorB
        print "{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB)
        print "{} is down to {} health".format(warriorB.name, warriorB.health)
        if warriorB.health <= 0:
            print "{} has died and {} is VICTORIOUS".format(warriorB.name, warriorA.name)
            return "Game Over"

        else:
            return "Fight Again"


def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Glaxon", 50, 20, 10)
    battle = Battle()
    battle.startFight(maximus, galaxon)


main()
