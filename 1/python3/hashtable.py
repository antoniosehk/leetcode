'''
Solution based on hashtable
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        memo = {}

        for i, num in enumerate(nums):

            # num + k = target
            # k = target - num
            k = target - num

            # found k in the hashtable
            if k in memo:
                return [memo[k], i]

            memo[num] = i
