# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def nums(node, prefix=0):
    if node is None:
        return
    prefix = prefix * 10 + node.val
    if node.left is node.right is None:
        yield prefix
    else:
        yield from nums(node.left, prefix)
        yield from nums(node.right, prefix)


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return sum(nums(root))
