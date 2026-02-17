'''
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place 
    such that each unique element appears at most twice. The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages, you must instead have the result 
    be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, 
    then the first k elements of nums should hold the final result. It does not matter what you leave beyond 
    the first k elements.
'''

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 2:
            return nums
        
        write = 1
        counter = 1
        for read in range(1, len(nums)):
            
            if nums[read] == nums[read-1]:
                counter += 1
            else:
                counter = 1
            
            nums[write] = nums[read]

            if counter <= 2:
                write += 1

        print(nums[:write])
        return nums[:write]
            
            

        

Solution().removeDuplicates(nums=[1,1,2,2,2,2,3,3])

[
    -10, -10, -10, -9, -9, -9, -8, -8, -8, 
    -7, -7, -7, -6, -6, -6, -5, -5, -5, -4, 
    -4, -4, -3, -3, -3, -2, -2, -2, -1, -1, 
    -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 
    4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 
    8, 8, 9, 9, 9, 10, 10, 10    
]