#Jaouen Programmation
from Maze import *
from math import sqrt
from heapq import * #permet de faire des tas

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
        """ calcule de la diagonal"""
        Depart = cellule.coord()
        Arriver = self.Coord_Fin()
        return (round(sqrt((Depart[0]+Arriver[0])^2+(Depart[1]+Arriver[1])^2)*sqrt(2)*10))

    def solve(self):
        #coordonnée de debut et de fin
        Start = self.Coord_Depart()
        Goal = self.Coord_Fin()

        print("Start:",Start,"Goal:",Goal)

        x,y = Start[0] , Start[1]



        #creation du tas, car un tas retourne de base la plus petite valeur
        open_set = []
        #initialise la premiere valeur
        heappush(open_set,(0,Start))

        #Obtention du labyrinthe pour pouvoir gerer les cellules
        Laby = self.getlaby()

        #dico pour savoir d'ou je viens
        came_from = {}

        #Les discrimants pour determiné qu'elle est la meilleur case
        g_score = {Start: 0}
        f_score = {Start: self.manhattan(Laby.cellule(x,y))}

        #set contenant les cellules deja visité, et ne pas tourné dans le vide
        visite = set()

        #Tant qu'il reste quelque chose a regardé
        while open_set:
            #Coordonnée de la cellule courante
            current = heappop(open_set)[1] #d'apres la doc : "Extraie le plus petit élément de heap en préservant l'invariant du tas" c'est donc UTILE :)

            #On la visite donc l'ajoute dans le set visite
            visite.add(current)

            #si chemin trouvé alors retourne la liste du chemin parcourut
            if current == Goal:
                #path -> liste contenant le chemin "retour" ( a l'envers donc)
                path = []
                #Fait le chemin "retour"
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(Start)

                #c'est a l'envers :/
                path.reverse()
                return path


            for direction in [(0,1), (1,0), (0,-1), (-1,0)]:#je regarde dans toutes les direction, deso joe pour la fonction :'(
                neighbor = (current[1] + direction[1], current[0] + direction[0])#
                print(neighbor)

            return "Test"





if __name__=="__main__":
    Laby = Maze(3, 3)

    # Detruire des murs pour creer un chemin
    Laby.maze[0][0].destroy("E")
    Laby.maze[1][0].destroy("O")
    Laby.maze[1][0].destroy("S")
    Laby.maze[1][1].destroy("N")
    Laby.maze[1][1].destroy("E")
    Laby.maze[2][1].destroy("O")
    Laby.maze[2][1].destroy("S")
    Laby.maze[2][2].destroy("N")

    Laby.maze[0][0].depart()
    Laby.maze[2][2].finale()
    print(Laby)

    # Resolution du labyrinthe
    Solver = A_Star(Laby)
    print(Solver.solve())


