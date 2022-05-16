def b_search(nums:[int], target):
    if not nums:
        return -1
    st = 0
    end = len(nums) - 1
    while st < end:
        mid = st + (end - st) //2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            end = mid
        else:
            st = mid+1
    if nums[st] == target:
        return st
    return -1


def search_rv(nums):
    st = 0
    end = len(nums) -1
    while st<end:
        mid = st+ (end-st)//2
        if nums[mid] > nums[mid+1]:
            return mid
        if nums[mid] >= nums[len(nums) - 1]:
            st = mid + 1
        else:
            end = mid
    return st



def SearchReverseInt(nums: [int], target) -> int:
    if not nums:
        return -1
    rverse_idx: int = search_rv(nums)
    a = b_search(nums[:rverse_idx+1], target)
    b = b_search(nums[rverse_idx+1:], target)
    if a != -1:
        return a
    elif b!= -1:
        return b+rverse_idx+1
    return -1


ts = [
    [4,5,6,1,2,3],
    [1,2,3],
    [1],
    []
    ]

for t in ts:
    print(t)
    print(SearchReverseInt(t,5))