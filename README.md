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

English :

The goal of this higher exercise is to manipulate lists but in a slightly more advanced way. If
you haven't completed the previous exercises, go back, it's important to do them first!
In this exercise, you will implement a very well-known card game, battle! The rules in
are relatively simple.
A deck of 52 cards is shuffled and divided into two equal parts distributed to each of the two
players.
Each player places a card face up, the highest of the two wins and the player who placed it
wins both cards. The order of the cards goes from 2 (the lowest) to Ace which is the highest.
If the cards are equal, each player places one card, face down, and a second card, face down.
visible. The player with the highest card wins the 6 on the table.
If they are equal again, we start the same process again.
The cards won are returned to the bottom of the player's deck.
This system will continue as long as both players have cards. Whoever has none left has lost the game!
To implement this, you will have to start by finding how to represent the card game in
memory... For the exercise, I suggest you do it in a list of lists. Each element of
main list is a sublist that represents a card having a value and a suit... By
example ["Ace", "Spades"] will represent the ace of spades... The main list will therefore be of the form:
[['2', 'Clubs'], ['9', 'Diamonds'], ['Queen', 'Diamonds'], ['4', 'Diamonds'], ['5', 'Hearts'] , ['Ace', 'Spade'], ...etc
Find out how to fill out the list containing the complete game as simply as possible. Think
to list comprehensions...
Then, mix the packet and divide it into two equal parts j1 and j2
And finally, implement the game algorithm... The cards will be removed from the start of the lists j1 and
j2, compared, and depending on the situation, added directly to the end of the winner's packet or stored
in new lists allowing the situation of equality to be managed. The winner then collects at the end
from his list all the cards from the lists that have been played.
