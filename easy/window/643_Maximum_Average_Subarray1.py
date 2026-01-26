'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will 
be accepted.
'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        state = 0
        max_sum = float('-inf')
        for end in range(len(nums)):
            state += nums[end]
            if end-start+1 == k:
                max_sum = max(max_sum,state)
                state -= nums[start]
                start += 1
        return max_sum / k

assert Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4) == 12.75