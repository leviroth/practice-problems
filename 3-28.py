def solve(preorder, inorder, p, lo, hi):
    if lo >= hi:
        return None
    root_val = preorder[p]
    node = TreeNode(root_val)
    i = lo
    while inorder[i] != root_val:
        i += 1
    node.left = solve(preorder, inorder, p + 1, lo, i)
    node.right = solve(preorder, inorder, p + (i - lo) + 1, i + 1, hi)
    return node


class Solution:
    def buildTree(self, preorder, inorder):
        return solve(preorder, inorder, 0, 0, len(preorder))
