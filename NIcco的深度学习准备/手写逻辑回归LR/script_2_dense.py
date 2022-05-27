import numpy as np

input_data: np.ndarray = np.ndarray((5, 7))
label: np.ndarray = np.asmatrix([
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, ],
    [1, 0, 0, 0, ]
])


def softmax(vec):
    return np.exp(vec) / np.sum(np.exp(vec))


def relu(x):
    return np.maximum(x, 0)


def dense_2(input_data: np.ndarray, hidden_size1: int, hidden_size2: int):
    n_samples, f_sizes = input_data.shape
    w1: np.ndarray = np.ndarray((f_sizes, hidden_size1))
    b1: np.ndarray = np.ndarray((hidden_size1, 1)).transpose()
    w2: np.ndarray = np.ndarray((hidden_size1, hidden_size2))
    b2: np.ndarray = np.ndarray((hidden_size2, 1)).transpose()
    h1: np.ndarray = relu( np.dot(input_data, w1) + b1)
    h2: np.ndarray = relu(np.dot(h1, w2) + b2)
    return softmax(h2)



if __name__ == '__main__':
    print(dense_2(input_data,8,4))
