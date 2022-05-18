def spiralOrder_helper(matrix: [[int]], res: [int]):
    if not matrix:
        return
    res.extend(matrix[0])
    re_m: [[int]] = [[-1 for _ in range(len(matrix) - 1)] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix) - 1):
            re_m[i][j] = matrix[j + 1][len(matrix[0]) - 1 - i]
    spiralOrder_helper(re_m, res)


def spiralOrder(matrix: [[int]]) -> [int]:
    res: [int] = []
    spiralOrder_helper(matrix, res)
    return res


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(spiralOrder(a))
