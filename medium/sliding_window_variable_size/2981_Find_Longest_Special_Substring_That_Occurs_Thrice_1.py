'''
    You are given a string s that consists of lowercase English letters.
    A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
    Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
    A substring is a contiguous non-empty sequence of characters within a string.
'''

class Solution:
    def maximumLength(self, s: str) -> int:
        res = -1
        left,right = 0,0
        hashmap = {}
        while right <= len(s)-1:

            while s[left] != s[right] and left < right:
                print('asdasds')
                if right == len(s)-1:
                    right = len(s)
                if s[left:right] not in hashmap:
                    hashmap[s[left:right]] = 1
                else:
                    hashmap[s[left:right]] += 1
                left += 1
            right += 1

        for i in hashmap:
            if hashmap[i] > 3:
                res = max(res, len(i))
        print(res, hashmap)
        return res
            

assert Solution().maximumLength(s = "aaaa") == 2
assert Solution().maximumLength(s = "abcdef") == -1
assert Solution().maximumLength(s = "abcaba") == 1
