'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will 
be accepted.
'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        ...
        

assert Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4) == 12.75