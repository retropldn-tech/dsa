'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0

        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        if len(s) == 1 and len(t) == 1 and s !=t:
            return False
        if len(t) == 0:
            return False
        
        while left <= len(s)-1 and right <= len(t)-1:

            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1
        return left == len(s)
    
assert Solution().isSubsequence(s = "abc", t = "ahbgdc") == True
assert Solution().isSubsequence(s = "axc", t = "ahbgdc") == False