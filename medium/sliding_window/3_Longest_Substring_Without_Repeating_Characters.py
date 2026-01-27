'''
Docstring для dsa.medium.sliding_window.3_Longest Substring_Without_Repeating_Characters
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = 0
        window_state = set()
        result = 0 # max len of non repeated substring
        for end in range(len(s)):
            if s[end] not in window_state:
                window_state.add(s[end])
                result = max(end-begin+1, result)
            else:
                while s[begin] != s[end]:
                    window_state.remove(s[begin])
                    begin += 1
                window_state.remove(s[begin])
                begin += 1
                window_state.add(s[end])
                    
        return result
assert Solution().lengthOfLongestSubstring(s = "abcabcbb") == 3
assert Solution().lengthOfLongestSubstring(s = "bbbbb") == 1
assert Solution().lengthOfLongestSubstring(s="pwwkew") == 3