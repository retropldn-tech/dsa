'''
    You are given an integer array nums and an integer k. Find the maximum subarray 
    sum of all the subarrays of nums that meet the following conditions:
    The length of the subarray is k, and
    All the elements of the subarray are distinct.
    Return the maximum subarray sum of all the subarrays that meet the conditions. 
    If no subarray meets the conditions, return 0.
    A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur_set = set()
        left = 0
        cur_sum = 0
        res = 0
        for right in range(len(nums)):
            while (nums[right] in cur_set) or right-left+1 > k:
                cur_sum -= nums[left]
                cur_set.remove(nums[left])
                left += 1
                
            cur_set.add(nums[right])
            cur_sum += nums[right]

            if len(cur_set) == k:
                print('asdasd')
                res = max(res, cur_sum)
        return res
    
assert Solution().maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3) == 15