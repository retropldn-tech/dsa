'''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        compare_map = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        for i in range(len(s)):
            if stack and s[i] in compare_map and stack[-1] == compare_map[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0


assert Solution().isValid(s = "()") == True
assert Solution().isValid(s = "()[]{}") == True
assert Solution().isValid(s = "(]") == False
assert Solution().isValid(s = "([])") == True
assert Solution().isValid(s = "([)]") == False