import numpy as np

A = np.array([
    [-1.00, 0.28, -0.17, 0.06],
    [0.52, -1.00, 0.12, 0.17],
    [0.17, -0.18, -0.79, 0.00],
    [0.11, 0.22, 0.03, -0.95]
])

B = np.array([-0.21, 1.17, 0.81, -0.72])
X = np.zeros(len(B))

eps = 0.0001


def gauss_seidel(A, B, eps):

    n = len(B)
    X = np.zeros(n)
    iter_count = 0

    while True:
        X_old = np.copy(X)  
        for i in range(n):
            s1 = sum(A[i][j] * X[j] for j in range(i))
            s2 = sum(A[i][j] * X_old[j] for j in range(i + 1, n))

            if A[i][i] == 0:
                raise ValueError(
                    "Діагональний елемент дорівнює нулю. Метод Гаусса-Зейделя не застосовний без перестановки рядків.")

            X[i] = (B[i] - s1 - s2) / A[i][i]

        iter_count += 1

        error = np.max(np.abs(X - X_old))
        if error < eps:
            break

        if iter_count > 1000:
            print(
                "Увага: Досягнуто максимальну кількість ітерацій (1000). Система може бути розбіжною або потребувати більше ітерацій.")
            break

    return X, error, iter_count


solution, error, iterations = gauss_seidel(A, B, eps)

print("Розв'язок (X):")
print(solution)
print("__________________")
print(f"\nПохибка (max(|X_k - X_{{k-1}}|)): {error:.6f}")
print(f"Точність (eps): {eps}")
print(f"Кількість ітерацій: {iterations}")