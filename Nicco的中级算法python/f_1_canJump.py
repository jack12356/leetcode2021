def canJump(nums:[int]):
    if not nums:
        return  -1
    visit: [bool] = [False for _ in nums]
    visit[0] = True
    for i,v in enumerate(nums):
        if visit[i]:
            for j in range(1,v+1):
                if i+j < len(visit):
                    visit[i+j] = True
    return visit[-1]


if __name__ == '__main__':
    ts = [
        [2,3,1,1,4],
        [3, 2, 1, 0, 4],
        [0,0,0,2]
         ]
    for t in ts:
        print(t)
        print(canJump(t))


