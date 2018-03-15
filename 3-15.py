class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        stack = []
        acc = []
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
                continue
            if not stack:
                break
            cur = stack.pop()
            acc.append(cur.val)
            cur = cur.right

        return acc
