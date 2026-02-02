class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter_s1 = {}

        for i in s1:
            if i in counter_s1:
                counter_s1[i] += 1
            else:
                counter_s1[i] = 1

        left = 0
        result =0
        for right in range(len(s2)):
            if s2[right] not in counter_s1:
                while left<=right:
                    left += 1
            print(right, left)
            result = max(result, right-left+1)
        print(result)
        return result == len(s1)

assert Solution().checkInclusion(s1="adc", s2="dcda") == True
# assert Solution().checkInclusion(s1 = "ab", s2 = "ab") == True
# assert Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo") == True
# assert Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo") == False
# assert Solution().checkInclusion(s1 = "abc", s2 = "lecabee") == True
# assert Solution().checkInclusion(s1 = "abc", s2 = "lecaabee") == False