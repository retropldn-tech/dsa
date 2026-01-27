'''
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left = 0
        max_count_character = 0
        result = 0
        for right in range(len(s)):

            if s[right] in counter:
                counter[s[right]] += 1
            else:
                counter[s[right]] = 1
            
            max_count_character = max(max_count_character, counter[s[right]])

            while k < right-left+1-max_count_character:
                counter[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result
    
assert Solution().characterReplacement(s = "AABABBA", k = 1) == 4
assert Solution().characterReplacement(s = "AABABBA", k = 1) == 4
assert Solution().characterReplacement(s = "XYYX", k = 2) == 4
assert Solution().characterReplacement(s = "AAABABB", k = 1) == 5