from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)

        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i + k]):
                d[x] += 1

        a = -1
        for x in d:
            if d[x] == 1:
                a = max(a, x)

        return a