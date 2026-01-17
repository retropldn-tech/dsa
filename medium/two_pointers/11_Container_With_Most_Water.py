'''
    You are given an integer array height of length n. There are n vertical lines drawn 
    such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        cur_max_square = 1
        left = 0
        right = len(height)-1
        while left <= right:
            width = right - left
            length = min(height[left], height[right])
            if cur_max_square <= width*length:
                cur_max_square = width*length
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
                right -= 1
        print(cur_max_square)
        return cur_max_square
assert Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]) == 49