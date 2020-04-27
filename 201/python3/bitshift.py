'''
Solution based on bitshift
time complexity: O(1),
  as the number of bitshift is bounded by
     the number of bits that an integer has, which is fixed.
space complexity: O(1)
'''

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        numOfBitShits = 0

        while m != n:
            m = m >> 1
            n = n >> 1
            numOfBitShits += 1

        return m << numOfBitShits
