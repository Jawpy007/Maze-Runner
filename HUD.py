# Importation des modules nécessaires
import tkinter as tk  # Module pour l'interface graphique
from Maze import Maze  # Classe pour créer et manipuler le labyrinthe
from Solver import *  # Importation des algorithmes de résolution de labyrinthes
from Generator import *  # Importation des algorithmes de génération de labyrinthes


# Paramètres pour l'affichage graphique
taille_cellule = 40  # Taille d'une cellule en pixels
couleur_mur = "black"  # Couleur des murs du labyrinthe
couleur_chemin = "white"  # Couleur des chemins du labyrinthe
epaisseur_mur = 6  # Épaisseur des murs en pixels

def dessiner_labyrinthe(canvas, maze):
    """
    Fonction qui dessine un labyrinthe sur un canvas tkinter.
    - canvas : widget tkinter où le labyrinthe sera dessiné.
    - maze : instance de Maze représentant le labyrinthe.
    """
    for ligne in range(maze.hauteur):  # Parcours des lignes du labyrinthe
        for colonne in range(maze.longeur):  # Parcours des colonnes du labyrinthe
            # Calcul des coordonnées de la cellule sur le canvas
            x1 = colonne * taille_cellule
            y1 = ligne * taille_cellule
            x2 = x1 + taille_cellule
            y2 = y1 + taille_cellule

            # Récupération de la cellule à la position donnée
            cellule = maze.cellule(ligne, colonne)
            murs = cellule.getwalls()  # Récupère les murs de la cellule

            # Dessin de la cellule (fond de la cellule)
            canvas.create_rectangle(y1, x1, y2, x2, fill=couleur_chemin, outline=couleur_chemin)

            # Dessin des murs si présents
            if murs['N']:  # Mur nord
                canvas.create_line(y1, x1, y2, x1, fill=couleur_mur, width=epaisseur_mur)
            if murs['S']:  # Mur sud
                canvas.create_line(y1, x2, y2, x2, fill=couleur_mur, width=epaisseur_mur)
            if murs['E']:  # Mur est
                canvas.create_line(y2, x1, y2, x2, fill=couleur_mur, width=epaisseur_mur)
            if murs['O']:  # Mur ouest
                canvas.create_line(y1, x1, y1, x2, fill=couleur_mur, width=epaisseur_mur)

def changer_couleur_case(canvas, ligne, colonne, couleur):
    """
    Fonction pour changer la couleur d'une cellule spécifique dans le labyrinthe.
    - canvas : widget tkinter où le labyrinthe est dessiné.
    - ligne : indice de la ligne de la cellule.
    - colonne : indice de la colonne de la cellule.
    - couleur : nouvelle couleur de la cellule.
    """
    x1 = colonne * taille_cellule
    y1 = ligne * taille_cellule
    x2 = x1 + taille_cellule
    y2 = y1 + taille_cellule

    # Redessine la cellule avec la couleur spécifiée
    canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline=couleur)
    
def trajet(canvas, fenetre, solution, index=1):
    """
    Affiche progressivement le chemin de la solution sur le canvas.
    - canvas : widget tkinter où le labyrinthe est dessiné.
    - fenetre : la fenêtre tkinter principale.
    - solution : liste des coordonnées représentant le chemin de la solution.
    - index : étape actuelle du trajet (par défaut 1).
    """
    if index < len(solution):  # Tant que l'on n'a pas atteint la fin de la solution
        # Colorie la cellule actuelle en vert pour marquer le chemin
        changer_couleur_case(canvas, solution[index][1], solution[index][0], "green")
        # Planifie l'affichage de la prochaine cellule après 100 ms
        fenetre.after(100, trajet , canvas, fenetre, solution, index + 1)

def Labyrinthe_affichage(taille, seed, bouton, Fenetre_menu):
    """
    Fonction qui crée et affiche le labyrinthe avec les paramètres donnés.
    - taille : taille du labyrinthe.
    - seed : valeur aléatoire pour générer le labyrinthe.
    - bouton : bouton tkinter qui permet d'afficher le labyrinthe.
    - Fenetre_menu : fenêtre du menu principal.
    """
    if taille != "":  # Si la taille n'est pas vide
        if int(taille) < 26:  # Taille maximale du labyrinthe (pour un affichage correct)
            Laby = Maze(int(taille))  # Création du labyrinthe avec la taille spécifiée

            MM(Laby, seed)  # Génération du labyrinthe avec la seed donnée

            fenetre = tk.Tk()  # Création d'une nouvelle fenêtre tkinter
            fenetre.title(seed)  # Titre de la fenêtre est la seed

            canvas_largeur = Laby.longeur * taille_cellule  # Largeur du canvas
            canvas_hauteur = Laby.hauteur * taille_cellule  # Hauteur du canvas

            canvas = tk.Canvas(fenetre, width=canvas_largeur, height=canvas_hauteur, bg="white")
            canvas.pack()  # Ajout du canvas à la fenêtre tkinter

            dessiner_labyrinthe(canvas, Laby)  # Dessin du labyrinthe sur le canvas

            # Marquer le départ et l'arrivée dans le labyrinthe
            for ligne in Laby.getmaze():
                for cellules in ligne:
                    if cellules.is_depart():  # Si la cellule est le départ
                        changer_couleur_case(canvas, cellules.coord()[0], cellules.coord()[1], "green")
                    if cellules.is_arriver():  # Si la cellule est l'arrivée
                        changer_couleur_case(canvas, cellules.coord()[0], cellules.coord()[1], "red")

            solver = A_Star(Laby)  # Création du solveur pour résoudre le labyrinthe
            solution = solver.solve()  # Résolution du labyrinthe
            print(solution)  # Affichage de la solution dans la console

            # Création du bouton pour afficher le chemin
            bouton = tk.Button(fenetre, text="Voir le chemin", command=lambda: (trajet(canvas, fenetre, solution), bouton.config(state="disabled")))
            bouton.pack(pady=20)  # Affichage du bouton

            fenetre.mainloop()  # Lancement de la boucle principale de tkinter
        else:
            bouton.config(state="disabled")  # Désactive le bouton si la taille est trop grande
            bouton_shake(bouton, Fenetre_menu)  # Applique un effet de secousse au bouton
    else:
        bouton.config(state="disabled")  # Désactive le bouton si la taille est vide
        bouton_shake(bouton, Fenetre_menu)  # Applique un effet de secousse au bouton

def bouton_shake(bouton, Fenetre_menu, value=3, boucle=0):
    """
    Fonction qui fait secouer un bouton pour attirer l'attention.
    - bouton : bouton tkinter à secouer.
    - Fenetre_menu : fenêtre principale où le bouton est affiché.
    - value : amplitude du mouvement de secousse (par défaut 3).
    - boucle : compteur pour limiter le nombre de secousses (par défaut 0).
    """
    if boucle < 4:  # Limite le nombre de secousses à 4
        # Obtenir la position actuelle du bouton
        x = bouton.winfo_x()
        y = bouton.winfo_y()

        # Appliquer un décalage pour secouer le bouton
        bouton.place(x=value-5 ,y=0)  # Appliquer le décalage

        # Revenir à la position initiale après un court délai
        Fenetre_menu.after(100, bouton_shake, bouton, Fenetre_menu, -value, boucle + 1)
    else:
        bouton.place(x=0 ,y=0)  # Revenir à la position initiale après les secousses
        bouton.config(state="active")  # Réactive le bouton

def menu():
    """
    Fonction qui crée et affiche le menu principal.
    Permet à l'utilisateur de saisir les paramètres du labyrinthe.
    """
    fenetre = tk.Tk()  # Création de la fenêtre principale
    fenetre.title("Menu")  # Titre de la fenêtre
    fenetre.geometry("500x500")  # Taille de la fenêtre

    canvas = tk.Canvas(fenetre, width=500, height=500, bg="white")  # Création du canvas pour le menu
    canvas.pack(fill="both", expand=True)  # Ajout du canvas à la fenêtre

    # Création des champs de saisie pour la taille et la seed
    entry_taille = tk.Entry(fenetre)
    entry_taille.place(relx=0.5, rely=0.3, anchor="center")  # Champ pour la taille du labyrinthe
    entry_seed = tk.Entry(fenetre)
    entry_seed.place(relx=0.5, rely=0.4, anchor="center")  # Champ pour la seed

    # Création du bouton pour lancer la génération du labyrinthe
    bouton = tk.Button(
        fenetre,
        text="Go",
        command=lambda: Labyrinthe_affichage(entry_taille.get(), entry_seed.get(), bouton, fenetre),
    )
    bouton.place(relx=0.5, rely=0.5, anchor="center")  # Centrer le bouton dans la fenêtre

    fenetre.mainloop()  # Lancement de la boucle principale de tkinter

# Point d'entrée du programme
if __name__ == "__main__":
    menu()  # Appel de la fonction menu pour démarrer l'application
