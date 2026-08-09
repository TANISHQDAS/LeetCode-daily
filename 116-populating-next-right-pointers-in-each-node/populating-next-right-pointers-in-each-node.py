class Solution:
    def connect(self, r):
        if not r:
            return r
        q = [r]
        while q:
            nxt = []
            for i, n in enumerate(q):
                if i < len(q) - 1:
                    n.next = q[i + 1]
                if n.left:
                    nxt.append(n.left)
                if n.right:
                    nxt.append(n.right)
            q = nxt
        return r