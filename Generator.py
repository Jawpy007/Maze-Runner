#Joe Programmation
from Maze import *
from random import *
from Solver import *


def MM(lab, seed=None):
    Ouvertureenhaut="e"
    hauteur=lab.hauteur
    longeur=lab.longeur
    listeValeur=[[Valeur_case for Valeur_case in range(longeur*h, longeur*(h+1))] for h in range(hauteur)] # on donne un numero a chaque case du laby

    #on crée le depart
    lab.maze[0][0].depart()

    for h in range(hauteur):

        #1 on relie aleatoirement horrizontalement des cellule
        for l in range(1, longeur):
            choix=choixrandom(seed)
            if choix==True:
                listeValeur[h][l]=listeValeur[h][l-1]
                lab.destroy_maze_walls(lab.maze[l][h],"O")

        #2 on relie aleatoirement verticalement des cellule
        if h<hauteur-1: #on verifie qu'on n'est pas a la derniere ligne de cellule
            dicVal, dicLen_Val=dicValIndex(listeValeur[h]) #on fait un dico dicval qui reference tout les index associer a une valeur et listelen le nombre d'index par valeur
            Nombre_sortie={} #liste du nombre de sortie a faire par valeur
            for cle in (dicLen_Val.keys()):
                if dicLen_Val[cle]//2>=1:
                    dicLen_Val[cle]=dicLen_Val[cle]//2
                Nombre_sortie[cle]=[choixrandom(seed, [1, dicLen_Val[cle]])]
            for cle in dicVal:
                index_vu=[]
                for sortie in range(Nombre_sortie[cle][0]): # nombre de repetition = nombre de sortie souhaiter pour cette valeur
                    index_possible=dicVal[cle]
                    index_de_la_sortie=choixrandom(seed,(0,len(index_possible)-1)) #on choisi au hasard un chiffre
                    while index_de_la_sortie in index_vu : #tant que l'index choisi a deja etait utilisé on  re choisi un index
                        index_de_la_sortie=choixrandom(seed,(0,len(index_possible)-1)) #on choisi au hasard un chiffre
                    index_vu+=[index_de_la_sortie]
                    index_de_la_sortie=index_possible[index_de_la_sortie] # on recuperer l'index de la sortie dans la liste des index possible
                    listeValeur[h+1][index_de_la_sortie]=listeValeur[h][index_de_la_sortie]
                    lab.destroy_maze_walls(lab.maze[index_de_la_sortie][h],"S")
        else:
            for l in range(1, longeur):
                listeValeur[h][l]=listeValeur[h][l-1]
                lab.destroy_maze_walls(lab.maze[l][h],"O")
            lab.maze[randint(1,longeur-1)][randint(0,hauteur-1)].finale()

def choixrandom(seed, Valeur=None):
    if Valeur==None:
        if seed!=None:
            a=randint(1,3)
            if a==1:
                return(False)
            else:
                return(True)
        else:
            a=randint(1,2)
            if a==1:
                return(False)
            else:
                return(True)
    else:
        if seed!=None:
            return(randint(Valeur[0],Valeur[1]))
        else:
            return(randint(Valeur[0],Valeur[1]))

def dicValIndex(listevaleur):
    dic_valeur={}
    for index_valeur in range(len(listevaleur)):
        valeur=listevaleur[index_valeur]
        if valeur in dic_valeur.keys():
            dic_valeur[valeur]+=[index_valeur]
        else:
            dic_valeur[valeur]=[index_valeur]
    listelen={}
    for cle in dic_valeur:
        listelen[cle]=len(dic_valeur[cle])
    return(dic_valeur, listelen)

if __name__=="__main__":
    Laby = Maze(10, 10)

    MM(Laby)

    solver=A_Star(Laby)
    solution= solver.solve()
    print(solution)
