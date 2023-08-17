class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       actual_sum = sum(nums)
       total_sum = sum(range(0, len(nums)+1))
       return total_sum - actual_sum


