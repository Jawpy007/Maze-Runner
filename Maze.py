#Jaouen programmation
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
        self.debut = False

    def is_depart(self):
        return self.debut

    def is_arriver(self):
        return self.arriver

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

    def depart(self):
        self.debut = True

class Maze:
    def __init__(self,Longeur,hauteur):
        self.maze = [ [Noed(i,j) for i in range(Longeur)] for j in range(hauteur)]
        self.longeur = Longeur
        self.hauteur = hauteur
    def cellule(self,x,y):
        return self.maze[x][y]


    def getmaze(self):
        return self.maze


    #Code pomper sur internet juste pour faciliter la comprehension le temps d'un affichage fait de nous meme
    def __str__(self):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * self.longeur * 2]
        for y in range(self.hauteur):
            maze_row = ['|']
            for x in range(self.hauteur):
                if self.maze[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.longeur):
                if self.maze[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def getnear(self, noed, Who=None):
        coordN=noed.coord()
        if Who=="N":
            coordNear=[coordN[0],coordN[1]-1]
        elif Who=="S":
            coordNear=[coordN[0],coordN[1]+1]
        elif Who=="O":
            coordNear=[coordN[0]-1,coordN[1]]
        elif Who=="E":
            coordNear=[coordN[0]+1,coordN[1]]
        elif Who==None:
            return(self.getnear(noed, "N")+ self.getnear(noed, "S")+ self.getnear(noed, "O")+ self.getnear(noed, "E"))
        if -1<coordNear[0]<self.longeur and -1<coordNear[1]<self.hauteur:
            return [[Who] + coordNear]
        else:
            return [[Who] + [None]+ [None]]
            
    def destroy_maze_walls(self, Cell, Who=None):
        Cell.destroy(Who)
        Liste=self.getnear(Cell,Who)
        for i in Liste:
            if i[0]=="N" and i[1]!=None and i[2]!=None:
                self.maze[i[1]][i[2]].destroy("S")
            elif i[0]=="S" and i[1]!=None and i[2]!=None:
                print(self.maze[i[1]][i[2]])
                self.maze[i[1]][i[2]].destroy("N")
                print(self.maze[i[1]][i[2]].getwalls)
            elif i[0]=="O" and i[1]!=None and i[2]!=None:
                self.maze[i[1]][i[2]].destroy("E")
            elif i[0]=="E" and i[1]!=None and i[2]!=None:
                self.maze[i[1]][i[2]].destroy("O") 
                     

if __name__=="__main__":
    #Test de fonctionnement des fonctions de base
    Noeu = Noed(0,0)
    print(Noeu.allwalls())
    print(Noeu.coord())


    print(Noeu.getwalls())
    Noeu.destroy("E")
    print(Noeu.getwalls())

    Laby = Maze(10,10)
    print(Laby.maze)

    print(Laby.cellule(0,0))