class Solution:
    def hamming_weight(self,n):
        cnt = 0
        while n > 0:
            cnt = cnt + n % 2
            n = n >> 1
        return cnt

if __name__ == '__main__':
    print(Solution().hamming_weight(8))
    