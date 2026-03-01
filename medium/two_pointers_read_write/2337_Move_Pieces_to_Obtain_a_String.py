'''
    You are given two strings start and target, both of length n. Each string consists only 
    of the characters 'L', 'R', and '_' where:
        The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if 
        there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a 
        blank space directly to its right.
        The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
        Return true if it is possible to obtain the string target by moving the pieces of the 
        string start any number of times. Otherwise, return false.
'''
# Solution:
# Make it in two phase:
#  - By the first make traverse from left side to the right:
#      if read see _ - do not increase write, if see L - swap and increase write
#      if see R - stop algo
# - The same moves for R but from another side
#  - in the and check if both strings equal

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len(target):
            return False
        counter_start = 0
        counter_target = 0
        for i in start:
            if i  != '_':
                counter_start += 1

        for i in target:
            if i  != '_':
                counter_target += 1
        if counter_target != counter_start:
            return False
        
        write = 0 
        for read in range(len(start)):
            if start[read] == 'L':
                if target[write] != 'L':
                    return False
                write += 1
            if start[read] == 'R':
                break;
        
        
        write = len(start)-1
        for read in range(len(start)-1, -1,-1):
            if start[read] == 'R':
                if target[write] != 'R':
                    return False
                write -= 1
            if start[read] == 'L':
                break;
        return True

assert Solution().canChange(start = "_L__R__R_", target = "L______RR") == True
assert Solution().canChange(start = "_R", target = "R_") == False