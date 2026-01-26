'''
    You are given an integer array height of length n. There are n vertical lines drawn 
    such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        cur_max = 0
        l = 0
        r = len(height)-1
        while l < r:
            cur_max = max(cur_max, min(height[l],height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r-=1
            else:
                r-=1
                l+=1
        return cur_max
assert Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]) == 49