'''
    Given an integer array nums, return all the triplets 
    [nums[i], nums[j], nums[k]] such that 
    i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = list()
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l<r:
                if (nums[i] + nums[l] + nums[r]) == 0:
                    k = [nums[i], nums[l], nums[r]]
                    ans.append(k)
                    l+=1
                    r-=1
                    while nums[l-1] == nums[l] and l<r:
                        l += 1

                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
        return ans

assert Solution().threeSum(nums = [-1,0,1,2,-1,-4])==[[-1,-1,2],[-1,0,1]]