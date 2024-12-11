# Maze-Runner
## Maze Creating Path and Solve it

### Répartition des Tâches

**Jaouen**  
- Développement des classes **Maze**, **Noed**, et **Solver**.

**Tom**  
- Développement de l'interface graphique (**HUD**) permettant de visualiser et interagir avec le labyrinthe.

**Joe**
- Développement de la classe Maze, génération du labyrinthe avec la fonction MM (MazeMaker) et d'autres fonctions associées.

---

### **1. Jaouen - Classe Maze, Noed, et Solver**

#### **Classe Noed**
La classe **Noed** représente une cellule ou un nœud du labyrinthe. Chaque nœud contient des informations sur ses voisins, ses murs et son statut (départ ou arrivée).

- **Attributs** :
  - `murs` : Un dictionnaire représentant les murs du nœud (N, S, E, O).
  - `voisins` : Liste des voisins du nœud (nœuds adjacents).
  
- **Méthodes** :
  - `est_depart()` : Vérifie si le nœud est le point de départ.
  - `est_arrivee()` : Vérifie si le nœud est le point d'arrivée.

#### **Classe Maze**
La classe **Maze** représente l'ensemble du labyrinthe. Elle permet de gérer la structure générale et manipuler les cellules du labyrinthe.

- **Méthodes** :
  - `cellule(ligne, colonne)` : Retourne la cellule (nœud) à une position donnée dans le labyrinthe.
  - `getmaze()` : Retourne l'ensemble des cellules du labyrinthe sous forme de matrice (2D).

#### **Solver (Résolution du Labyrinthe)**
Le module de résolution contient l'algorithme qui permet de résoudre le labyrinthe, par exemple, l'algorithme A*.

- **Méthode principale** :
  - `A_Star()` : Résout le labyrinthe en trouvant le chemin le plus court du départ à l’arrivée.

---

### **2. Tom - Interface Utilisateur (HUD)**

#### **Fonctions de l'HUD**

- **`dessiner_labyrinthe()`**  
  Cette fonction dessine le labyrinthe sur le canevas. Elle parcourt chaque cellule du labyrinthe et dessine les murs (nord, sud, est, ouest) en fonction des données de la cellule.

  - **Paramètres** :
    - `canvas` : Le widget Canvas de tkinter utilisé pour dessiner le labyrinthe.
    - `maze` : L'instance de la classe Maze représentant le labyrinthe.

- **`changer_couleur_case()`**  
  Change la couleur d'une cellule spécifique du labyrinthe sur le canevas.

  - **Paramètres** :
    - `canvas` : Le widget Canvas de tkinter.
    - `ligne` : L'indice de la ligne de la cellule à modifier.
    - `colonne` : L'indice de la colonne de la cellule à modifier.
    - `couleur` : La couleur à appliquer à la cellule.

- **`trajet()`**  
  Affiche progressivement le chemin de la solution sur le canevas, avec un effet d'animation.

  - **Paramètres** :
    - `canvas` : Le widget Canvas de tkinter.
    - `fenetre` : La fenêtre principale de tkinter.
    - `solution` : Liste des coordonnées représentant le chemin de la solution.
    - `index` : L'étape actuelle du trajet (par défaut à 1).

- **`menu()`**  
  Crée et affiche une interface de menu principal permettant à l'utilisateur de saisir les paramètres nécessaires pour générer le labyrinthe (taille et seed).

---

### **3. Joe - Développement de la classe Maze, génération du labyrinthe avec la fonction MM (MazeMaker) et d'autres fonctions associées.**

#### **Fonctions de Génération et Manipulation des Murs**

- **`getnear()`**  
  Cette fonction retourne les nœuds voisins adjacents au nœud spécifié, en fonction de la direction donnée. Si la direction est `None`, elle renvoie tous les voisins adjacents.

  - **Paramètres** :
    - `noed` : Un objet de la classe Noed.
    - `direction` : La direction de recherche (N, S, E, W, ou None).

  - **Retour** :
    - Le(s) nœud(s) voisin(s) correspondant à la direction spécifiée.

- **`getnearjoe()`**  
  Similaire à `getnear()`, mais optimisée pour la manipulation des murs dans la fonction `destroy_maze_walls()`. Elle récupère les voisins adjacents d’un nœud dans un format adapté à la destruction des murs.

  - **Paramètres** :
    - `noed` : Un objet de la classe Noed.
    - `direction` : La direction de recherche (N, S, E, W, ou None).

  - **Retour** :
    - Le(s) nœud(s) voisin(s) correspondant à la direction spécifiée, optimisé pour la destruction des murs.

- **`destroy_maze_walls()`**  
  Cette fonction détruit un mur spécifié sur le nœud et détruit le mur opposé sur le nœud adjacent. Si la direction est `None`, tous les murs et leurs opposés sont détruits.

  - **Paramètres** :
    - `noed` : Un objet de la classe Noed.
    - `direction` : La direction du mur à détruire (N, S, E, W, ou None).

  - **Retour** :
    - La destruction du mur spécifié et de son opposé sur le nœud adjacent.

- **`MM()` (Generator)**  
  La fonction **MM** (MazeMaker) génère un labyrinthe dans l'instance de Maze passée en paramètre en utilisant un algorithme de génération. Elle peut prendre une seed pour produire des labyrinthes spécifiques.

  - **Paramètres** :
    - `maze` : Une instance de la classe Maze à modifier.
    - `seed` (optionnel) : Une valeur aléatoire donnée pour générer un labyrinthe spécifique.

