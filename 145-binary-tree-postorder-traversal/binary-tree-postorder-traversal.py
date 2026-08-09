class Solution:
    def postorderTraversal(self, r):
        res, st = [], [(r, False)] if r else []
        while st:
            n, v = st.pop()
            if v:
                res.append(n.val)
            else:
                st.append((n, True))
                if n.right:
                    st.append((n.right, False))
                if n.left:
                    st.append((n.left, False))
        return res 