# Joe Programming
from Maze import *  # Importation des classes nécessaires pour gérer le labyrinthe
from random import *  # Importation des fonctions pour la génération aléatoire
from Solver import *  # Importation du module de résolution de labyrinthes


def MM(maze, seed_maze=None):
    """
    Générateur de labyrinthe basé sur une version de l'algorithme d'Eller.
    maze : instance de la classe Maze représentant le labyrinthe
    seed_maze : (optionnel) seed initiale pour contrôler les décisions aléatoires
    """
    seed_maze = seedMaker(seed_maze)  # Génération ou mise à jour de la seed
    
    height = maze.hauteur  # Hauteur du labyrinthe
    width = maze.longeur  # Largeur du labyrinthe
    
    # Initialisation d'une matrice assignant une valeur unique à chaque cellule
    cell_values = [[value for value in range(width * row, width * (row + 1))] for row in range(height)]

    # Définition de la cellule de départ (coin supérieur gauche)
    maze.maze[0][0].depart()

    for row in range(height):
        # Étape 1 : Relier aléatoirement les cellules horizontalement dans la ligne actuelle
        for col in range(1, width):
            choice, seed_maze = random_choice(seed_maze)  # Génère une décision aléatoire (0 ou 1)
            if choice:  # Si choice est True, fusionne les cellules horizontalement
                cell_values[row][col] = cell_values[row][col - 1]
                maze.destroy_maze_walls(maze.maze[col][row], "O")  # Détruit le mur à l'ouest

        # Étape 2 : Relier aléatoirement les cellules verticalement vers la prochaine ligne
        if row < height - 1:  # Si ce n'est pas la dernière ligne
            # Création d'un dictionnaire associant chaque valeur à ses indices dans la ligne
            value_dict, size_dict = create_value_dict(cell_values[row])
            exit_dict = {}  # Dictionnaire pour suivre le nombre de connexions verticales par valeur
            
            # Calcul du nombre de connexions nécessaires pour chaque valeur
            for value, size in size_dict.items():
                if size // 2 >= 1:
                    size_dict[value] = size // 2
                exit_dict[value], seed_maze = random_choice(seed_maze, [1, size_dict[value]])
                exit_dict[value] = [exit_dict[value]]
            
            # Connexion verticale des cellules en respectant les contraintes
            for value, indices in value_dict.items():
                used_indices = []  # Liste des indices déjà utilisés pour les connexions
                for _ in range(exit_dict[value][0]):  # Boucle sur le nombre de connexions à effectuer
                    possible_indices = indices
                    exit_index, seed_maze = random_choice(seed_maze, (0, len(possible_indices) - 1))
                    
                    # Recherche d'un index non utilisé
                    while exit_index in used_indices:
                        exit_index, seed_maze = random_choice(seed_maze, (0, len(possible_indices) - 1))
                    
                    used_indices.append(exit_index)
                    exit_index = possible_indices[exit_index]
                    
                    # Mise à jour des valeurs et destruction des murs correspondants
                    cell_values[row + 1][exit_index] = cell_values[row][exit_index]
                    maze.destroy_maze_walls(maze.maze[exit_index][row], "S")  # Détruit le mur au sud
        else:
            # Dernière ligne : connexion horizontale complète
            for col in range(1, width):
                cell_values[row][col] = cell_values[row][col - 1]
                maze.destroy_maze_walls(maze.maze[col][row], "O")
            
            # Définition aléatoire de la cellule finale
            final_col, seed_maze = random_choice(seed_maze, [1, width - 1])
            final_row, seed_maze = random_choice(seed_maze, [0, height - 1])
            maze.maze[final_col][final_row].finale()

def seedMaker(seed_maze):
    """
    Création ou mise à jour de la seed du labyrinthe.
    seed_maze : (optionnel) seed actuelle pour la génération du labyrinthe.
    Retourne une nouvelle seed sous forme de chaîne de caractères.
    """
    if seed_maze is None:  # Si aucune seed n'est fournie
        seed_maze = random()  # Génère une seed aléatoire
        return str(seed_maze)[2:]  # Retourne la seed sous forme d'entier (string)
    else:
        seed(seed_maze)  # Définit la seed pour la génération
        seed_maze = random()  # Génère une nouvelle valeur basée sur la seed
        return str(seed_maze)[2:]

def random_choice(seed_maze, value_range=None):
    """
    Génère une valeur aléatoire basée sur la seed donnée.
    seed_maze : seed actuelle.
    value_range : plage de valeurs possibles sous forme de liste [min, max] (optionnel).
    """
    seed_maze = seedMaker(seed_maze)  # Met à jour la seed
    seed(seed_maze)  # Définit la nouvelle seed
    if value_range is None:  # Si aucune plage n'est spécifiée, retourne True/False
        return randint(0, 1), seed_maze
    else:
        return randint(value_range[0], value_range[1]), seed_maze

def create_value_dict(value_list):
    """
    Crée deux dictionnaires à partir d'une liste de valeurs.
    value_list : liste des valeurs associées aux cellules.
    Retourne :
        - value_dict : dictionnaire associant chaque valeur à une liste de ses indices.
        - size_dict : dictionnaire associant chaque valeur à la taille de sa liste.
    """
    value_dict = {}
    for index, value in enumerate(value_list):
        if value in value_dict:
            value_dict[value].append(index)
        else:
            value_dict[value] = [index]
    size_dict = {value: len(indices) for value, indices in value_dict.items()}
    return value_dict, size_dict

if __name__ == "__main__":
    maze = Maze(25)  # Crée un labyrinthe de taille 25x25

    MM(maze)  # Génère le labyrinthe

    solver = A_Star(maze)  # Initialise un solveur pour le labyrinthe
    solution = solver.solve()  # Résout le labyrinthe
    print(solution)  # Affiche la solution
