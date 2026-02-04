'''
    Write an algorithm to determine if a number n is happy.
    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), 
    or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        def make_devision(n) -> int:
            new_n = 0
            while n > 0:
                new_n += (n%10) ** 2
                n = n//10
            return new_n
        
        slow = make_devision(n)
        fast = make_devision(make_devision(n))

        while fast != 1 and slow!=fast:
            slow = make_devision(slow)
            fast = make_devision(make_devision(fast))
        
        return fast==1

assert Solution().isHappy(n = 19) == True
assert Solution().isHappy(n = 2) == False