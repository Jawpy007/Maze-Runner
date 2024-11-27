import random #utile ?


class Noed:
    """
    Creation de la classe Noed:
        x,y = coordonnée x,y
        walls = une liste des mures qu'il possede
        arriver = Defini si c'est l'arriver
    """
    def __init__(self,x,y):
        self.x , self.y = x,y
        self.walls = {"N":True,"S":True,"E":True,"O":True}
        self.arriver = False

    def getwalls(self):
        """
        retourne tous les murs qu'il possede ou pas
        """
        return self.walls

    def allwalls(self):
        """
        retourne tous les murs qu'il possede uniquement
        """
        for Bool in self.walls.values():
            if Bool == False:
                return False

        return True

    def coord(self):
        """
        retourne les coordonnée d'une cellule
        """
        return (self.x,self.y)

    def destroy(self,Who = None):
        """
        si aucun argument donnée detruit tous les murs
        si donnée un point cardinaux en str(), detruit le murs correspondant si il existe
        """
        Nord = {"N":False}
        Sud = {"S":False}
        Est = {"E":False}
        Ouest = {"O":False}
        if Who == None:
           self.walls.update(Nord)
           self.walls.update(Sud)
           self.walls.update(Est)
           self.walls.update(Ouest)
        else:
            self.walls[Who] = False

    def finale(self):
        self.arriver = True

class Maze:
    def __init__(self,Longeur,Largeur):
        self.maze = [ [Noed(i,j) for i in range(Longeur)] for j in range(Largeur)]

    def cellule(self,x,y):
        return self.maze[x][y]


if __name__=="__main__":
    Noeu = Noed(0,0)
    print(Noeu.allwalls())
    print(Noeu.coord())


    print(Noeu.getwalls())
    Noeu.destroy("E")
    print(Noeu.getwalls())

    Laby = Maze(10,10)
    print(Laby.maze)

    print(Laby.cellule(0,0))
