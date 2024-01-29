Français :

Le but de cet exercice supérieur est de manipuler les liste mais de manière un peu plus avancée. Si
vous n'avez pas terminé les exercices précédents, retournez-y, c'est important de les faire d'abord !
Dans cet exercice, vous allez implémenter un jeu de cartes très connu, la bataille ! Les règles en
sont relativement simples.
Un jeu de 52 cartes est mélangé et divisé en deux parties égales distribuées à chacun des deux
joueurs.
Chaque joueur pose une carte, face visible, la plus forte des deux gagne et le joueur qui l'a posée
remporte les deux cartes. L'ordre des cartes va du 2 (la plus faible) à l'As qui est la plus forte.
Si les cartes sont égales, chaque joueur pose une carte, face cachée, et une seconde carte, face
visible. Le joueur ayant posé la carte la plus forte remporte les 6 qui sont sur la table. 
Si elles sont de nouveau égales, on recommence le même procédé.
Les cartes gagnées sont remises sous le paquet du joueur.
Ce système va continuer tant que les deux joueurs ont des cartes. Celui qui n'en a plus, a perdu la partie !
Pour implémenter cela, il va falloir commencer par trouver comment représenter le jeu de cartes en
mémoire... Pour l'exercice, je vous propose de le faire dans une liste de listes. Chaque élément dela
liste principale est une sous-liste qui représente une carte ayant une valeur et une couleur... Par
exemple ["As", "Pique"] représentera l'as de pique... La liste principale sera donc de la forme :
[['2', 'Trefle'], ['9', 'Carreau'], ['Dame', 'Carreau'], ['4', 'Carreau'], ['5', 'Coeur'], ['As', 'Pique'], ...etc
Trouvez déjà comment remplir le plus simplement possible la liste contenant le jeu complet. Pensez
aux compréhensions de listes...
Ensuite, mélangez le paquet et divisez le en deux parties égales j1 et j2
Et finalement, implémentez l'algorithme de jeu... Les cartes seront retirées du début des listes j1 et
j2, comparées, et selon la situation, ajoutées directement à la fin du paquet du gagnant ou stockées
dans des nouvelles listes permettant de gérer la situation d'égalité. Le gagnant récupére alors à la fin
de sa liste toutes les cartes des listes qui ont été jouées.
Chaque coup joué sera affiché et la touche entrée permettra de passer au coup suivant.
Voilà, amusez-vous bien !