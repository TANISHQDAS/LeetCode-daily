from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = sorted(Counter(word).values(), reverse=True)
        ans = 0
        for i, x in enumerate(c):
            ans += x * (i // 8 + 1)
        return ans