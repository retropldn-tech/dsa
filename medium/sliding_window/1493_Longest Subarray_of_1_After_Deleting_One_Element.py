'''
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.
'''

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        begin = 0 
        window_state = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                window_state += 1

            while window_state>1:
                if nums[begin] == 0:
                    window_state -= 1
                begin += 1
            result = max(result, i-begin+1)
        print(result)
        return result-1


assert Solution().longestSubarray(nums = [1,1,0,1]) == 3
assert Solution().longestSubarray(nums = [0,1,1,1,0,1,1,0,1]) == 5