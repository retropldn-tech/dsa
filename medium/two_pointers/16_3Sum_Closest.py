'''
    Given an integer array nums of length n and an integer target, 
    find three integers at distinct indices in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.
'''

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if abs(target - (nums[i] + nums[left] + nums[right])) < abs(target - ans):
                    ans = (nums[i] + nums[left] + nums[right])

                print(ans, i, left, right )

                if (nums[i] + nums[left] + nums[right]) == target:
                    return target
                elif (nums[i] + nums[left] + nums[right]) > target:
                    right -= 1
                elif (nums[i] + nums[left] + nums[right]) < target:
                    left += 1
            
            #closest_sum = min(closest_sum, abs(target - (nums[i] + nums[left] + nums[right])))
        print(ans)
        return ans
assert Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1) == 2
assert Solution().threeSumClosest(nums = [0,0,0], target = 1) == 0