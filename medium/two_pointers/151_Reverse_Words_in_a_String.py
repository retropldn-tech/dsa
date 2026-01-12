'''
Description:
Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space. Return a string of the words in reverse order 
concatenated by a single space. Note that s may contain leading or trailing spaces or 
multiple spaces between two words. The returned string should only have a single space separating the words. 
Do not include any extra spaces.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = self.sanitise_string(s=s)
        left  = 0
        right = len(s_list) -1
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ' '.join(s_list)
    
    def sanitise_string(self, s: str) -> list[str]:
        return s.strip().split()

assert Solution().reverseWords(s = "the sky is blue") == "blue is sky the"
assert Solution().reverseWords(s = "  hello world  ") == "world hello"
assert Solution().reverseWords(s = "a good   example"
) == "example good a"