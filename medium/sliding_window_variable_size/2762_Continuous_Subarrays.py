'''
    You are given a 0-indexed integer array nums. A subarray of nums is called 
    continuous if:
    Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of 
    indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
    Return the total number of continuous subarrays.
    A subarray is a contiguous non-empty sequence of elements within an array.
'''
from collections import deque
class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        res = 0
        left = 0
        if len(nums) == 1:
            return nums[0]
        
        min_deq = deque()
        max_deq = deque()

        for right in range(len(nums)):
            while max_deq and nums[max_deq[-1]] < nums[right]:
                max_deq.pop()
            max_deq.append(right)

            while min_deq and nums[min_deq[-1]] > nums[right]:
                min_deq.pop()
            min_deq.append(right) 
            
            
            while nums[max_deq[0]] - nums[min_deq[0]] > 2:
                left += 1
                if max_deq[0] < left:
                    max_deq.popleft()
                if min_deq[0] < left:
                    min_deq.popleft()

            res += right-left+1
        print(res)
        return res

assert Solution().continuousSubarrays(nums = [5,4,2,4]) == 8