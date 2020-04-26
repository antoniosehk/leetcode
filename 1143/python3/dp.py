'''
Solution based on dynamic programming
time complexity: O(m*n)
space complexity: O(m*n)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = {}
        dp[(0,0)] = 0

        num_rows = len(text1)
        num_cols = len(text2)

        for row in range(1, num_rows+1):
            dp[(row, 0)] = 0

        for col in range(1, num_cols+1):
            dp[(0, col)] = 0


        for row in range(1, num_rows+1):
            for col in range(1, num_cols+1):

                if text1[row-1] == text2[col-1]:
                    dp[(row, col)] = dp[(row-1,col-1)] + 1
                else:
                    dp[(row, col)] = max(dp[(row-1,col)], dp[(row,col-1)])


        return dp[(num_rows, num_cols)]
