
'''
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
    starting with word1. If a string is longer than the other, append the additional 
    letters onto the end of the merged string.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l,r = 0,0
        while l<len(word1) and r < len(word2):
            res += word1[l] + word2[r]
            l += 1
            r += 1
        return res + word1[l:] + word2[r:]
    
assert Solution().mergeAlternately(word1 = "abc", word2 = "pqr") == 'apbqcr'
assert Solution().mergeAlternately(word1 = "ab", word2 = "pqrs") == 'apbqrs'
assert Solution().mergeAlternately(word1 = "abcd", word2 = "pq") == 'apbqcd'