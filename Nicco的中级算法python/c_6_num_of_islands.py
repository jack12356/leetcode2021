from typing import List


def spread(nums, i, j, visited: [[bool]]):
    if 0 <= i < len(nums) and 0 <= j < len(nums[0]) and not visited and nums[i][j] == 1:
        visited[i][j] = True
        spread(nums, i - 1, j, visited)
        spread(nums, i + 1, j, visited)
        spread(nums, i, j - 1, visited)
        spread(nums, i, j + 1, visited)


def num_of_islands(nums: List[List[int]]) -> int:
    if not nums or not nums[0]:
        return 0
    cnt = 0
    visited: [[bool]] = [[False for _ in range(len(nums[0]))] for _ in range(len(nums))]
    for i in range(len([nums])):
        for j in range(len(nums[0])):
            if not visited[i][j] and nums[i][j] == 1:
                spread(nums, i, j, visited)
                cnt += 1
    return cnt


# todo:
#  debug 2->3


if __name__ == '__main__':
    matrix: [[int]] = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    print(num_of_islands(matrix))
