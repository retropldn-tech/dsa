'''
    Given a string s of '(' , ')' and lowercase English characters.
    Your task is to remove the minimum number of parentheses 
    ( '(' or ')', in any positions ) so that the resulting parentheses string 
    is valid and return any valid string.
    Formally, a parentheses string is valid if and only if:
    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
'''
from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        res = ''
        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                elif not stack or (stack and s[stack[-1]] == ')'):
                    stack.append(i)
            print(stack)

        for i in range(len(s)):
            if stack and i == stack[0]:
                stack.popleft()
                continue
            res += s[i]
        
        print(res, stack)
        return res

assert Solution().minRemoveToMakeValid(s = "lee(t(c)o)de)") == "lee(t(c)o)de"
assert Solution().minRemoveToMakeValid(s = "a)b(c)d") == "ab(c)d"
# assert Solution().minRemoveToMakeValid(s = "))((") == ""