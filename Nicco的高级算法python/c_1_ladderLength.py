class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return -1
        queue: [] = [beginWord]
        cnt = 1
        visited: {} = {}
        not_used: [] = [c for c in wordList]
        while queue:
            cnt += 1
            for k in range(len(queue)):
                cur = queue.pop(0)
                for i in range(len(not_used) - 1, -1, -1):
                    c: str = not_used[i]
                    if self.can_transfer(cur, c):
                        queue.append(c)
                        not_used.pop(i)
                        visited[c] = min(visited.get(c, 1e7), cnt)
        return visited.get(endWord, 0)

    def can_transfer(self,cur, c):
        cnt = 0
        for i, j in zip(cur, c):
            if i != j:
                cnt += 1
        return cnt == 1





if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # print(can_transfer('hitt', 'hote'))
    print(Solution().ladderLength(beginWord, endWord, wordList))
