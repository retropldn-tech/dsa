'''
    You are given a 0-indexed string s of even length n. 
    The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
    A string is called balanced if and only if:
    It is the empty string, or
    It can be written as AB, where both A and B are balanced strings, or
    It can be written as [C], where C is a balanced string.
    You may swap the brackets at any two indices any number of times.
    Return the minimum number of swaps to make s balanced.
'''
from math import ceil

class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '[':
                stack.append('[')
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
        return ceil(len(stack)/4)

assert Solution().minSwaps(s = "][][") == 1
assert Solution().minSwaps(s = "]]][[[") == 2
assert Solution().minSwaps(s = "[]") == 0