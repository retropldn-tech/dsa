class Solution:
    def compress(self,chars):
        if len(chars) == 1:
            return 1
        counter = 1
        final_counter = 0
        prev_symbol = chars[0]
        for i in range(1,len(chars)):
            if chars[i] == prev_symbol:
                counter += 1
            else:
                
                len_counter = len(str(counter))
                if counter != 1:
                    len_counter += 1
                else:
                    len_counter = 1

                final_counter += len_counter
                counter = 1
                prev_symbol = chars[i]

        final_counter += 1

        if counter > 1:
            len_counter = len(str(counter))
            final_counter += len_counter

        return final_counter
    
assert Solution().compress(["a", "b", "c", "d", "e"]) == 5
assert Solution().compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
assert Solution().compress(["a"]) == 1
assert Solution().compress(["z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z", "z"]) == 3