import tkinter as tk
from Maze import Maze
from Solver import*
import time
from Generator import *

if __name__=="__main__":
    Laby = Maze(10, 10)

    MM(Laby)

    solver=A_Star(Laby)
    solution= solver.solve()
    print(solution)





# Paramètres

taille_cellule = 40  # Taille d'une cellule (en pixels)
couleur_mur = "black"  # Couleur des murs
couleur_chemin = "white"
epaisseur_mur = 6  # Épaisseur des murs
def dessiner_labyrinthe(canvas, maze):
    """Dessine un labyrinthe sur le canvas."""
    for ligne in range(maze.hauteur):
        for colonne in range(maze.longeur):
            x1 = colonne * taille_cellule
            y1 = ligne * taille_cellule
            x2 = x1 + taille_cellule
            y2 = y1 + taille_cellule

            cellule = maze.cellule(ligne, colonne)
            murs = cellule.getwalls()

            # Colore le fond des chemins
            case=canvas.create_rectangle(y1, x1, y2, x2, fill=couleur_chemin, outline=couleur_chemin)

            # Dessine les murs avec des couleurs et épaisseurs définies
            if murs['N']:
                canvas.create_line(y1, x1, y2, x1, fill=couleur_mur, width=epaisseur_mur)  # Mur nord
            if murs['S']:
                canvas.create_line(y1, x2, y2, x2, fill=couleur_mur, width=epaisseur_mur)  # Mur sud
            if murs['E']:
                canvas.create_line(y2, x1, y2, x2, fill=couleur_mur, width=epaisseur_mur)  # Mur est
            if murs['O']:
                canvas.create_line(y1, x1, y1, x2, fill=couleur_mur, width=epaisseur_mur)  # Mur ouest

def changer_couleur_case(canvas, ligne, colonne, couleur):
    """Change la couleur d'une case spécifique dans le labyrinthe."""
    x1 = colonne * taille_cellule
    y1 = ligne * taille_cellule
    x2 = x1 + taille_cellule
    y2 = y1 + taille_cellule

    # Redessiner la case avec la nouvelle couleur
    canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline=couleur)

# Initialisation de la fenêtre tkinter

fenetre = tk.Tk()
fenetre.title("Labyrinthe")

# Dimensions du canvas
canvas_largeur = Laby.longeur * taille_cellule
canvas_hauteur = Laby.hauteur * taille_cellule

# Création du canvas
canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
canvas.pack()

# Dessiner le labyrinthe
dessiner_labyrinthe(canvas, Laby)

for ligne in Laby.getmaze():                                     #coloriage de la cellule départ

    for cellules in ligne:
        if cellules.is_depart()==True:
            changer_couleur_case(canvas,cellules.coord()[0],cellules.coord()[1],"green")
        if cellules.is_arriver()==True:

            print('t')
            changer_couleur_case(canvas,cellules.coord()[0],cellules.coord()[1],"red")

def trajet(index=1):                #colorie chaque le chemin
    bouton.config(state="disabled")  # Désactive le bouton
    global solution
    if index < len(solution):
        changer_couleur_case(canvas,solution[index][1],solution[index][0],"green")
        fenetre.after(500, trajet, index + 1)

bouton = tk.Button(fenetre, text="Voir le chemin", command=trajet)
bouton.pack(pady=20)

# Lancer l'interface graphique
fenetre.mainloop()

