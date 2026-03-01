'''
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
    '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        up = len(s)-1
        down = len(t) - 1

        def next_valid_index(s, i):
            skip = 0
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                elif skip > 0 and s[i] !='#':
                    skip -= 1
                elif skip == 0 and s[i] != '#':
                    return i
                i -= 1
            return -1


        while up >=0 or down >=0:
            up = next_valid_index(s, up)
            down = next_valid_index(t, down)
            print(up, down)

            if up < 0 and down < 0:
                return True
            if up < 0 or down < 0:
                return False
            if s[up] != t[down]:
                return False

            up -= 1
            down -= 1
            
            
assert Solution().backspaceCompare(s = "a##c", t = "#a#c") == True
# assert Solution().backspaceCompare(s = "y#fo##f", t = "y#f#o##f") == True
assert Solution().backspaceCompare(s = "bxj##", t = "bxj###") == False
# assert Solution().backspaceCompare(s = "bxj##tw", t = "bxo#j##tw") == True
# assert Solution().backspaceCompare(s = "xywrrmp", t = "xywrrm#p") == False
# assert Solution().backspaceCompare(s = "ab#c", t = "ad#c") == True
# assert Solution().backspaceCompare(s = "ab##", t = "c#d#") == True
# assert Solution().backspaceCompare(s = "a#c", t = "b") == False