'''
Description: Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        postfix = 1
        prefix = 1
        res = [None] * length
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*postfix
            postfix = postfix * nums[i]
            
        return res
assert Solution().productExceptSelf(nums = [1,2,3,4]) == [24,12,8,6]
assert Solution().productExceptSelf(nums = [-1,1,0,-3,3]) == [0,0,9,0,0]