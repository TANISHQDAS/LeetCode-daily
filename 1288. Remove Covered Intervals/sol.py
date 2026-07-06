class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        max_right = -1

        for left, right in intervals:
            if right > max_right:
                ans += 1
                max_right = right

        return ans