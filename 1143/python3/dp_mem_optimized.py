'''
Solution based on dynamic programming, with memory optimized
time complexity: O(m*n)
space complexity: O(min(m,n))
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) < len(text2):
            temp = text1
            text1 = text2
            text2 = temp

        num_cols = len(text1)
        num_rows = len(text2)

        previous = [0] * (num_rows + 1)

        for col in range(1, num_cols+1):
            current = [0] * (num_rows + 1)
            for row in range(1, num_rows+1):
                if text1[col-1] == text2[row-1]:
                    current[row] = previous[row-1] + 1
                else:
                    current[row] = max(current[row-1], previous[row])
            previous = current

        return current[num_rows]
