'''
    Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        left, right = 0,0
        result = set()
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                result.add(nums1[left])
                left += 1
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            elif nums2[right] < nums1[left]:
                right += 1
        print(result)
        return list(result)

assert Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]) == [2]
assert Solution().intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [9,4]