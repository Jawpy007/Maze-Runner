# Importation des modules nécessaires
import tkinter as tk  # Module pour l'interface graphique
from Maze import Maze  # Classe pour créer et manipuler le labyrinthe
from Solver import *  # Importation des algorithmes de résolution de labyrinthes
import time  # Module pour la gestion du temps (non utilisé ici)
from Generator import *  # Importation des algorithmes de génération de labyrinthes


# Paramètres pour l'affichage graphique
taille_cellule = 40  # Taille d'une cellule en pixels
couleur_mur = "black"  # Couleur des murs du labyrinthe
couleur_chemin = "white"  # Couleur des chemins du labyrinthe
epaisseur_mur = 6  # Épaisseur des murs en pixels

def dessiner_labyrinthe(canvas, maze):
    """
    Dessine un labyrinthe sur un canvas tkinter.
    canvas : widget tkinter où le labyrinthe sera dessiné
    maze : instance de Maze représentant le labyrinthe
    """
    for ligne in range(maze.hauteur):
        for colonne in range(maze.longeur):
            # Coordonnées de la cellule sur le canvas
            x1 = colonne * taille_cellule
            y1 = ligne * taille_cellule
            x2 = x1 + taille_cellule
            y2 = y1 + taille_cellule

            # Récupération de la cellule et des murs associés
            cellule = maze.cellule(ligne, colonne)
            murs = cellule.getwalls()

            # Dessin du fond de la cellule
            canvas.create_rectangle(y1, x1, y2, x2, fill=couleur_chemin, outline=couleur_chemin)

            # Dessin des murs si présents
            if murs['N']:
                canvas.create_line(y1, x1, y2, x1, fill=couleur_mur, width=epaisseur_mur)  # Mur nord
            if murs['S']:
                canvas.create_line(y1, x2, y2, x2, fill=couleur_mur, width=epaisseur_mur)  # Mur sud
            if murs['E']:
                canvas.create_line(y2, x1, y2, x2, fill=couleur_mur, width=epaisseur_mur)  # Mur est
            if murs['O']:
                canvas.create_line(y1, x1, y1, x2, fill=couleur_mur, width=epaisseur_mur)  # Mur ouest

def changer_couleur_case(canvas, ligne, colonne, couleur):
    """
    Change la couleur d'une cellule spécifique dans le labyrinthe.
    canvas : widget tkinter où le labyrinthe est dessiné
    ligne : indice de la ligne de la cellule
    colonne : indice de la colonne de la cellule
    couleur : nouvelle couleur de la cellule
    """
    x1 = colonne * taille_cellule
    y1 = ligne * taille_cellule
    x2 = x1 + taille_cellule
    y2 = y1 + taille_cellule

    # Redessine la cellule avec la couleur spécifiée
    canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline=couleur)
    
def trajet(canvas,fenetre,solution,index=1):
    """
    Affiche progressivement le chemin de la solution sur le canvas.
    index : étape actuelle du trajet (par défaut 1)
    """
    if index < len(solution):
        # Colorie la cellule actuelle en vert
        changer_couleur_case(canvas, solution[index][1], solution[index][0], "green")
        # Planifie l'affichage de la prochaine cellule après 100 ms
        fenetre.after(100, trajet , canvas,fenetre,solution, index + 1)
def Labyrinthe_affichage(taille, seed):
    Laby = Maze(int(taille))  

    MM(Laby, seed)

    fenetre = tk.Tk()
    fenetre.title(seed)

    canvas_largeur = Laby.longeur * taille_cellule
    canvas_hauteur = Laby.hauteur * taille_cellule


    canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
    canvas.pack()


    dessiner_labyrinthe(canvas, Laby)

    for ligne in Laby.getmaze():
        for cellules in ligne:
            if cellules.is_depart():  
                changer_couleur_case(canvas, cellules.coord()[0], cellules.coord()[1], "green")
            if cellules.is_arriver():  
                changer_couleur_case(canvas, cellules.coord()[0], cellules.coord()[1], "red")

    solver = A_Star(Laby)
    solution = solver.solve()  
    print(solution)  

    bouton = tk.Button(fenetre, text="Voir le chemin", command=lambda:(trajet(canvas,fenetre,solution), bouton.config(state="disabled"))) # lance trajet et Désactive le bouton pour éviter des clics multiples
    bouton.pack(pady=20)

    fenetre.mainloop()
def menu():

    fenetre = tk.Tk()
    fenetre.title("menu")

    canvas_largeur = 500
    canvas_hauteur = 500

    canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
    canvas.pack(fill="both")

    """# Dessin du labyrinthe sur le canvas
    dessiner_labyrinthe(canvas, Laby)

    # Mise en évidence des cases de départ et d'arrivée
    for ligne in Laby.getmaze():
        for cellules in ligne:
            if cellules.is_depart():  # Si c'est la cellule de départ
                changer_couleur_case(canvas, cellules.coord()[0], cellules.coord()[1], "green")
            if cellules.is_arriver():  # Si c'est la cellule d'arrivée
                changer_couleur_case(canvas, cellules.coord()[0], cellules.coord()[1], "red")"""


    entry_taille = tk.Entry (fenetre) 
    entry_taille.pack(pady=20)
    entry_seed = tk.Entry (fenetre) 
    entry_seed.pack(pady=20)
    bouton = tk.Button(fenetre, text="Go", command=lambda: Labyrinthe_affichage(entry_taille.get(), entry_seed.get()))
    bouton.pack(pady=20)

    fenetre.mainloop()

if __name__ == "__main__":
    menu()