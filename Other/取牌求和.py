# A和B从n堆牌取牌，每次取一张，A取牌顶，B取牌底，都希望取完后总权重和大于对面的总权重，那么求解最终各自的总权重是多少。

import numpy as np
import queue

pokes = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def get_sum(pokes):
    n = len(pokes)
    sum_A = 0
    sum_B = 0
    num = sum(len(i) for i in pokes)    # 总牌数
    flag_one = 0
    while num > 0:
        # 选牌顶最大的牌
        max_A1 = [0, 0]
        max_A1_idx = -1
        max_A2_idx = -1
        max_A2 = 0
        for i in range(n):
            if len(pokes[i]) > 0:
                flag_one = 1 if len(pokes[i]) == 1 else 0
                if pokes[i][0] + flag_one > sum(max_A1):
                    max_A1[0] = pokes[i][0]
                    max_A1[1] = flag_one
                    max_A1_idx = i
            if len(pokes[i]) > 1:
                if pokes[i][1] > max_A2:
                    max_A2 = pokes[i][1]
                    max_A2_idx = i
        if(max_A1[0]>=max_A2):
            sum_A += max_A1[0]
            pokes[max_A1_idx].pop(0)
        else:
            sum_A += max_A2
            pokes[max_A2_idx].pop()
        num -= 1
        if(num<=0): break
        # 选牌底最小的牌
        min_B1 = [0, 0]
        min_B1_idx = -1
        min_B2_idx = -1
        min_B2 = 0
        for i in range(n):
            if len(pokes[i]) > 0:
                flag_one = 1 if len(pokes[i]) == 1 else 0
                if pokes[i][-1] + flag_one > sum(min_B1):
                    min_B1[0] = pokes[i][-1]
                    min_B1[1] = flag_one
                    min_B1_idx = i
            if len(pokes[i]) > 1:
                if pokes[i][-2] < min_B2:
                    min_B2 = pokes[i][-2]
                    min_B2_idx = i
        if min_B1[0]<=min_B2:
            sum_B += min_B1[0]
            pokes[min_B1_idx].pop(0)
        else:
            sum_B += min_B2
            pokes[min_B2_idx].pop()
        num -= 1
        if(num<=0): break
    return sum_A, sum_B






