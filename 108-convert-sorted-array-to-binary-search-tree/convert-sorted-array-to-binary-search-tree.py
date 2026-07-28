class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)

            return root

        return build(0, len(nums) - 1)