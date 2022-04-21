import numpy as np

datamat: list = [[0.2, 0.6], [0.2, 0.7], [-0.2, -0.7], [-0.2, -0.6]]
class_labels: list = [1, 1, -1, -1]

# 扩充datamat,将x0填补上去
datamat: list = [[1.0] + x for x in datamat]

datamat: np.ndarray = np.asmatrix(datamat)
class_labels: np.ndarray = np.asmatrix(class_labels).transpose()


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + np.exp(-x))
    # return x


def decrese_gradent(datamat: np.ndarray, class_labels: np.ndarray, alpha: float):
    m, n = datamat.shape
    weights: np.ndarray = np.ones((n, 1))
    for i in range(100):
        y_hat = sigmoid(datamat * weights)
        error = y_hat - class_labels
        weights = weights - alpha * datamat.transpose() * error
        print(np.sum(error.flatten())/m)
    return weights


if __name__ == '__main__':
    weights = decrese_gradent(datamat, class_labels, 0.01)
    print(weights)