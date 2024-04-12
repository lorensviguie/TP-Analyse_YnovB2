import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles
from sklearn.metrics import accuracy_score, log_loss
from tqdm import tqdm



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

    for c in range(1, C):
        Z = parametres['W' + str(c)].dot(activations['A' + str(c - 1)]) + parametres['b' + str(c)]
        activations['A' + str(c)] = 1 / (1 + np.exp(-Z))
    #overflow numerique de activation
    # Couche de sortie avec activation softmax
    Z_out = parametres['W' + str(C)].dot(activations['A' + str(C - 1)]) + parametres['b' + str(C)]
    Z_out -= np.max(Z_out)  # Stabilisation numérique
    exp_Z_out = np.exp(Z_out)
    activations['A' + str(C)] = np.where(exp_Z_out == 0, 0, exp_Z_out / np.sum(exp_Z_out, axis=0))

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
        parametres['W' + str(c)] -= learning_rate * gradients['dW' + str(c)]
        parametres['b' + str(c)] -= learning_rate * gradients['db' + str(c)]

    return parametres

def predict(X, parametres):
    activations = forward_propagation(X, parametres)
    C = len(parametres) // 2
    softmax_output = activations['A' + str(C)]
    predictions = np.argmax(softmax_output, axis=0)
    return predictions.reshape(1, -1)

def plot_decision_boundary(X, y, parametres):
    x1_min, x1_max = X[0, :].min() - 1, X[0, :].max() + 1
    x2_min, x2_max = X[1, :].min() - 1, X[1, :].max() + 1

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01),
                           np.arange(x2_min, x2_max, 0.01))

    Z = predict(np.c_[xx1.ravel(), xx2.ravel()].T, parametres)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap='summer')
    plt.scatter(X[0, :], X[1, :], c=y, cmap='summer')
    
    plt.title('Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

def normalize_data(X):
    mean = np.mean(X, axis=1, keepdims=True)
    std = np.std(X, axis=1, keepdims=True)
    X_normalized = (X - mean) / std
    return X_normalized, mean, std

def calculate_accuracy_by_index(y_true, y_pred, index_values):
    accuracy_by_index = {}
    unique_index_values = np.unique(index_values)
    for index_value in unique_index_values:
        index_mask = index_values == index_value
        accuracy = accuracy_score(y_true[index_mask], y_pred[index_mask])
        accuracy_by_index[index_value] = accuracy
    return accuracy_by_index

def plot_accuracy_by_index(accuracy_by_index):
    index_values = list(accuracy_by_index.keys())
    accuracy_values = list(accuracy_by_index.values())

    plt.figure(figsize=(10, 6))
    plt.plot(index_values, accuracy_values, marker='o', linestyle='-')
    plt.title('Taux de réussite de la prédiction en fonction de l\'index')
    plt.xlabel('Index')
    plt.ylabel('Taux de réussite de la prédiction')
    plt.grid(True)
    plt.show()


def deep_neural_network(X, y, hidden_layers=(16, 16), learning_rate=0.01, n_iter=10000):
    dimensions = list(hidden_layers)
    dimensions.insert(0, X.shape[0])
    dimensions.append(len(np.unique(y))) 
    np.random.seed(1)
    parametres = initialisation(dimensions)

    # Normaliser les données d'entrée
    X_normalized, mean, std = normalize_data(X)

    training_history = np.zeros((int(n_iter), 2))

    C = len(parametres) // 2
    for i in tqdm(range(n_iter)):
        activations = forward_propagation(X_normalized, parametres)  # Utiliser les données normalisées
        gradients = back_propagation(y, parametres, activations)
        parametres = update(gradients, parametres, learning_rate)
        Af = activations['A' + str(C)]
        training_history[i, 0] = log_loss(y.flatten(), Af.T, labels=np.unique(y))
        y_pred = predict(X_normalized, parametres)  # Utiliser les données normalisées pour la prédiction
        training_history[i, 1] = accuracy_score(y.flatten(), y_pred.flatten())

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(training_history[:, 0], label='train loss')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(training_history[:, 1], label='train acc')
    plt.legend()
    plt.show()
    plot_decision_boundary(X_normalized, y, parametres)  # Utiliser les données normalisées pour le tracé de la frontière de décision

    # Calculer le taux de réussite de la prédiction en fonction de l'index
    accuracy_by_index = calculate_accuracy_by_index(y.flatten(), y_pred.flatten(), df['Index'].values)
    # Tracer le graphique du taux de réussite de la prédiction en fonction de l'index
    plot_accuracy_by_index(accuracy_by_index)
    
    return training_history


df = pd.read_csv("./donnes_14h13_700-000.csv")
df['Index'] = ((df['Nom_dé'] != df['Nom_dé'].shift()) | (df['Rank'] != df['Rank'].shift())).cumsum()
df.dropna(inplace=True)
df.to_csv("./donnees_16h06.csv", index=False)
print("Les modifications ont été enregistrées dans le fichier CSV.")

X = df[['Seed', 'Index']].values.T  # Transpose pour avoir les bonnes dimensions
y = df['Résultat'].values.reshape(1, -1)

print('dimensions de X:', X.shape)
print('dimensions de y:', y.shape)

history = deep_neural_network(X, y, hidden_layers=(70, 140, 200,100), learning_rate=0.01, n_iter=42)
