# TP-Analyse_YnovB2
LE tp de b2 manipulation de données 

le but de notre projet est de genere notre porpre jeux de données, qui va contenir des lancer de dés la seed utiliser ainsi que le rank du dé

ces dés viennent d'un autre projet que nous avons qui vise a crée un site qui permet de faire un jeux avec leadeboard classement sur la base d'un jeux de dé ou il existe different dé qiu varie eu meme du a leur facteur rang

une fois ce jeux de données analysé notre objectif est d'analysé les resulat des different dé dans un but d'equilibrrage des dés pour malgré la debilité de notre porjet faire un jeux un tous petit equilibré 

dans un deuxieme temps nous allons essayer de crée une IA qui va essayer de predire les resultat des dés en fonction de la seed du dé et du rank 


## Generation des datasets
[dans le dossier ici present](./work/)
on trouve le code go qui genere les lancer de dé et qui genere le csv

## Analyse des données
[dans le dossier ici presnt](./data_analyse/)

ici on trouve les certain jeux de données les seul que on a push ainsi que dse fichier ipynb qui nous permette de comparé les dé entre eux mais aussi different jeux de données lancer a des heure differente

on peut constaté que l'heure na aucune influence sur les resultat l'aleatoire de go marche pas trop mal (si certain set presente quelque difference significative c'est du a des modifications du fonctionement des dé)

de plus on peut constaté que nos dé sont absolument pas equilibré ce qui été le but 

## machine learning 

[ici une prise de note sur l'ia](./data_analyse/Machine_learning/Notes%20de%20cours%20sur%20l’intelligence%20artificielle.pdf)

notre IA utilise un modele relativement basic  
[Lorens a ecrit un powerpoint qui explique comment crée sa premiere qui fonctionnent sur un seul neuronnes](./data_analyse/Machine_learning/Présentation%20IA.pptx)
vous trouverez ici les explication des fonction clé utilise Descente de gradient fonction Gout ou le perceptron cependant les problmes qu el'on peut reousdre avec un seul neuronnes sont assez binaire pour notre problemes on va avoir besoin d'un reseaux de neurronnes on fait evoluer donc evoluer grandement le code les pricipaux changement sont : l'apparation de la forwardpropagation (dans le modele precedent on entraine le neuronne dans seulement en sens ici on va l'entraine vers l'avant et reconstuire l'entrainement dans le sins inverse pour verifier l'evolution positive de notre modele)

on se retrouve donc avec un reseaux de neuronnes completement bridé pour eviter les debordement de memoires et on essaye de l'entraine avec deifferement parametre differente configuration de reseaus de neuronnes 

apres plusieur jour de test de configuration est different set conclusion l'ia narrive a avoir des resultat satisafaisant data bridée a 7million de ligne plus de ligne nos pc crash 

on peut conclure que meme avec la seed predire le resulatat de different dé pipé est imposible pour notre ia avec les données que l'on lui a fournie 