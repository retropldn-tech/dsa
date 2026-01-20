'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, 
nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r, ind = m-1,n-1, m+n-1
        while r >= 0:
            if l >=0 and nums1[l] > nums2[r]:
                nums1[ind] = nums1[l]
                l -= 1
                ind -= 1
            else:
                nums1[ind] = nums2[r]
                ind -= 1
                r -= 1

        return nums1

#Solution().merge(nums1 = [4,0,0,0,0,0], m = 1, nums2 = [1,2,3,5,6], n = 5) == [1,2,2,3,5,6]            
Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
# Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]
# Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1) == [1]