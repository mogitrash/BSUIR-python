import numpy as np

np.random.seed(42)

N = 4


X = np.ones((12, 3))
X[:, 1] = np.arange(N, N + 12)
X[:, 2] = np.random.randint(60, 83, size=(12,))

Y = np.random.uniform(13.5, 18.6, size=(12, 1))

A = np.linalg.inv(X.T @ X) @ (X.T @ Y)

print("Матрица X:")
print(X)

print("\nВектор Y:")
print(Y)

print("\nОценки уравнения регрессии (вектор A):")
print(A)

Y_pred = X @ A
print("\nПроверка уравнения регрессии:")
print(Y_pred)