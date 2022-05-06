from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.FLAG: int = -2 ** 32
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.set_flag(matrix, i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == self.FLAG:
                    matrix[i][j] = 0

    def set_flag(self, matrix, i, j):
        for k in range(len(matrix)):
            matrix[k][j] = self.FLAG if matrix[k][j] != 0 else 0
        for k in range(len(matrix[0])):
            matrix[i][k] = self.FLAG if matrix[i][k] != 0 else 0


if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(matrix)
    print(matrix)
