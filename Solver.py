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

print(Laby)