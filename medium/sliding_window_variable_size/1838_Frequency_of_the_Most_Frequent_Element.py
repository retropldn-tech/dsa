'''
    The frequency of an element is the number of times it occurs in an array.
    You are given an integer array nums and an integer k. In one operation, 
    you can choose an index of nums and increment the element at that index by 1.
    Return the maximum possible frequency of an element after performing at most k operations.
'''

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        left = 0
        max_val = nums[0]
        max_possible_frequency = 1
        max_possible_sum = 0
        cur_sum = 0
        cur_k = k
        for right in range(len(nums)):
            max_val = max(max_val, nums[right])
            max_possible_sum = (max_val * (right-left+1))
            cur_sum += nums[right]
            diff = (max_possible_sum-cur_sum)
            cur_k = k - diff

            while cur_k<0:
                diff = max_val-nums[left]
                cur_k += diff
                cur_sum -= nums[left]
                max_possible_sum -= max_val
                left += 1
            max_possible_frequency = max(max_possible_frequency, right-left+1)
        return max_possible_frequency

assert Solution().maxFrequency(nums = [1,2,4], k = 5) == 3
assert Solution().maxFrequency(nums = [1,4,8,13], k = 5) == 2
assert Solution().maxFrequency(nums = [3,9,6], k = 2) == 1