'''
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        final_qty = 0
        def count_palindrome_in_current_centers(s, left, right) -> int:
            palidrome_qty = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    palidrome_qty += 1
                left -= 1
                right += 1
            return palidrome_qty
        
        for center in range(len(s)):
            final_qty += count_palindrome_in_current_centers(s=s, left=center, right=center)
            final_qty += count_palindrome_in_current_centers(s=s, left=center, right=center+1)

        return final_qty

assert Solution().countSubstrings(s = "abc") == 3
assert Solution().countSubstrings(s = "aaa") == 6