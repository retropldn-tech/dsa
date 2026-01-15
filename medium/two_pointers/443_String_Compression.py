'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.
'''

class Solution:
    def compress(self, chars: list[str]) -> int:
        sorted(chars)
        def counter_division(literal:str, counter: int):
            res = [literal]
            if counter > 9:
                for i in list(str(counter)):
                    res.append(i)
            else:
                if counter > 1:
                    res.append(str(counter))
            return res
        
        prev_char = chars[0]
        first_append_char = 0
        counter=1
        for i in range(1,len(chars)):
            if prev_char == chars[i]:
                counter += 1
                
            if prev_char != chars[i]:
                new_counter = counter_division(literal=prev_char, counter=counter)
                chars[first_append_char:i] = new_counter
                counter=1
                first_append_char = i
                prev_char = chars[i]

            if i == len(chars)-1:
                new_counter = counter_division(literal=prev_char, counter=counter)
                chars[first_append_char:i+1] = new_counter
        return len(chars)
    
Solution().compress(chars = ["a","a","a","a","a","b","b"])
# assert Solution().compress(chars = ["a","a","b","b","c","c","c"]) == 6
# assert Solution().compress(chars = ["a"]) == 1
#assert Solution().compress(chars = ["a", "a", "c", "b","b","b","b","b","b","b","b","b","b","b","b"]) == 4
