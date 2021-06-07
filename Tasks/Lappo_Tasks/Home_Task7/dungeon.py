from random import randint
import h_m_f as h_m_f

class Wall:
    
    def __init__(self, wall1, wall2, wall3):
        self.wall1 = wall1
        self.wall2 = wall2
        self.wall3 = wall3

class Room(Wall):

    def __init__(self, wall1, wall2, wall3, door_coord, monster = False, loot = ''):
        super().__init__(wall1, wall2, wall3)
        self.door_coord = door_coord
        self.monster = monster
        self.loot = loot

    def door_coord():
        d_c = ["top", "right", "bottom", "left"]
        door_coord = d_c[randint(0,3)]
        return door_coord

    def get_monster(self):
        return self.monster

    def get_hero(self):
        return self.hero

    def getloot(self):
        return self.loot


Room1 = Room(None, None, None, Room.door_coord())
Room2 = Room(None, None, None, Room.door_coord(), monster=True,loot='Sword')
Room3 = Room(None, None, None, Room.door_coord())
Room4 = Room(None, None, None, Room.door_coord())
Room5 = Room(None, None, None, Room.door_coord(), monster=True,loot='shield')
Room6 = Room(None, None, None, Room.door_coord())
Room7 = Room(None, None, None, Room.door_coord())
Room8 = Room(None, None, None, Room.door_coord())
Room9 = Room(None, None, None, Room.door_coord())
Room10 = Room(None, None, None, Room.door_coord(), monster=True,loot='princess')



rooms = [Room1, Room2, Room3, Room4, Room5, Room6, Room7, Room8, Room9, Room10]
   
for room in rooms:
    if room.monster == True:
        die=h_m_f.fight()
        if die=='Hero':
            print(f"Hero DIE in before he end his journey. He found {room.loot}")
            break
        else: print(f"Hero find treasury and princess. He found {room.loot}")
            



       





