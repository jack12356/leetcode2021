from typing import List


def b_search(matrix, x, y, target) -> bool:
    if (not 0 <= x < len(matrix)) or not (0 <= y < len(matrix[0])):
        return False
    if matrix[x][y] == target:
        return True
    if matrix[x][y] > target:
        return b_search(matrix, x - 1, y, target)
    else:
        return b_search(matrix, x, y + 1, target)


def searchMatrix(matrix: List[List[int]], target) -> bool:
    if not matrix or not matrix[0]:
        return False
    return b_search(matrix, len(matrix) - 1, 0, target)


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(searchMatrix(matrix, 100))
