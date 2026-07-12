class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        r = 1
        for x in sorted(set(arr)):
            d[x] = r
            r += 1
        return [d[x] for x in arr]