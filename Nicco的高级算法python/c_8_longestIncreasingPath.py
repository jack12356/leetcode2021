class Solution:
    def longestIncreasingPath(self, matrix: [[]]) -> int:
        if not matrix:
            return 0
        visited: [[]] = [[0 for _ in range(len(matrix[0]))] for _ in range(matrix)]
        max_v = -10 ** 7
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cur_len = self.fin_longest_len(matrix, visited, i, j, -10 ** 7)
                max_v = max(max_v, cur_len)
        return max_v

    def fin_longest_len(self, matrix, visited, i, j, pre):
        if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or matrix[i][j] <= pre:
            return 0
        if visited[i][j] != 0:
            return visited[i][j]
        cur = matrix[i][j]
        up = self.fin_longest_len(matrix, visited, i - 1, j, cur)
        down = self.fin_longest_len(matrix, visited, i + 1, j, cur)
        lf = self.fin_longest_len(matrix, visited, i, j - 1, cur)
        rt = self.fin_longest_len(matrix, visited, i, j + 1, cur)
        visited[i][j] = max(up, down, lf, rt) + 1
        return visited[i][j]
