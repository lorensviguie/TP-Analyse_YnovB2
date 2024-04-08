import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
from tqdm import tqdm
import pandas as pd

def initialisation(dimensions):
    
    parametres = {}
    C = len(dimensions)

    np.random.seed(1)

    for c in range(1, C): 
        parametres['W' + str(c)] = np.random.randn(dimensions[c], dimensions[c - 1])
        parametres['b' + str(c)] = np.random.randn(dimensions[c], 1)

    return parametres



def forward_propagation(X, parametres):
  
  activations = {'A0': X}

  C = len(parametres) // 2

  for c in range(1, C + 1):

    W = parametres['W' + str(c)]
    b = parametres['b' + str(c)]
    A_prev = activations['A' + str(c - 1)]

    Z = W.dot(A_prev) + b
    activations['A' + str(c)] = 1 / (1 + np.exp(-Z))

  return activations




def back_propagation(y, parametres, activations):

  m = y.shape[1]
  C = len(parametres) // 2

  dZ = activations['A' + str(C)] - y
  gradients = {}

  for c in reversed(range(1, C + 1)):
    gradients['dW' + str(c)] = 1/m * np.dot(dZ, activations['A' + str(c - 1)].T)
    gradients['db' + str(c)] = 1/m * np.sum(dZ, axis=1, keepdims=True)
    if c > 1:
      dZ = np.dot(parametres['W' + str(c)].T, dZ) * activations['A' + str(c - 1)] * (1 - activations['A' + str(c - 1)])

  return gradients

def update(gradients, parametres, learning_rate):

    C = len(parametres) // 2

    for c in range(1, C + 1):
        parametres['W' + str(c)] = parametres['W' + str(c)] - learning_rate * gradients['dW' + str(c)]
        parametres['b' + str(c)] = parametres['b' + str(c)] - learning_rate * gradients['db' + str(c)]

    return parametres



def predict(X, parametres):
  activations = forward_propagation(X, parametres)
  C = len(parametres) // 2
  Af = activations['A' + str(C)]
  return Af >= 0.5

def plot_decision_boundary(X, y, parametres):
    # Définir la grille pour les valeurs possibles de X1 et X2
    x1_min, x1_max = X[0, :].min() - 1, X[0, :].max() + 1
    x2_min, x2_max = X[1, :].min() - 1, X[1, :].max() + 1

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01),
                           np.arange(x2_min, x2_max, 0.01))

    # Prédire les étiquettes pour chaque point de la grille
    Z = predict(np.c_[xx1.ravel(), xx2.ravel()].T, parametres)
    Z = Z.reshape(xx1.shape)

    # Tracer la frontière de décision
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap='summer')

    # Tracer le nuage de points
    plt.scatter(X[0, :], X[1, :], c=y, cmap='summer')
    
    plt.title('Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

def deep_neural_network(X, y, hidden_layers = (16, 16, 16), learning_rate = 0.001, n_iter = 3000):
    
    # initialisation parametres
    dimensions = list(hidden_layers)
    dimensions.insert(0, X.shape[0])
    dimensions.append(y.shape[0])
    np.random.seed(1)
    parametres = initialisation(dimensions)

    # tableau numpy contenant les futures accuracy et log_loss
    training_history = np.zeros((int(n_iter), 2))

    C = len(parametres) // 2

    # gradient descent
    for i in tqdm(range(n_iter)):

        activations = forward_propagation(X, parametres)
        gradients = back_propagation(y, parametres, activations)
        parametres = update(gradients, parametres, learning_rate)
        Af = activations['A' + str(C)]

        # calcul du log_loss et de l'accuracy
        training_history[i, 0] = (log_loss(y.flatten(), Af.flatten()))
        y_pred = predict(X, parametres)
        training_history[i, 1] = (accuracy_score(y.flatten(), y_pred.flatten()))
        
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(training_history[:, 0], label='train loss')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(training_history[:, 1], label='train acc')
    plt.legend()
    plt.show()
    plot_decision_boundary(X, y, parametres)
    return training_history

df = pd.read_csv("./donnees_14h35.csv")


df[['Seed', 'Rank']] = df[['Seed', 'Rank']].apply(pd.to_numeric, errors='coerce')

# Séparation des fonctionnalités (X) et de la variable cible (y)
X = df[['Seed', 'Rank']]
y = df['Résultat']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
history = deep_neural_network(X_train.T, y_train.values.reshape(1, -1), hidden_layers=(16, 16), learning_rate=0.01, n_iter=100000)

# Extraction des paramètres finaux du modèle
final_params = history[-1]

# Évaluation du modèle sur les données de test
y_pred = predict(X_test.T, final_params)
accuracy = accuracy_score(y_test, y_pred.flatten())
print("Accuracy on test set:", accuracy)