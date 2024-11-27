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



a = {"N":True,"S":True,"E":True,"O":True}
Nord = {"N":False}
Sud = {"S":False}
a.update([Nord,Sud])
