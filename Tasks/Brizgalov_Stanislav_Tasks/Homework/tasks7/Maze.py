from random import randint
import characters as chr


class Wall:
    
    def __init__(self, wall1, wall2, wall3):
        self.wall1 = wall1
        self.wall2 = wall2
        self.wall3 = wall3


class Room(Wall):

    def __init__(self, wall1, wall2, wall3, door_coord, monster = False):
        super().__init__(wall1, wall2, wall3)
        self.door_coord = door_coord
        self.monster = monster

    def door_coord():
        d_c = ["top", "right", "bottom", "left"]
        door_coord = d_c[randint(0,3)]
        return door_coord

    def get_villian(self):
        return self.monster

    def get_hero(self):
        return self.hero


Room1 = Room(None, None, None, Room.door_coord())
Room2 = Room(None, None, None, Room.door_coord())
Room3 = Room(None, None, None, Room.door_coord())
Room4 = Room(None, None, None, Room.door_coord())
Room5 = Room(None, None, None, Room.door_coord())
Room6 = Room(None, None, None, Room.door_coord())
Room7 = Room(None, None, None, Room.door_coord())
Room8 = Room(None, None, None, Room.door_coord())
Room9 = Room(None, None, None, Room.door_coord())
Room10 = Room(None, None, None, Room.door_coord(), monster=True)



rooms = [Room1, Room2, Room3, Room4, Room5, Room6, Room7, Room8, Room9, Room10]
   
for room in rooms:
    if room.monster == True:
        chr.fight()



       





