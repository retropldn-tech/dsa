'''
    Given a binary array nums, you should delete one element from it.
    Return the size of the longest non-empty subarray containing only 1's in the 
    resulting array. Return 0 if there is no such subarray.
'''

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        res = 0
        zeros_qty = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_qty += 1
            while zeros_qty > 1:
                if nums[left] == 0:
                    zeros_qty -= 1
                left += 1
            res = max(res, right-left+1-zeros_qty)
        return res
    
assert Solution().longestSubarray(nums = [1,1,0,1]) == 3 
assert Solution().longestSubarray(nums = [0,1,1,1,0,1,1,0,1]) == 5