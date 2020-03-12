Bouhout Mohsin 17244
Abah Emene 17282

___

# Projet IA Quixo

Dans le cadre du cours "projet informatique" à l'ECAM en BAC 2 Science de l'ingénieur industriel, nous avons dû réalisé une intelligence artificielle pour le jeu "QUIXO"
Celle-ci devait pouvoir affronté d'autre IA ou joueur via une interface web mise à disposition par le professeur(https://github.com/ECAM-Brussels/AIGameRunner)
## Algorithme

Nous avons utilisé la librairie EasyAI permettant de mettre en place des IA assez rapidement et facilement. Cette librairie met à disposition plusieurs algorithmes de recherche dont le principal et ainsi celle que nous avons utilisé : Negamax avec alpha beta pruning Negamax est une simplification de l'algorithme minimax (minmax) qui parcoure les différentes possibilités de la partie tout en essayant de "maximiser" ou "Minimiser" l'état du jeu, c'est a dire que l'algorithme prend en compte le fait que le joueur adverse est intelligent et a son mot à dire et renvoie a chaque tour le meilleur coup possible



## Utilisation
Démarrer le server web
```html

python server.py 

```
Lancer l'IA
```html

python QuixoAI.py <port> 

```
Se rendre sur  [l'adresse du serveur web](http://127.0.0.1:80)  lancé plutot 


![alt text](https://i.ibb.co/swDnC5K/server.png)
nous tombons sur cette interface

il nous suffit alors de renseigné le Nom ,l'IP ("127.0.0.1" en local) ainsi que le port de l'IA (choisit précédement)
clicker sur "Add participant" pour chaque joueur (IA) ensuite de clicker sur le bouton play apparaissant devant chaque combinaison de duel



*Vous pouvez lancer 2 fois la même IA pour pouvoir l'observé s'affronté elle même localement.*

