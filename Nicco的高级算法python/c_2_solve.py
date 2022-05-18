from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = len(board)
        l0 = len(board[0])
        # 从外面往里面DFS
        for i in range(l):
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            if board[i][l0 - 1] == "O":
                self.dfs(board, i, l0 - 1)
        for j in range(l0):
            if board[0][j] == "O":
                self.dfs(board, 0, j)
            if board[l - 1][j] == "O":
                self.dfs(board, l - 1, j)
        for i in range(l):
            for j in range(l0):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return

    def dfs(self, board, i, j):
        if (not 0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] in ["X", "T"]:
            return
        board[i][j] = "T"
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j + 1)
