from random import randint


class Creature:

    def __init__(self, health, attack, level):
        self.health = health
        self.attack = attack
        self.level = level


class Hero(Creature):
    def __init__(self):
        Creature.__init__(self, randint(170, 280), randint(20, 40), 23)


class Monster(Creature):
    def __init__(self):
        Creature.__init__(self, randint(190, 300), randint(25, 35), 26)


H = Hero()
M = Monster()


def fight():
    count = 0

    while H.health > 0 or M.health > 0:
        H.health = H.health - M.attack
        M.health = M.health - H.attack
        count += 1

    if H.health > M.health:
        return f"The Hero won, he gave {count} times!"
    else:
        return f"The Monster won, he gave {count} times!"


print(fight())
