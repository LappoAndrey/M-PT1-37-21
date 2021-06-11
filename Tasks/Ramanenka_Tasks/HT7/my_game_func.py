import random


""" функция случайного выбора начального положения игрока;
выбираются обе координаты x и y
"""
def step_init(dim):
    x = random.randint(0,dim-1)
    y = random.randint(0,dim-1)
    l = [x,y]
    return l

""" функция для выбора хода игрока; 
позволяет сделать один ход по гозонтали или вертикали, контролируя границы лабиринта
"""
def select_step(pos:list, num):
    n = pos[0]
    m = pos[1]
    ways = {}
    if n==0 and m==0:
        val = [[n+1, m], [n, m+1]]
    elif n==0 and m==num-1:
        val = [[n+1, m], [n, m-1]]
    elif n==num-1 and m==0:
        val = [[n-1, m], [n, m+1]]
    elif n==num-1 and m==num-1:
        val = [[n-1, m], [n, m-1]]
    elif n==0:
        val = [[n+1, m], [n, m+1], [n, m-1]]
    elif n==num-1:
        val = [[n-1, m], [n, m+1], [n, m-1]]
    elif m==0:
        val = [[n-1, m], [n+1, m], [n, m+1]]
    elif m==num-1:
        val = [[n-1, m], [n+1, m], [n, m-1]]
    else:
        val = [[n-1, m], [n+1, m], [n, m-1], [n, m+1]]
    ways [tuple(pos)] = val
    list_pos = list(ways.values())
    list_new = list_pos[0]
    position = random.choice(list_new)
    return position