'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i<= second:
                second = i
            else:
                return True
        return False
    
assert Solution().increasingTriplet(nums = [1,2,3,4,5]) == True
assert Solution().increasingTriplet(nums = [5,4,3,2,1]) == False
assert Solution().increasingTriplet(nums = [2,1,5,0,4,6]) == True

assert Solution().increasingTriplet(nums = [1,2,1,3]) == True
assert Solution().increasingTriplet(nums=[20,100,10,12,5,13]) == True