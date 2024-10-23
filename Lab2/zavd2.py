import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

def create_cubic_spline_matrix(n: int) -> np.ndarray:
    A = np.zeros((n + 1, n + 1))
    for i in range(1, n):
        A[i, i - 1:i + 2] = [1, 4, 1]

    A[0, :2] = [1.5, 0.5]
    A[n, -2:] = [0.5, 1.5]

    return A

def cubic_spline_interpolation(x: np.ndarray, y: np.ndarray):
    n = len(x) - 1
    h = np.diff(x)

    A = create_cubic_spline_matrix(n)

    b = np.zeros(n + 1)
    b[1:n] = 3 * ((y[2:] - y[1:-1]) / h[1:] - (y[1:-1] - y[:-2]) / h[:-1])
    b[0] = 2 * (y[1] - y[0]) / h[0]
    b[n] = 2 * (y[n] - y[n - 1]) / h[n - 1]

    c = solve(A, b)

    a = y[:-1]
    b = np.zeros(n)
    d = np.zeros(n)

    for i in range(n):
        b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    return a, b, c, d


def evaluate_spline(x: np.ndarray, x_new: np.ndarray, a: np.ndarray, b: np.ndarray,
                    c: np.ndarray, d: np.ndarray) -> np.ndarray:
    result = np.zeros_like(x_new, dtype=float)
    n = len(x) - 1

    for i in range(n):
        mask = (x_new >= x[i]) & (x_new <= x[i + 1])
        if np.any(mask):
            dx = x_new[mask] - x[i]
            result[mask] = a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3

    return result

if __name__ == "__main__":
    import matplotlib
    matplotlib.use('TkAgg')

    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 2, 1, 3, 4])
    a, b, c, d = cubic_spline_interpolation(x, y)
    x_new = np.linspace(x[0], x[-1], 200)
    y_new = evaluate_spline(x, x_new, a, b, c, d)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ko', label='Вхідні точки')
    plt.plot(x_new, y_new, 'b-', label='Кубічний сплайн')
    plt.title('Кубічний сплайн зі слабкими граничними умовами')
    plt.legend()
    plt.grid(True)
    plt.show()