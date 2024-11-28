#Jaouen Programmation
from Maze import *
from math import sqrt
class A_Star:
    def __init__(self,Laby):
        self.laby = Laby

    def getlaby(self):
        return self.laby

    def MoovAble(self):
        pass

    def Coord_Fin(self):
        for i in self.laby.getmaze():
            for j in i:
                if j.is_arriver() == True:
                    return j.coord()
        return None

    def Coord_Depart(self):
        for i in self.getlaby().getmaze():
            for j in i:
                if j.debut == True:
                    return j.coord()
        return None

    def manhattan(self,cellule):
        """calcule la distance a pied, case par case, et renvoie le nbr de case a parcourir"""
        Depart = cellule.coord()
        Arriver = self.Coord_Fin()
        return(abs(Depart[0]-Arriver[0])+ abs(Depart[1]-Arriver[1]))


    def pytha(self,cellule):
        Depart = cellule.coord()
        Arriver = self.Coord_Fin()
        return (round(sqrt((Depart[0]+Arriver[0])^2+(Depart[1]+Arriver[1])^2)*sqrt(2)*10))


    def path(self):

        Depart = self.Coord_Depart()
        Arriver = self.Coord_Fin()
        Laby = self.getlaby()
        Visite = [Depart]
        Cell_depart  = Laby.cellule(Depart[0],Depart[1])
        Cell_arriver = Laby.cellule(Arriver[0],Arriver[1])
        Paire = {"N":"S","S":"N","E":"O","O":"E"}

        sortie = False
        while sortie == False:

            CaseProche = Laby.getnear(Cell_depart)
            #print(CaseProche)

            Obti = {}
            for case in CaseProche:
                if None not in case:
                    Card = case[0]
                    x,y = case[1], case[2]
                    Murs = Laby.cellule(x,y).getwalls()
                    #print("je suis en ",x,y,"Mur de",Card,Murs[Card])
                    #print(Murs[Paire[Card]] == False,(x,y) not in Visite)
                    if Murs[Paire[Card]] == False and (x,y) not in Visite:
                        Discriminant = self.manhattan(Laby.cellule(x,y)) + self.pytha(Laby.cellule(x,y))
                        Obti[(x,y)] = Discriminant
                        if Laby.cellule(x,y).is_arriver():
                            sortie = True

            #print(Obti)
            Mieux = min(Obti)
            BestCell = Laby.cellule(Mieux[1],Mieux[0])
            Visite.append((Mieux[1],Mieux[0]))
            Cell_depart = BestCell

        return Visite


            #print(Visite)


if __name__=="__main__":
    #creation labyrinthe basique
    Laby = Maze(3,3)

    Laby.maze[0][0].destroy("E")
    Laby.maze[1][0].destroy("O")

    Laby.maze[0][0].depart()

    Laby.maze[1][0].destroy("E")
    Laby.maze[2][0].destroy("O")

    Laby.maze[1][0].destroy("S")
    Laby.maze[1][1].destroy("N")

    Laby.maze[1][1].destroy("S")
    Laby.maze[1][2].destroy("N")

    Laby.maze[1][2].finale()


    #mise en place du solver
    Solver = A_Star(Laby)



    print(Solver.Coord_Fin())
    print(Solver.Coord_Depart())
    print(Solver.getlaby())

    print(Solver.path())
