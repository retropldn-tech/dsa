'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should 
be kept the same. Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. 
After removing duplicates, return the number of unique elements k. The first k elements of nums should 
contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_unique_ind = 0
        cnt_unique_nums = 1
        for i in range(len(nums)):
            if nums[last_unique_ind] != nums[i]:
                last_unique_ind+=1
                cnt_unique_nums+=1
                nums[last_unique_ind], nums[i] = nums[i], nums[last_unique_ind]
        return nums[:cnt_unique_nums]
assert Solution().removeDuplicates(nums = [1,1,2,3,4]) == [1,2,3,4]