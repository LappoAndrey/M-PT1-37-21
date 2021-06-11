import time
from random import *
from Room import *
from Door import *
from Hero import *
from time import *
delay = 0.5

def catacombs():
    print('you are in the catacombs')


def old_museum():
    print('you are in the old museum')


def fire_room():
    print('you are in the fire room')


def stinky_room():
    print('you are in the stinky room,the worst one')


class Maze:
    def __init__(self, numb_of_rooms):
        self.hero = None
        self.rooms = []
        self.doors = []
        self.numb_of_rooms = numb_of_rooms
        i = 0
        list_of_rooms = []
        while i < numb_of_rooms:
            for j in range(numb_of_rooms):
                list_of_rooms.append(f'room {j + 1}')
                i += 1
        self.rooms = list_of_rooms
        self.room_len = len(self.rooms)

    def create_hero(self):
        name = input('Enter name: ')
        age = input('Enter age: ')
        race = input('Enter race: ')
        hero = Hero(name, age, race)
        print(f"You created your hero")
        print(f'Good luck {hero.name}')
        self.hero = hero

    def get_rooms_count(self):
        return self.rooms

    def create_doors(self, range2):
        k = 1
        door_set = set()
        i = 0
        while i < range2 - 1:
            for j in range(random.randint(0, 3)):
                door_set.add(f'door {k}')
                k += 1
                i += 1
        self.doors = list(door_set)
        self.doors.sort()
        return self.doors

    def maze_builder(self, room_list, next_room):
        print(f',you just entered the Entrance Hall')
        room_count = len(room_list)
        choices = []
        input_massage = "Choose a door: ("
        door_massage = ""
        for count in range(room_count):
            choices.append(f'door {count + 1}')
            if count + 1 < m.room_len:
                door_massage += f'door{count + 1}, '
            else:
                door_massage += f'door{count + 1}): '
        input_massage += door_massage
        r = Monster('Bob', 'Ogre')
        while True:
            command = input(input_massage).lower()
            if command in choices:
                if room_list[choices.index(command)]:
                    if not random.choice([False, True]):
                        eval(next_room[choices.index(command)] + '()')
                    else:
                        print(f'You fund a monster with {r.health} health points')
                        fight(self.hero.damage, self.hero.health, r.damage, r.health)
                        break
            else:
                print(f'Sorry,you must choose {door_massage} ')



