from typing import List


class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        visited: [] = [0 for _ in range(len(matrix))]
        cnt = 0
        for i in range(len(matrix)):
            if not visited[i]:
                cnt += 1
                self.circle_dfs(matrix, visited, i)
        return cnt

    def circle_dfs(self, matrix, visited, i):
        if visited[i]:
            return
        visited[i] = 1
        for j in range(len(matrix)):
            if not visited[j] and matrix[i][j] == 1:
                self.circle_dfs(matrix, visited, j)


