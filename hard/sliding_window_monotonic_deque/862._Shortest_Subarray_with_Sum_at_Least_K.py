'''
    Given an integer array nums and an integer k, return the length of the shortest 
    non-empty subarray of nums with a sum of at least k. If there is no such subarray, 
    return -1. A subarray is a contiguous part of an array.
'''
from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # Работаем с префиксами. 
        # Сверху ложим самый манимальный префикс. 
        # Если нашли префикс меньше чем те что есть то удаляем те что больше справа
        # Также надо проверять можем ли мы удалить префикс посредством проверки станет ли текущая сумма подходящей если удалим верхушку

        res = float('inf')
        cur_sum = 0
        dq = deque()

        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= k:
                res = min(res, r+1)

            while dq and cur_sum - dq[0][0] >=k:
                val, index = dq.popleft()
                res = min(res, r-index)

            while dq and dq[-1][0] >= cur_sum:
                dq.pop()

            dq.append((cur_sum, r))
        print(res)
        return -1 if res == float('inf') else res
    

assert Solution().shortestSubarray(nums = [2,-1,2], k = 3) == 3