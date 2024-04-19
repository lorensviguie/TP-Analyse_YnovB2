# TP-Analyse_YnovB2: Analyse et Prédiction des Dés

## Table des matières

[Objectif](#1-objectif)
[Génération de données](#2-génération-de-données)
[Analyse des données](#3-analyse-des-données)
[Apprentissage automatique](#4-apprentissage-automatique)
[Conclusion](#conclusion)

## 1. Objectif

L'objectif de ce projet est de générer un ensemble de données contenant les lancers de dés, la graine utilisée et le rang du dé. Ces données seront utilisées pour analyser les résultats des différents dés et tenter de les équilibrer pour une expérience de jeu plus équitable. De plus, une intelligence artificielle (IA) sera développée pour prédire les résultats des dés en fonction de la graine et du rang.

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

Un modèle de réseau neuronal de base est utilisé, comme expliqué dans [la présentation](./data_analyse/Machine_learning/Présentation%20IA.pptx)  Le modèle est modifié pour inclure la propagation vers l'avant et la rétropropagation afin d'entraîner le réseau et d'évaluer ses progrès.

### 4.2 Encodage des données d'entrée

Le modèle initial était conçu pour des entrées et des sorties binaires. Pour prendre en compte trois valeurs d'entrée (nom du dé, rang et graine), le nom du dé et le rang sont combinés pour créer des identifiants de dé uniques allant de 1 à 70 (première partie du code avant d'exécuter l'IA).

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
