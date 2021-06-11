import time


class CharactersFeatures:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.health = 100

    def show_stats(self):
        discretion = (f'name: {self.name}, level: {self.level}, health: {self.health}, agility: {self.agility}, '
                      f'stamina: {self.stamina}, intellect: {self.intellect}, strength: {self.damage}'.title())
        print(discretion)

    def move(self, direction):
        self.direction = direction
        if self.direction == 'forward':
            print(f'{self.name} going forward')
        elif self.direction == 'back':
            print(f'{self.name} going back')
        elif self.direction == 'right':
            print(f'{self.name} going back')
        elif self.direction == 'left':
            print(f'{self.name} going left')

    def level_up(self):
        self.level += 1


class Monster(CharactersFeatures):
    def __init__(self, name, type_of_creature, level=1, age='unknown'):
        super().__init__(name, age)
        self.level = level
        self.type_of_creature = type_of_creature
        self.health = 120
        self.intellect = 4
        self.damage = 12
        self.stamina = 13
        self.agility = 6
        #print(f'Name: {name} , Type: {type_of_creature}, Level: {level}, Age: {age}')

    def level_up(self):
        self.level += 1
        self.health += 17
        self.agility += 2
        self.stamina += 3
        self.damage += 4
        self.intellect += 1

    def roar(self):
        return print(f'{self.name} makes ROOOOAAARRR')


class Hero(CharactersFeatures):

    def __init__(self, name, age, race, level=1):
        super().__init__(name, age)
        self.race = race
        self.health = 140
        self.intellect = 8
        self.damage = 10
        self.stamina = 10
        self.agility = 8
        self.level = level
        # print(f'Name: {name} , Age: {age}, Race: {race} Level: {level}')

    def level_up(self):
        self.level += 1
        self.health += 15
        self.agility += 4
        self.stamina += 1
        self.damage += 3
        self.intellect += 3

    def get_health(self):
        return self.health

    def speak(self):
        return 'Hello fella'


def fight(hero_damage, hp_hero, monster_damage, hp_monster):
    while hp_hero != 0 or hp_monster != 0:
        for i in range(100):
            hp_monster -= hero_damage
            if hp_monster > 0:
                hp_hero -= monster_damage
                time.sleep(0.5)
                print(f"Monster have {hp_monster} health points after your damage")
            if hp_monster > 0 and hp_hero < 0:
                time.sleep(0.5)
                return print("monster won")
            elif hp_monster < 0 and hp_hero > 0:
                time.sleep(0.5)
                print(f"Monster have 0 health")
                return print(f"You WON!!!!")
