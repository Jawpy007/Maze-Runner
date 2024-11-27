# Ecrit ton programme ici ;-)
class Noed:
    def __init__(self,x,y):
        self.x , self.y = x,y
        self.walls = {"N":True,"S":True,"E":True,"O":True}

    def getwalls(self):
        return self.walls

    def allwalls(self):
        for Bool in self.walls.values():
            if Bool == False:
                return False

        return True

    def coord(self):
        return (self.x,self.y)

    def destroy(self,Who = None):
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

class Maze:
    def __init__(self,Longeur,Largeur):
        self.maze = [ [Noed(i,j) for i in range(Longeur)] for j in range(Largeur)]

if __name__=="__main__":
    Noeu = Noed(0,0)
    print(Noeu.allwalls())
    print(Noeu.coord())


    print(Noeu.getwalls())
    Noeu.destroy("E")
    print(Noeu.getwalls())

    Laby = Maze(10,10)
    print(Laby.maze)
