'''
    There are n balls on a table, each ball has a color black or white.
    You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
    In each step, you can choose two adjacent balls and swap them.
    Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
'''

class Solution:
    def minimumSteps(self, s: str) -> int:
        right = len(s)-1
        zero_count, res_count = 0, 0
        while s[right] == '1':
            right -= 1
        
        while right >= 0:
            if s[right] == '0':
                zero_count += 1
            else:
                res_count += zero_count
            right -= 1

        return res_count

        

assert Solution().minimumSteps(s = "101") == 1 

assert Solution().minimumSteps(s = "100") == 2
assert Solution().minimumSteps("11000111") == 6
assert Solution().minimumSteps("01010001") == 7