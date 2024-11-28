#Jaouen Programmation
from Maze import *



class A_Star:
    def __init__(self,Laby):
        self.laby = Laby

    def MoovAble(self):
        pass

    def Coord_Fin(self):
        for i in self.laby.getmaze():
            for j in i:
                if j.is_arriver() == True:
                    return j.coord()
        return None

    def Coord_Depart(self):
        for i in self.laby.getmaze():
            for j in i:
                if j.debut == True:
                    return j.coord()
        return None

    def chemin_possible(self,Coord):
        Ways = []


    def path(self):
        Depart = self.Coord_Depart()
        Arriver = self.Coord_Fin()

        pass


if __name__=="__main__":
    #creation labyrinthe basique
    Laby = Maze(3,3)
    Laby.maze[0][0].destroy("E")
    Laby.maze[0][0].depart()
    Laby.maze[1][0].destroy("E")
    Laby.maze[1][0].destroy("S")
    Laby.maze[1][1].destroy("S")
    Laby.maze[1][2].finale()


    #mise en place du solver
    Solver = A_Star(Laby)

    print(Solver.Coord_Fin())
    print(Solver.Coord_Depart())

