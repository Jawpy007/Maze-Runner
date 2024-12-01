#Joe Programmation
from Maze import *
from random import *

def mazemaker(lab, Longeur, hauteur, seed=None):
    Ouvertureenhaut="e"
    listeValeur=[]
    listeValeur.append([x for x in range(0, Longeur)])
    valeursalle=[0,Longeur]
    for h in range(hauteur):
        # horrizontal
        for l in range(1,Longeur):
                choix=choixrandom(seed)
                if choix==True:
                    listeValeur[h][l]=listeValeur[h][l-1]
                    lab.destroy_maze_walls(lab.maze[h][l],"O")

        # vertical
        if h!=hauteur-1:
            valeursalle[0]+=Longeur
            valeursalle[1]+=Longeur
            listeValeur.append([x for x in range(valeursalle[0],valeursalle[1])])
            nontrie=listeValeur.copy()
            listeValeur[h]=listeValeurtrie(listeValeur[h])
            Nombredesalle=len(listeValeur[h])
            Nombredesortie=[]

            for salle in range(Nombredesalle):
                nombremaxdesortie=listeValeur[h][salle][3]//2
                nombremindesortie=1
                if nombremaxdesortie>1:
                    Nombredesortie.append(randint(nombremindesortie,nombremaxdesortie))
                else:
                    Nombredesortie.append(1)

            for salle in range(Nombredesalle):
                valeurinterdite=[]
                for sortie in range(Nombredesortie[salle]):
                    aleaval=randint(listeValeur[h][salle][0],listeValeur[h][salle][1])
                    while aleaval in valeurinterdite:
                        aleaval=randint(listeValeur[h][salle][0],listeValeur[h][salle][1])
                    valeurinterdite.append(aleaval)
                    lab.destroy_maze_walls(lab.maze[h][valeurinterdite[-1]],"S")
                    listeValeur[h+1][valeurinterdite[-1]]=nontrie[h][valeurinterdite[-1]]


def choixrandom(seed):
    if seed!=None:
        a=randint(1,22)
        if a==1:
            return(False)
        else:
            return(True)
    else:
        a=randint(1,4)
        if a==1:
            return(False)
        else:
            return(True)

def listeValeurtrie(listeValue):
    premierindex=0 #index , valeur
    dernierindex=0 #index , valeur
    longueur=len(listeValue)
    listeensemble=[]
    for i in range(longueur):
        if i+1<longueur:
            if listeValue[premierindex]==listeValue[i+1]:
                dernierindex=i+1
            else:
                nbcell=dernierindex-premierindex+1
                listeensemble+=[[premierindex,dernierindex, listeValue[premierindex],nbcell]]
                premierindex=i+1
                dernierindex=i+1
        else:

            nbcell=dernierindex-premierindex+1
            listeensemble+=[[premierindex,dernierindex, listeValue[premierindex],nbcell]]
    return(listeensemble)
