class Solution():
    def find_peak_point(self, nums: [int]):
        pre = -2**32
        for i,v in enumerate(nums):
            if v< pre:
                return i-1
            pre = v
        return i


if __name__ == '__main__':
    print(Solution().find_peak_point([3,2,1]))