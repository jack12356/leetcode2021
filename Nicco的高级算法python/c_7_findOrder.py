from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 统计每个节点的入度
        input_lst: [] = [0 for _ in range(numCourses)]
        for match in prerequisites:
            cur_input = match[0]
            input_lst[cur_input] = input_lst[cur_input] + 1
        # 去掉入度为0的点
        queue: [] = [i for i, v in enumerate(input_lst) if v == 0]
        visited = [i for i in range(numCourses)]
        orders: [] = []
        while queue:
            for i in range(len(queue)):
                c = queue.pop(0)
                visited.remove(c)
                orders.append(c)
                for match in prerequisites:
                    if c == match[1]:
                        out = match[0]
                        input_lst[out] -= 1
                        if input_lst[out] == 0:
                            queue.append(out)
        return orders if len(visited) == 0 else []


if __name__ == '__main__':
    n = 2
    m = [[1, 0]]
    print(Solution().findOrder(n, m))