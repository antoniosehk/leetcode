'''
Solution based on Brian Kernighan's Algorithm
time complexity: O(1),
  as the number of bitshift is bounded by
     the number of bits that an integer has, which is fixed.
space complexity: O(1)
'''

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        if m > n:
            m, n = n, m

        while n > m:
            n &= n - 1

        return m & n
