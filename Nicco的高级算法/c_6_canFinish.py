"""
有向图的环的检测
1、dfs
2、入度，每次将入度为0的去掉
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]):
        # 统计每个节点的入度
        input_lst: [] = [0 for _ in range(numCourses)]
        for match in prerequisites:
            cur_input = match[1]
            input_lst[cur_input] = input_lst[cur_input] + 1
        # 去掉入度为0的点
        queue: [] = [i for i, v in enumerate(input_lst) if v == 0]
        visited = [i for i in range(numCourses)]
        while queue:
            for i in range(len(queue)):
                c = queue.pop(0)
                visited.remove(c)
                for match in prerequisites:
                    if c == match[0]:
                        out = match[1]
                        input_lst[out] -= 1
                        if input_lst[out] == 0:
                            queue.append(out)
        return len(visited) == 0


if __name__ == '__main__':
    n = 2
    m = [[0, 1]]
    print(Solution().canFinish(n, m))


