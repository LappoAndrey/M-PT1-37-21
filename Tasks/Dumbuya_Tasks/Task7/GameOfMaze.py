from Maze import*
from Room import*
from Door import*
from Wall import*



m = Maze(4)

m.create_hero()
m.maze_builder(m.rooms, ['catacombs', 'old_museum', 'fire_room', 'stinky_room'])
