'''
    Given string num representing a non-negative integer num, and an integer k, 
    return the smallest possible integer after removing k digits from num.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        
        stack = []

        for right in range(k+1):
            if stack and int(stack[-1]) > int(num[right]):
                stack.pop()
                stack.append(num[right])
            else:
                if not stack:
                    stack.append(num[right])
                elif stack and int(stack[-1]) < int(num[right]):
                    continue;
            print(stack)
        print(str(stack[-1])+num[k+1:] if int(stack[-1]) > 0 else num[k:])
        return str(stack[-1])+num[k+1:] if int(stack[-1]) > 0 else num[k:]



# assert Solution().removeKdigits(num = "10", k = 2) == "0"
assert Solution().removeKdigits(num = "1432219", k = 3) == "1219"
assert Solution().removeKdigits(num = "10200", k = 1) == "200"