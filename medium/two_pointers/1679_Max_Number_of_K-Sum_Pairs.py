'''
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.
'''

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        count_sum = 0
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[right] + nums[left] < k:
                left += 1
            else:
                count_sum += 1
                left += 1
                right-=1
        return count_sum

assert Solution().maxOperations(nums = [1,2,3,4], k = 5) == 2
assert Solution().maxOperations(nums = [3,1,3,4,3], k = 6) == 1