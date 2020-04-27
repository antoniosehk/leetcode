'''
Solution based on dynamic programming
time complexity: O(m*n)
key observation:
  if dp[row][col] == 1:
    dp[row][col] = min(dp[row-1][col-1],
                       dp[row-1][col],
                       dp[row][col-1]) + 1
space complexity: O(m*n)
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        dp = [[0] * num_cols for _ in range(num_rows)]
        output = 0

        for row in range(num_rows):
            for col in range(num_cols):
                dp[row][col] = int(matrix[row][col])
                if row - 1 >=0 and col-1 >= 0 and dp[row][col] == 1:
                    dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
                output = max(output, dp[row][col])


        return output * output
