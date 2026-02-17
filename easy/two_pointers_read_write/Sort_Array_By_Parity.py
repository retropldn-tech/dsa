
class Solution:
    def sortArrayByParity(self, A):
        write = 0
        read = 0
        while read < len(A):
            
            if A[read] % 2 == 0:
                A[read], A[write] = A[write], A[read]
                write += 1
            read += 1
        return A
Solution().sortArrayByParity([3, 1, 2, 4])