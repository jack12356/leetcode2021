from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board or not board[0]:
            return False
        visited: [[]] = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        find = [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.exist_helper(board, word, 0, i, j, visited, find)
        return find[0]

    def exist_helper(self, board, word, idx, i, j, visited, find):
        if idx == len(word):
            find[0] = True
            return
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and not visited[i][j] and word[idx] == board[i][j] and not find[0]:
            visited[i][j] = True
            self.exist_helper(board, word, idx + 1, i - 1, j, visited, find)
            self.exist_helper(board, word, idx + 1, i + 1, j, visited, find)
            self.exist_helper(board, word, idx + 1, i, j - 1, visited, find)
            self.exist_helper(board, word, idx + 1, i, j + 1, visited, find)
            visited[i][j] = False
