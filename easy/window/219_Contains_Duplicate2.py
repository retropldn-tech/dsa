'''
    Given an integer array nums and an integer k, 
    return true if there are two distinct indices i and j in 
    the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l = 0
        r = len(nums) - 1
        window = set()
        while r <= len(nums) -1:
            if r-l >k:
                window.remove(nums[l])
                l -=1
            if nums[r] in window:
                return True
            r+=1
            window.add(nums[r])
        return False
assert Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3) == True