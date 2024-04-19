# TP-Analyse_YnovB2: Analyse et Prédiction des Dés

## Table des matières

[Objectif](#1-objectif)
[Génération de données](#2-génération-de-données)
[Analyse des données](#3-analyse-des-données)
[Apprentissage automatique](#4-apprentissage-automatique)
[Conclusion](#conclusion)

## 1. Objectif

le but de notre projet est de genere notre porpre jeux de données, qui va contenir des lancer de dés la seed utiliser ainsi que le rank du dé

ces dés viennent d'un autre projet que nous avons qui vise a crée un site qui permet de faire un jeux avec leadeboard classement sur la base d'un jeux de dé ou il existe different dé qui varie eu meme du a leur facteur rang [ici le lien de git](https://github.com/lorensviguie/STOUK-GAME)

une fois ce jeux de données analysé notre objectif est d'analysé les resultats des differents dés, dans un but d'equilibrrage des dés pour malgré la debilité de notre projet faire un jeux un tous petit peu equilibré

dans un deuxieme temps nous allons essayer de crée une IA qui va essayer de predire les resultat des dés en fonction de la seed du dé et du rank

## 2. Génération de données

Le code go dans le répertoire [ici](./work/) génère des lancers de dés et crée un fichier CSV. La variable roll peut être modifiée pour ajuster le nombre de lancers par dé. Le dossier dice contient des fonctions individuelles pour chaque type de dé.

## 3. Analyse des données

[Le répertoire](./data_analysis/) contient des ensembles de données, des notebooks Jupyter pour comparer les dés et les ensembles de données générés à des moments différents. L'analyse utilise principalement Pandas, NumPy et Matplotlib.

### 3.1 Analyse de la moyenne des lancers

Certains dés, comme le dé normal, ont des moyennes aberrantes. Le traçage des moyennes des lancers par rang de dé révèle des déséquilibres importants, en particulier aux rangs comme Maître et Platine où les résultats sont généralement plus faibles. Le codage couleur des graphiques met encore plus en évidence que la plupart des lancers de dés sont inférieurs à 10.

### 3.2 Analyse par histogramme

Les histogrammes pour chaque type de dé montrent que la moyenne des lancers varie considérablement selon le rang du dé. Cela indique que les dés ne sont pas cohérents et que le rang n'a pas d'influence positive sur les résultats des lancers, contrairement à l'objectif initial.

### 3.3 Analyse des graines

Une analyse rapide basée sur la graine a été inconclusive en raison de l'influence des paquets de zéro sur certains dés.

### 3.4 Analyse du temps

Le temps n'affecte pas les résultats, ce qui indique que la randomisation de Go fonctionne bien.

### 3.5 Analyse du rang

Les dés ne sont pas équilibrés et le rang a souvent un impact négatif sur les lancers, en particulier pour les dés Power Rank et Parabole.

## 4. Apprentissage automatique

[prise de note sur l'ia](./data_analyse/Machine_learning/Notes%20de%20cours%20sur%20l’intelligence%20artificielle.pdf)

### 4.1 Modèle de réseau neuronal

notre IA utilise un modele relativement basique
[Lorens a ecrit un powerpoint qui explique comment crée sa premiere IA qui fonctionnent sur un seul neuronnes](./data_analyse/Machine_learning/Présentation%20IA.pptx)
le powerpoint ci dessus explique comment crée un neuronne et pas un reseaux de neuronnes modulaire qui et le type de reseaux que nous allons utilisé il s'agit d'un modele tres basique sur son fonctionnement ou les parametres du reseaux seront fait au pif pour tester

vous trouverez aussi les explication des fonction clé utilise Descente de gradient, fonction Cout, ou le perceptron cependant les problmes que l'on peut resoudre avec un seul neuronnes sont assez binaire pour notre probleme on va avoir besoin d'un reseaux de neuronnes on fait donc evoluer grandement le code. les pricipaux changement sont : l'apparation de la forwardpropagation (dans le modele precedent on entraine le neuronne dans seulement en sens ici on va l'entraine vers l'avant et reconstruire l'entrainement dans le sens inverse pour verifier l'evolution positive de notre modele)et eviter que ca parte en cacahuete trop vite (spoil ca va quand meme mal finir )

### 4.2 Encodage des données d'entrée

[ici le code de base](./data_analyse/Machine_learning/save.py)
[ici le code de notre IA](./data_analyse/Machine_learning/base.py)
on rencontre un premier probleme ce modele basique et concu pour resoudre des problemes binaire en entré et en sortie longueur largeur et toxic ou pas, on sait pas comment faire rentré plus de 2 valeur en entré mais nous on en a 3 on va donc rusé et melangé le nom du dé avec le rang pour crée des dé unique qui vont de 1 a 70 premiere partie du code avant de lancer l'ia

### 4.3 Problème de débordement de mémoire

Les paramètres du réseau neuronal deviennent rapidement trop grands, ce qui entraîne des problèmes de débordement de mémoire. Pour y remédier, le réseau est limité pour réduire la taille des paramètres. Concrètement, la valeur maximale de Z est soustraite pour décaler toutes les valeurs du réseau vers le bas.

### 4.4 Entraînement

Un ensemble de données de 7 millions de lignes est utilisé pour l'entraînement (non diffusé en raison de sa taille mais facilement générable). L'IA est testée avec différentes configurations de réseau:

```python
history = deep_neural_network(X, y, hidden_layers=(70, 140, 200,100), learning_rate=0.01, n_iter=42)
```

la ligne ci-dessus et la dernière et on peut configurer les réseaux de neuronne rajouter des lignes de neuronne et agrandir le nombre comme on veut (on ne garantit pas la bonne santé de votre pc en cas de taille démesurée)on peut aussi changer la vitesse de descente de la descente de gradient et le nombre de fois ou réseau va s'entrainer

on se retrouve donc avec un reseaux de neuronnes completement bridé pour eviter les debordement de memoires et on essaye de l'entraine avec different parametre de configuration de reseaux de neuronnes

Après plusieurs jours de tests et de configuration  différente en conclusion l'ia n'arrive à avoir des résultats satisfaisants
[nos trois meilleur test](./data_analyse/Machine_learning/Figure_1_train1000.png)
[nos trois meilleur test](./data_analyse/Machine_learning/Figure_2_train2.png)
[nos trois meilleur test](./data_analyse/Machine_learning/500neuroneswith45try.png)

data bridée à 7 millions après le pc de Lorens explose

on peut conclure que même avec la seed prédire le resultat de different dé pipé est impossible pour notre ia avec les données que l'on lui a fournies on pourrait penser qu'un jeu de données enorme pourrait marche mais il faudrait la partitioné un plusieur jeux de données et faire un entrainement progressif (entraine l'ia plein de fois en sauvegardant c'est parametre pour)pour la mettre a l'epreuve sur beaucoup plus de données

## conclusion

nos dés sont :
-imprévisibles
-pas du tous equilibrés
