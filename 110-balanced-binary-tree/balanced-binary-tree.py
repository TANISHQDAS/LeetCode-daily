class Solution:
    def isBalanced(self, r):
        def h(n):
            if not n:
                return 0
            l, r = h(n.left), h(n.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1
        return h(r) != -1