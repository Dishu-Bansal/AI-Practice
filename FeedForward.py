import numpy as np
import matplotlib.pyplot as plt

Nclass = 500

X1 = np.random.randn(Nclass, 2) + np.array([0, -2])
X2 = np.random.randn(Nclass, 2) + np.array([2, 2])
X3 = np.random.randn(Nclass, 2) + np.array([-2, 2])
X = np.vstack([X1, X2, X3])

Y = np.array([0] * Nclass + [1] * Nclass + [2] * Nclass)

plt.scatter(X[:,0], X[:, 1], c=Y, s=100, alpha=0.5)
plt.show()

D = 2
M = 3
K = 3

w1 = np.random.randn(D, M)
b1 = np.random.randn(M)
w2 = np.random.randn(M, K)
b2 = np.random.randn(K)

def forward(X, w1, b1, w, b2):
    Z = 1 / (1 + np.exp(-X.dot(w1)) - b1)
    A = Z.dot(w2) + b2
    expA = np.exp(A)
    Y = expA / expA.sum(axis=1, keepdims=True)
    return Y

def classification_rte(Y, P):
    n_correct=0
    n_total=0
    for i in range(len(Y)):
        n_total += 1
        if Y[i] == P[i]:
            n_correct +=1
    return float(n_correct) / n_total

P_Y_given_X = forward(X, w1, b1, w2, b2)
P = np.argmax(P_Y_given_X, axis=1)

assert(len(P) == len(Y))

print("Classification rate for randomly chosen weights:", classification_rte(Y, P))