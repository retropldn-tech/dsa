'''
    Given an array nums with n objects colored red, white, or blue, sort them in-place 
    so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    You must solve this problem without using the library's sort function.
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left = 0
        right = len(nums)-1
        cursor = 0

        while cursor < right:
            if nums[cursor] == 2:
                nums[cursor], nums[right] = nums[right], nums[cursor]
                right -= 1
                cursor -= 1
            elif nums[cursor] == 0:
                nums[cursor], nums[left] = nums[left], nums[cursor]
                left += 1
            
            cursor += 1
            
        print(nums)
        return nums

assert Solution().sortColors(nums = [2,0,2,1,1,0]) == [0,0,1,1,2,2]