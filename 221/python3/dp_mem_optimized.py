'''
Solution based on dynamic programming
time complexity: O(n*n)
key observation:
  if dp[row][col] == 1:
    dp[row][col] = min(dp[row-1][col-1],
                       dp[row-1][col],
                       dp[row][col-1]) + 1
space complexity: O(n)
Only two 1D arrays are needed: previous and current
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        output = 0

        for row in range(num_rows):
            current = [0] * num_cols
            for col in range(num_cols):
                current[col] = int(matrix[row][col])
                if row - 1 >=0 and col-1 >= 0 and current[col] == 1:
                    current[col] = min(previous[col-1], previous[col], current[col-1]) + 1
                output = max(output, current[col])
            previous = current

        return output * output
