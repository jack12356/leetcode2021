import numpy as np
from typing import List

# lr sigmoid输出
data = [[1, 2, 3], [0.3, 0.5, 0.9], [0.2, 0.1, 0.5]]
label = [1, 1, 0]


def sigmoid(vec):
    # e^x/(1+e^x)
    return np.exp(vec) / (1 + np.exp(vec))


def grad_descent(data: List[List[float]], label: List[int], epochs: int = 10, alpha: float = 0.05) -> np.ndarray:
    train_data = [[1.0] + _ for _ in data]  # 偏置项置为1
    y_true = np.asmatrix(label).transpose()
    data_mat: np.ndarray = np.asmatrix(data)
    n_samples, f_size = data_mat.shape
    weights: np.ndarray = np.ones((f_size, 1))
    for i in range(epochs):
        h_hat: np.ndarray = sigmoid(data_mat @ weights)
        e: np.ndarray = h_hat - y_true
        weights = weights - alpha * data_mat.transpose() @ e
        print("cur error is {}".format(np.sum(e) / f_size))
    print("weights is: {}".format(weights))
    return weights


if __name__ == "__main__":
    grad_descent(data, label)
