'''
    Given an array of positive integers nums and a positive integer target, 
    return the minimal length of a subarray whose sum is greater than or equal to target. 
    If there is no such subarray, return 0 instead.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        begin = 0
        minimal_len = float('inf')
        cur_sum = 0
        for end in range(len(nums)):
            cur_sum += nums[end]
            
            while cur_sum >= target:
                minimal_len = min(end-begin+1, minimal_len)
                cur_sum -= nums[begin]
                begin += 1
            

        if minimal_len == float('inf'):
            return 0
        return minimal_len



assert Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]) == 2
assert Solution().minSubArrayLen(target = 7, nums = [4,3,1,2,2,3]) == 2
assert Solution().minSubArrayLen(target = 7, nums = [4,3,1,3,2,7]) == 1