'''
    Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_palindrome_indexes(s, left, right):
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1
        
        max_len = 0
        longest_palindrome = ''
        for center in range(len(s)):
            left,right = get_palindrome_indexes(s, center, center)

            if right-left+1 > max_len:
                max_len = right-left+1
                longest_palindrome = s[left:right+1]
            
            left,right = get_palindrome_indexes(s, center, center+1)

            if right-left+1 > max_len:
                max_len = right-left+1
                longest_palindrome = s[left:right+1]

        return longest_palindrome
    
assert Solution().longestPalindrome(s = "babad") == 'bab'