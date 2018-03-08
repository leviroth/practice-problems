# Requires python2 because leetcode doesn't have 3 for this problem


def _dfs(cur, prev, parents):
    if cur is None:
        return
    parents[cur] = prev
    _dfs(cur.left, cur, parents)
    _dfs(cur.right, cur, parents)


def find_parent_chain(parents, node):
    chain = []
    cur = node
    while cur is not None:
        chain.append(cur)
        cur = parents[cur]
    chain.reverse()
    return chain


def find_parents(root, n1, n2):
    parents = {}
    _dfs(root, None, parents)
    n1_chain = find_parent_chain(parents, n1)
    n2_chain = find_parent_chain(parents, n2)
    return n1_chain, n2_chain


def lca(chain1, chain2):
    prev = None
    from itertools import izip_longest
    for n1, n2 in izip_longest(chain1, chain2, fillvalue=None):
        if n1 is not n2:
            return prev
        prev = n1


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        chain1, chain2 = find_parents(root, p, q)
        return lca(chain1, chain2)
