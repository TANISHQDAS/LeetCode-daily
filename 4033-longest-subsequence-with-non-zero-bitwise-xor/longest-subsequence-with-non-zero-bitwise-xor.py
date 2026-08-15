class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0
        for v in nums:
            x ^= v

        if x:
            return len(nums)

        for v in nums:
            if v:
                return len(nums) - 1

        return 0