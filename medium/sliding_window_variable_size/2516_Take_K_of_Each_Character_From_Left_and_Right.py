'''
    You are given a string s consisting of the characters 'a', 'b', and 'c' 
    and a non-negative integer k. Each minute, you may take either the leftmost 
    character of s, or the rightmost character of s.
    Return the minimum number of minutes needed for you to take at least k of 
    each character, or return -1 if it is not possible to take k of each character.
'''

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        left = 0
        hashmap = {
            'a': 0,
            'b': 0,
            'c': 0,
        }
        res = 0
        for i in s:
            hashmap[i] += 1
        for i in hashmap:
            if hashmap[i] < k:
                return -1
        for right in range(len(s)):
            hashmap[s[right]] -= 1
            while hashmap[s[right]]  < k and left<=right:
                hashmap[s[left]] += 1
                left += 1
            res = max(res, right-left+1)
        return len(s)-res

assert Solution().takeCharacters(s = "aabaaaacaabc", k = 2) == 8