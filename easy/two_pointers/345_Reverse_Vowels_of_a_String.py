''' Description: 
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        
        s_list = list(s)
        right = len(s_list) -1 
        while left < right:
            if s_list[left] in vovels and s_list[right] not in vovels:
                right -= 1
            if s_list[left] not in vovels and s_list[right] in vovels:
                left += 1
            if s_list[left] not in vovels and s_list[right] not in vovels:
                right -= 1
                left += 1
            if s_list[left] in vovels and s_list[right] in vovels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                right -= 1
                left += 1

        return ''.join(s_list)

assert Solution().reverseVowels(s='IceCreAm') == 'AceCreIm'
assert Solution().reverseVowels(s='leetcode') == 'leotcede'
