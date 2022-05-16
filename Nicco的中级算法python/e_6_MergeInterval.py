from typing import List


def MergeInterval(intervals: List[List[int]]):
    sorted(intervals, key=lambda x: x[0])
    for i in range(len(intervals) - 1, -1, -1):
        cur = intervals[i]
        next = intervals[i + 1] if i + 1 < len(intervals) else None
        if next and cur[1] >= next[0]:
            if cur[1] < next[1]:
                cur[1] = next[1]
            intervals.pop(i + 1)
    return


if __name__ == '__main__':
    tests = [
        [[1, 3], [2, 6], [8, 10], [15, 18]]
        , [[1, 4], [4, 5]]
        , []
        , [[1, 2]]
    ]
    for a in tests:
        print(a)
        MergeInterval(a)
        print(a)
