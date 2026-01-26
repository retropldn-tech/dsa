'''
Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.
'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        def swap(l: int, r:int) -> None:
            while l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r-=1

        swap(l=0, r=(len(nums)-1)) #<--- swap all
        swap(l=0, r=k-1) # <--- swap right
        swap(l=k, r=(len(nums)-1))

        return nums
    
assert Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3) == [5,6,7,1,2,3,4]
assert Solution().rotate(nums = [1,2,3,4,5,6,7,8], k = 4) == [5,6,7,8,1,2,3,4]
