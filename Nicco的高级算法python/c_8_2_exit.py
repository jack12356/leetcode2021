"""
矩阵中查找字符串
"""


class Solution:
    def exit_word(self, matrix: [[str]], word: str) -> bool:
        if not word or not matrix:
            return False
        visited: [[bool]] = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.dfs(matrix, visited, i, j, 0, word):
                    return True
        return False

    def dfs(self, matrix: [[str]], visited: [[bool]], i, j, idx, word: str) -> bool:
        if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or visited[i][j] or matrix[i][j] != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        visited[i][j] = True
        if self.dfs(matrix, visited, i - 1, j, idx + 1, word) or self.dfs(matrix, visited, i + 1, j, idx + 1, word) or \
                self.dfs(matrix, visited, i, j - 1, idx + 1, word) or self.dfs(matrix, visited, i, j + 1, idx + 1,
                                                                               word):
            return True
        visited[i][j] = False
        return False
