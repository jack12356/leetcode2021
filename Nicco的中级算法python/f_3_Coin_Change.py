
"""
只找到最少的硬币数，用动态规划

升级： 如果要找出一共多少种组合，可以用dp
dp[i][sum]表示用前i中硬币组合成sum的不同组合数
那么dp[i][sum] = dp[i-1][sum]+dp[i-1][sum-Vm]+dp[i-1][sum-2*Vm]+dp[i-1][sum-3*Vm]+...dp[i-1][sum-sum//Vm * Vm]
"""
def Coin_Change(nums: [int],target:int) -> int:
    dp: [int] = [1e7 for _ in range(target+1)]
    for i in range(target+1):
        if i in nums:
            dp[i] = 1
            continue
        for n in nums:
            if i-n >=0:
                dp[i] = min(dp[target], dp[i-n]+1)
    return dp[target] if dp[target]!=1e7 else -1


if __name__ == '__main__':
    print(Coin_Change([5], 3))
