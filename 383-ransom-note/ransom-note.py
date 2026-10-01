class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}

        for x in magazine:
            a[x] = a.get(x, 0) + 1

        for x in ransomNote:
            if x not in a or a[x] == 0:
                return False
            a[x] -= 1

        return True