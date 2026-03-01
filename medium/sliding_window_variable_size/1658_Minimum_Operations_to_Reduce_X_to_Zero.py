'''
    You are given an integer array nums and an integer x. 
    In one operation, you can either remove the leftmost or the rightmost 
    element from the array nums and subtract its value from x. 
    Note that this modifies the array for future operations.
    Return the minimum number of operations to reduce x to exactly 0 if 
    it is possible, otherwise, return -1.
'''

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        left = 0
        max_window = -1
        target = sum(nums) - x
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]

            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
                        
            if cur_sum == target:
                max_window = max(max_window, right-left+1)
        return -1 if max_window == -1 else len(nums) - max_window

assert Solution().minOperations(nums = [1,1,4,2,3], x = 5) == 2
assert Solution().minOperations(nums = [5,6,7,8,9], x = 4) == -1
assert Solution().minOperations(nums = [3,2,20,1,1,3], x = 10) == 5
