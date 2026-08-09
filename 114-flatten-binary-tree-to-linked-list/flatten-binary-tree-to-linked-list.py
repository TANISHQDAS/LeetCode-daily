class Solution:
    def flatten(self, r):
        if not r:
            return
        if r.left:
            self.flatten(r.left)
            t = r.left
            while t.right:
                t = t.right
            t.right = r.right
            r.right = r.left
            r.left = None
        self.flatten(r.right)