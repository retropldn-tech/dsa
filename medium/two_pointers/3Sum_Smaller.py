'''

'''

class Solution:
    def threeSumSmaller(self, nums, target):
        count_triplets = 0
        nums.sort()
        for i in range(len(nums)):
            left, right = 0, len(nums)-1
            while left<right:
                if nums[i] + nums[right] + nums[left] < target:
                    count_triplets += 1
                    left += 1
                    right -= 1
                else:
                    right -= 1
        return count_triplets
