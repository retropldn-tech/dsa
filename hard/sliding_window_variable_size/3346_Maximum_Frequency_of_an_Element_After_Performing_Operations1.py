'''
    You are given an integer array nums and two integers k and numOperations.
    You must perform an operation numOperations times on nums, where in each operation you:
    Select an index i that was not selected in any previous operations.
    Add an integer in the range [-k, k] to nums[i].
    Return the maximum possible frequency of any element in nums after 
    performing the operations.
'''

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        nums.sort()
        res = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2*k*numOperations:
                left += 1
            res = max(res, right-left)
        print(res)
        return res

assert Solution().maxFrequency(nums = [1,4,5], k = 1, numOperations = 2) == 2
assert Solution().maxFrequency(nums = [5,11,20,20], k = 5, numOperations = 1) == 2