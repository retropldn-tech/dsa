'''
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        def is_palindrome(l: int, r: int):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        while left < right:
            if s[right] != s[left]:
                return is_palindrome(l=left+1, r=right) or is_palindrome(l=left, r=right-1)
            else:
                right -= 1
                left += 1
        return True

assert Solution().validPalindrome(s = "aca")
assert Solution().validPalindrome(s = "abbadc") == False
assert Solution().validPalindrome(s = "abbda")
