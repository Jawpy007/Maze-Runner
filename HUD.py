<<<<<<< Updated upstream
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
        if cellules.is_arriver==True:
            changer_couleur_case(case,cellules.coord[0],cellule.coord[1],"green")


# Initialisation de la fenêtre tkinter
fenetre = tk.Tk()
fenetre.title("Labyrinthe")

# Charger le labyrinthe


# Dimensions du canvas
canvas_largeur = Laby.longeur * taille_cellule
canvas_hauteur = Laby.hauteur * taille_cellule

# Création du canvas
canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
canvas.pack()

# Dessiner le labyrinthe
dessiner_labyrinthe(canvas, Laby)

# Lancer l'interface graphique
fenetre.mainloop()




canvas_largeur = labyrinthe.longeur * taille_cellule
canvas_hauteur = labyrinthe.hauteur * taille_cellule

# Création du canvas
canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
canvas.pack()

# Dessiner le labyrinthe
dessiner_labyrinthe(canvas, labyrinthe)
fenetre.mainloop()
=======
#Tom Programmation
import tkinter as tk
from Maze import Maze

# Dimensions du labyrinthe
LARGEUR = 10
HAUTEUR = 10
CELL_SIZE = 40  # Taille d'une cellule en pixels

def draw_maze(canvas, maze):
    """Dessine le labyrinthe sur le canvas en fonction des murs de chaque cellule."""
    for x in range(maze.longeur):
        for y in range(maze.hauteur):
            cell = maze.cellule(x, y)
            x1, y1 = x * CELL_SIZE, y * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

            # Dessiner les murs en fonction de leur présence
            if cell.walls["N"]:  # Mur Nord
                canvas.create_line(x1, y1, x2, y1, fill="black", width=2)
            if cell.walls["S"]:  # Mur Sud
                canvas.create_line(x1, y2, x2, y2, fill="black", width=2)
            if cell.walls["E"]:  # Mur Est
                canvas.create_line(x2, y1, x2, y2, fill="black", width=2)
            if cell.walls["O"]:  # Mur Ouest
                canvas.create_line(x1, y1, x1, y2, fill="black", width=2)

# Initialisation de la fenêtre tkinter
root = tk.Tk()
root.title("Affichage du Labyrinthe")

canvas_width = LARGEUR * CELL_SIZE
canvas_height = HAUTEUR * CELL_SIZE
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Création et affichage du labyrinthe
laby = Maze(LARGEUR, HAUTEUR)
draw_maze(canvas, laby)

# Lancer la boucle tkinter
root.mainloop()

>>>>>>> Stashed changes
