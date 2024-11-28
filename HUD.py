import tkinter as tk
from Maze import Maze  # Importer votre classe Maze

Laby = Maze(10,10)
for ligne in Laby.getmaze():
    for cellules in ligne:
        if cellules.is_depart==True:
            print(cellules)
# Paramètres
taille_cellule = 40  # Taille d'une cellule (en pixels)
couleur_mur = "#444444"  # Couleur des murs
couleur_chemin = "#DDDDDD"  # Couleur des chemins
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

            # Colorer le fond des chemins
            case=canvas.create_rectangle(x1, y1, x2, y2, fill=couleur_chemin, outline=couleur_chemin)

            # Dessiner les murs avec des couleurs et épaisseurs définies
            if murs['N']:
                canvas.create_line(x1, y1, x2, y1, fill=couleur_mur, width=epaisseur_mur)  # Mur nord
            if murs['S']:
                canvas.create_line(x1, y2, x2, y2, fill=couleur_mur, width=epaisseur_mur)  # Mur sud
            if murs['E']:
                canvas.create_line(x2, y1, x2, y2, fill=couleur_mur, width=epaisseur_mur)  # Mur est
            if murs['O']:
                canvas.create_line(x1, y1, x1, y2, fill=couleur_mur, width=epaisseur_mur)  # Mur ouest

def changer_couleur_case(canvas, ligne, colonne, couleur):
    """Change la couleur d'une case spécifique dans le labyrinthe."""
    x1 = colonne * taille_cellule
    y1 = ligne * taille_cellule
    x2 = x1 + taille_cellule
    y2 = y1 + taille_cellule

    # Redessiner la case avec la nouvelle couleur
    canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline=couleur)

for ligne in Laby.maze:
    for cellules in ligne:
        if cellules.is_depart==True:
            changer_couleur_case(case,cellules.coord[0],cellule.coord[1],"green")

for ligne in Laby.maze:
    for cellules in ligne:
        if cellules.is_==True:
            changer_couleur_case(case,cellules.coord[0],cellule.coord[1],"green")


# Initialisation de la fenêtre tkinter
fenetre = tk.Tk()
fenetre.title("Labyrinthe avec changement de couleur")

# Charger le labyrinthe


# Dimensions du canvas
canvas_largeur = labyrinthe.longeur * taille_cellule
canvas_hauteur = labyrinthe.hauteur * taille_cellule

# Création du canvas
canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
canvas.pack()

# Dessiner le labyrinthe
dessiner_labyrinthe(canvas, labyrinthe)

# Lancer l'interface graphique
fenetre.mainloop()


labyrinthe = Maze(10, 10)  # Labyrinthe de 10x10


canvas_largeur = labyrinthe.longeur * taille_cellule
canvas_hauteur = labyrinthe.hauteur * taille_cellule

# Création du canvas
canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
canvas.pack()

# Dessiner le labyrinthe
dessiner_labyrinthe(canvas, labyrinthe)
fenetre.mainloop()
