'''
Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue;
            for j in range(i+1,len(nums)):
                if j > i+1 and  nums[j] == nums[j-1]:
                    continue;
                left = j+1
                right = len(nums)-1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
        return res

assert Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
assert Solution().fourSum(nums = [2,2,2,2,2], target = 8) == [[2,2,2,2]]
assert Solution().fourSum(nums = [3,2,3,-3,1,0], target = 3) == [[-3,0,3,3],[-3,1,2,3]]
assert Solution().fourSum(nums = [1,-1,1,-1,1,-1], target = 2) == [[-1,1,1,1]]