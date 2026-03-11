'''
    You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
    We repeatedly make duplicate removals on s until we no longer can.
    Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)

assert Solution().removeDuplicates(s = "abbaca") == 'ca'