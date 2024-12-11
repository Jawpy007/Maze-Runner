# Jaouen et Joe programmation
class Noed:
    """
    Classe représentant une cellule du labyrinthe:
        x, y = coordonnées de la cellule
        walls = murs de la cellule (dictionnaire de directions)
        arriver = indique si c'est la cellule d'arrivée
    """
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {"N": True, "S": True, "E": True, "O": True}
        self.arriver = False
        self.debut = False

    def is_depart(self):
        return self.debut

    def is_arriver(self):
        return self.arriver

    def getwalls(self):
        # Retourne les murs de la cellule
        return self.walls

    def allwalls(self):
        # Vérifie si tous les murs sont intacts
        return all(self.walls.values())

    def coord(self):
        # Retourne les coordonnées de la cellule
        return (self.x, self.y)

    def destroy(self, Who=None):
        """
        Détruit un ou plusieurs murs de la cellule:
        - Si Who est None, détruit tous les murs
        - Sinon, détruit le mur correspondant à la direction donnée
        """
        if Who is None:
            self.walls = {key: False for key in self.walls}
        else:
            self.walls[Who] = False

    def finale(self):
        self.arriver = True

    def depart(self):
        self.debut = True


class Maze:
    def __init__(self, proportion):
        # Génère une grille proportion x proportion de cellules
        self.maze = [[Noed(i, j) for i in range(proportion)] for j in range(proportion)]
        self.longeur = proportion
        self.hauteur = proportion

    def cellule(self, x, y):
        # Retourne la cellule aux coordonnées x, y
        return self.maze[x][y]

    def maze_width(self):
        return self.longeur

    def maze_height(self):
        return self.hauteur

    def getmaze(self):
        return self.maze

    def __str__(self):
        """ Représentation textuelle simple du labyrinthe """
        maze_rows = ['-' * self.longeur * 2]
        for y in range(self.hauteur):
            maze_row = ['|']
            for x in range(self.hauteur):
                maze_row.append(' |' if self.maze[x][y].walls['E'] else '  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.longeur):
                maze_row.append('-+' if self.maze[x][y].walls['S'] else ' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def getnear(self, noed, Who=None):
        """
        Retourne les coordonnées des voisins dans une direction donnée.
        - Who: direction ('N', 'S', 'E', 'O') ou None pour toutes.
        """
        coordN = noed.coord()
        if Who == "N":
            coordNear = [coordN[0], coordN[1] - 1]
        elif Who == "S":
            coordNear = [coordN[0], coordN[1] + 1]
        elif Who == "O":
            coordNear = [coordN[0] - 1, coordN[1]]
        elif Who == "E":
            coordNear = [coordN[0] + 1, coordN[1]]
        elif Who is None:
            return (self.getnear(noed, "N") +
                    self.getnear(noed, "S") +
                    self.getnear(noed, "O") +
                    self.getnear(noed, "E"))
        if -1 < coordNear[0] < self.longeur and -1 < coordNear[1] < self.hauteur:
            return [[Who] + coordNear]
        else:
            return [[Who] + [None, None]]

    def getnearjoe(self, noed, Who=None):
        """
        Variante de getnear avec un ordre de directions différent.
        """
        coordN = noed.coord()
        if Who == "O":
            coordNear = [coordN[0], coordN[1] - 1]
        elif Who == "E":
            coordNear = [coordN[0], coordN[1] + 1]
        elif Who == "N":
            coordNear = [coordN[0] - 1, coordN[1]]
        elif Who == "S":
            coordNear = [coordN[0] + 1, coordN[1]]
        elif Who is None:
            return (self.getnearjoe(noed, "N") +
                    self.getnearjoe(noed, "S") +
                    self.getnearjoe(noed, "O") +
                    self.getnearjoe(noed, "E"))
        if -1 < coordNear[0] < self.longeur and -1 < coordNear[1] < self.hauteur:
            return [[Who] + coordNear]
        else:
            return [[Who] + [None, None]]

    def destroy_maze_walls(self, Cell, Who=None):
        """
        Détruit les murs de la cellule donnée et met à jour les voisins.
        - Who: direction du mur à détruire (ou None pour tous les murs).
        """
        Cell.destroy(Who)  # Détruit le mur de la cellule
        voisins = self.getnearjoe(Cell, Who)  # Récupère les voisins
        for voisin in voisins:
            direction, x, y = voisin
            if x is not None and y is not None:  # Vérifie la validité des coordonnées
                if direction == "N":
                    self.maze[y][x].destroy("S")  # Mur Sud du voisin Nord
                elif direction == "S":
                    self.maze[y][x].destroy("N")  # Mur Nord du voisin Sud
                elif direction == "O":
                    self.maze[y][x].destroy("E")  # Mur Est du voisin Ouest
                elif direction == "E":
                    self.maze[y][x].destroy("O")  # Mur Ouest du voisin Est


if __name__ == "__main__":
    # Tests de base
    Noeu = Noed(0, 0)
    print(Noeu.allwalls())  # True (tous les murs intacts)
    print(Noeu.coord())  # (0, 0)

    print(Noeu.getwalls())  # {"N": True, "S": True, "E": True, "O": True}
    Noeu.destroy("E")  # Détruit le mur Est
    print(Noeu.getwalls())  # {"N": True, "S": True, "E": False, "O": True}

    Laby = Maze(10)
    print(Laby)  # Affichage du labyrinthe

    print(Laby.cellule(0, 0))  # Affiche une cellule
