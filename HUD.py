#Tom Programmation

import tkinter as tk
from Maze import Maze  # Importer la classe Maze

# Paramètres
taille_cellule = 40  # Taille d'une cellule (en pixels)
couleur_mur = "#444444"  # Couleur des murs
couleur_chemin = "#DDDDDD"  # Couleur des chemins
couleur_debut = "#00FF00"  # Couleur de l'entrée
couleur_sortie = "#FF0000"  # Couleur de la sortie
epaisseur_mur = 6  # Épaisseur des murs

def dessiner_labyrinthe(canvas, maze):
    """Dessine un labyrinthe esthétique sur le canvas."""
    for ligne in range(maze.hauteur):
        for colonne in range(maze.longeur):
            x1 = colonne * taille_cellule
            y1 = ligne * taille_cellule
            x2 = x1 + taille_cellule
            y2 = y1 + taille_cellule

            cellule = maze.cellule(ligne, colonne)
            murs = cellule.getwalls()

            # Colorer le fond des chemins
            canvas.create_rectangle(x1, y1, x2, y2, fill=couleur_chemin, outline=couleur_chemin)

            # Dessiner les murs avec des couleurs et épaisseurs définies
            if murs['N']:
                canvas.create_line(x1, y1, x2, y1, fill=couleur_mur, width=epaisseur_mur)  # Mur nord
            if murs['S']:
                canvas.create_line(x1, y2, x2, y2, fill=couleur_mur, width=epaisseur_mur)  # Mur sud
            if murs['E']:
                canvas.create_line(x2, y1, x2, y2, fill=couleur_mur, width=epaisseur_mur)  # Mur est
            if murs['O']:
                canvas.create_line(x1, y1, x1, y2, fill=couleur_mur, width=epaisseur_mur)  # Mur ouest


    for cellule in self.maze:
        if cellule.is_arriver()==True:



fenetre = tk.Tk()
fenetre.title("Labyrinthe")


labyrinthe = Maze(10, 10)  # Labyrinthe de 10x10


canvas_largeur = labyrinthe.longeur * taille_cellule
canvas_hauteur = labyrinthe.hauteur * taille_cellule

# Création du canvas
canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
canvas.pack()

# Dessiner le labyrinthe
dessiner_labyrinthe(canvas, labyrinthe)
fenetre.mainloop()
