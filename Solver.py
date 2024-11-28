#Jaouen Programmation
from Maze import *

Laby = Maze(3,3)

Laby.maze[0][0].destroy("E")
Laby.maze[1][0].destroy("E")
Laby.maze[1][0].destroy("S")
Laby.maze[1][1].destroy("S")
Laby.maze[1][2].finale()

def MoovAble(Laby):
    pass

def Coord_Fin(Laby):
    for i in Laby.maze:
        for j in i:
            if j.arriver == True:
                return j.coord()
    return None

print(Laby)
print(Coord_Fin(Laby))