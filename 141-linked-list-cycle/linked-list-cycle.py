class Solution:
    def hasCycle(self, h):
        s, f = h, h
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False