'''
    You are given a 0-indexed integer array nums. 
    To create the compressed array, repeatedly remove every pair of adjacent equal elements from 
    nums until no such pairs remain. After compression, calculate the mean (average) of the elements in the resulting array.
    Return the mean of the compressed array as a floating-point number. If the compressed array is empty, return 0.0.
'''

class Solution:
    def calculateCompressedMean(self, quantities: List[int]) -> float:
        cur_sum = 0
        
        ...

assert Solution().calculateCompressedMean([2, 2, 3, 3, 4, 5, 5, 4]) == 3.5