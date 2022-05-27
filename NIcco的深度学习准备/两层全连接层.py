# 实现一个两层的全连接层，中间层为relu，输出层为softmax，并编写relu和softmax函数
import numpy as np


def relu(x):
    return np.maximum(x, 0)


def softmax(vec: np.ndarray) -> np.ndarray:
    return np.exp(vec) / np.sum(np.exp(vec))


def dense(input: np.ndarray, hidden_size: int) -> np.ndarray:
    m, n = input.shape
    w = np.random.rand(n, hidden_size)
    b = np.random.rand(hidden_size, 1).T
    h = relu(np.dot(input, w) + b)
    o = softmax(h)
    return o


def dense2(input: np.ndarray, hidden_size1: int, hidden_size2: int) -> np.ndarray:
    m, n = input.shape
    w1 = np.random.rand(n, hidden_size1)
    b1 = np.random.rand(hidden_size1, 1).T
    w2 = np.random.rand(hidden_size1, hidden_size2)
    b2 = np.random.rand(hidden_size2, 1).T
    h1 = relu(np.dot(input, w1) + b1)
    h2 = relu(np.dot(h1, w2) + b2)
    o = softmax(h2)
    return o


if __name__ == "__main__":
    # input = np.random.random((3, 10))
    # o = dense(input, 6)
    # print(o)
    input = np.random.random((3, 10))
    o = dense2(input, 6,4)
    print(o)