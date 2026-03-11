class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [-1] * len(nums)

        for i in range((len(nums))*2):
            while stack and nums[stack[-1]] < nums[i%len(nums)]:
                n = stack.pop()
                ans[n] = nums[i%len(nums)]
            if i < len(nums):
                stack.append(i)

        return ans

assert Solution().nextGreaterElements(nums=[100,1,11,1,120,111,123,1,-1,-100]) == [120,11,120,120,123,123,-1,100,100,100]
# assert Solution().nextGreaterElements(nums=[1,2,3,2,1]) == [2,3,-1,3,2]
# assert Solution().nextGreaterElements(nums = [1,2,1]) == [2,-1,2]
# assert Solution().nextGreaterElements(nums = [1,2,3,4,3]) == [2,3,4,-1,4]
# assert Solution().nextGreaterElements(nums=[5,4,3,2,1]) == [-1,5,5,5,5]