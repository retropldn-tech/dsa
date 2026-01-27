'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
in the array if you can flip at most k 0's.
'''

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        cur_k = 0
        max_len = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                cur_k += 1

            while cur_k > k:
                if nums[left] == 0:
                    cur_k -= 1
                left += 1

            max_len = max(end-left+1, max_len)
        return max_len
assert Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2) == 6
