'''
    Given two strings s and t of lengths m and n respectively, return 
    the minimum window substring of s such that every character in t (including duplicates) 
    is included in the window. If there is no such substring, return the empty string "".
    The testcases will be generated such that the answer is unique.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map, t_map = {}, {} 
        we_need, we_have = 0,0
        left = 0
        min_len = float('inf')
        ans = ''

        for i in t:
            if i not in t_map:
                we_need += 1
            t_map[i] = 1 + t_map.get(i, 0)

        for right in range(len(s)):
            if s[right] in t_map:
                
                s_map[s[right]] = 1 + s_map.get(s[right], 0)
                if s_map[s[right]] == t_map[s[right]]:
                    we_have += 1

            while we_have == we_need:
                if right - left + 1 < min_len:
                    min_len = right -left + 1
                    ans = s[left:right+1]
                if s[left] in t_map:
                    s_map[s[left]] -= 1
                    if s_map[s[left]] < t_map[s[left]]:
                        we_have -= 1

                left += 1
        return ans


assert Solution().minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd") == "abbbbbcdd"
assert Solution().minWindow(s = "ADOBECODEBANC", t = "ABC") == "BANC"
assert Solution().minWindow(s = "OUZODYXAZV", t = "XYZ") == "YXAZ"
assert Solution().minWindow(s = "a", t = "a") == "a"
assert Solution().minWindow(s = "a", t = "aa") == ""