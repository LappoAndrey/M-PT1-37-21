from my_game_func import select_step, step_init


class Heroe():

    def __init__(self, name, move):
        self.__name = name
        self.__move = move
       
    def get_name(self):
        return self.__name

    def get_move(self):
        return self.__move

    def set_name(self,name):
        self.__name=name

    def set_move(self, move):
        self.__move = move

class Monster():

    def __init__(self, name, move):
        self.__name = name
        self.__move = move
       
    def get_name(self):
        return self.__name

    def get_move(self):
        return self.__move

    def set_name(self,name):
        self.__name=name

    def set_move(self, move):
        self.__move = move

"""здесь должен был быть класс лабиринта/поля

class Rooms(Heroe, Monster, labirint):
"""

""" на данном этапе идет обработка кодом, описанным функциями.
функция для создания лабиринта 
"""
def matriz(simbol,x,y):
    tabl=[]
    row=[]
    for i in range(x):
        row=[]
        for j in range(y):
            row.append(simbol)
        tabl.append(row)
    return tabl


"""" функция визуализации поля в консоли
"""
def show_map(mapa):
    x=len(mapa)
    y=len(mapa[0])
    for i in range(x):
        print ('')
        for j in range(y):
            print (mapa[i][j],end = '')


""" функция замены символов (заполнителей) поля именами объектов игры для визуализации
"""
def change_map(map1):
    x=len(map1) 
    y=len(map1[0])
    for i in range(x):
        print ('')
        for j in range(y):
            print (map1[i][j],end = '')

print('Enter the number in range 2 - 10 \n')
num = int(input(''))
labirint = matriz("*", num, num)

show_map(labirint)
print(' ')
step_init_h = step_init(num)
step_init_m = step_init(num)
H = Heroe("Hero",step_init_h)
M = Monster("Monstr",step_init_m)

H_move = H.get_move()
M_move = M.get_move() 
print(f'start of H is {H_move}, start of M is {M_move}')

show_step_init_h = labirint[H_move[0]][H_move[1]] = 'H'
show_step_init_m = labirint[M_move[0]][M_move[1]] = 'M'
change_map(labirint)

next_step_h = select_step(H_move, num)  
next_step_m = select_step(M_move, num)
H.set_move(next_step_h)
M.set_move(next_step_m)

H_move = H.get_move()
M_move = M.get_move()

print(' ')
print(f'next of H is {H_move}, next of M is {M_move}')
labirint = matriz("*", num, num)
labirint[H_move[0]][H_move[1]] = 'H'
labirint[M_move[0]][M_move[1]] = 'M'
change_map(labirint)
print(' ')


""" переключение очереди ходов игроков 
"""
flag = 1
count = 0
while H.get_move() != M.get_move():
    count += 1
    if flag == 1 :
        next_step_h = select_step(H.get_move(), num)
        H.set_move(next_step_h)
        print(f'step of H is {H.get_move()}')
        labirint = matriz("*", num, num)
        labirint[H.get_move()[0]][H.get_move()[1]] = 'H'
        labirint[M.get_move()[0]][M.get_move()[1]] = 'M'
        change_map(labirint)
        print(' ')
        flag = 1 - flag
    else:
        next_step_m = select_step(M.get_move(), num)
        M.set_move(next_step_m)
        print(f'step of M is {M.get_move()}')
        labirint = matriz("*", num, num)
        labirint[H.get_move()[0]][H.get_move()[1]] = 'H'
        labirint[M.get_move()[0]][M.get_move()[1]] = 'M'
        change_map(labirint)
        print(' ')
        flag = 1 + flag
    if not next_step_h != next_step_m:
        print(f'number of steps is {count + 1}')
        print('attack')
        break