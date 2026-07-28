class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        i = 0

        def build(l, r):
            nonlocal i
            if l > r:
                return None

            root = TreeNode(preorder[i])
            i += 1
            mid = pos[root.val]

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, len(inorder) - 1)