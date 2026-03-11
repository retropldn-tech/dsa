'''
    The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
    You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
    Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hm = {}
        stack = []
        ans = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                n = stack.pop()
                hm[n] = nums2[i]
            stack.append(nums2[i])
            
        for i in nums1:
            if i in hm:
                ans.append(hm[i])
            else:
                ans.append(-1)
        return ans

assert Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]) == [-1,3,-1]
assert Solution().nextGreaterElement(nums1 = [1,3,5,2,4], nums2 = [6,5,4,3,2,1,7]) == [7,7,7,7,7]