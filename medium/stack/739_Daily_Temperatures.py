'''
    Given an array of integers temperatures represents the daily temperatures, 
    return an array answer such that answer[i] is the number of days you have to wait 
    after the ith day to get a warmer temperature. If there is no future day for
    which this is possible, keep answer[i] == 0 instead.
'''

class Solution:
    def dailyTemperatures(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ind = stack.pop()
                ans[ind] = (i-ind)

            stack.append(i)
        return ans


assert Solution().dailyTemperatures(nums = [73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]