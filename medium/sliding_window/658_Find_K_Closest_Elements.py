'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        res = [float('inf')] * k
        begin = 0
        for end in range(len(arr)):
            while end-begin+1 > k:
                ...

        ...

assert Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3) == [1,2,3,4]
assert Solution().findClosestElements(arr = [1,1,2,3,4,5], k = 4, x = -1) == [1,1,2,3]

assert Solution().findClosestElements(arr = [2,4,5,8], k = 2, x = 6) == [4,5]
assert Solution().findClosestElements(arr = [2,3,4], k = 3, x = 1) == [2,3,4]