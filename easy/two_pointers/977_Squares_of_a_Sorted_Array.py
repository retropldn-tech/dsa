'''
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        left, right = 0, len(nums)-1
        end_index = len(nums)-1
        while left < right:
            if nums[left]*nums[left] >= nums[right]*nums[right]:
                ans[end_index] = nums[left]*nums[left]
                left += 1
            else:
                ans[end_index] = nums[right]*nums[right]
                right -= 1

            end_index-=1
        return ans

assert Solution().sortedSquares(nums = [-4,-1,0,3,10]) == [0,1,9,16,100]
