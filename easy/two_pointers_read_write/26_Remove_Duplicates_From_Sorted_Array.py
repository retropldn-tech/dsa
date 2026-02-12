'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should 
be kept the same. Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. 
After removing duplicates, return the number of unique elements k. The first k elements of nums should 
contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        write = 1
        for read in range(1,len(nums)):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1
        return nums[:write]
    
assert Solution().removeDuplicates(nums=[1,1]) == [1]
assert Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4]

assert Solution().removeDuplicates(nums = [1,1,2,3,4]) == [1,2,3,4]

