class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        a = sorted(nums)
        n = len(nums)

        for i in range(n):
            if a[i] != i:
                return i

        return n