class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        stack = []
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(['(',i])
            else:
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append([')',i])


        if not stack:
            return len(s)

        indices = [-1] + [el[1] for el in stack] + [len(s)]

        for i in range(1, len(indices)):
            max_len = max(max_len, indices[i] - indices[i-1] - 1)

        return max_len