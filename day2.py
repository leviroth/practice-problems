from functools import partial


def safe_get(node, attr, default):
    if node is None:
        return default
    return getattr(node, attr)


safe_val = partial(safe_get, attr='val', default=0)
safe_next = partial(safe_get, attr='next', default=None)


class Solution:
    def _add_two_numbers(self, l1, l2, carry=0):
        if l1 is None and l2 is None:
            return None if carry == 0 else ListNode(carry)
        else:
            new_n = safe_val(l1) + safe_val(l2) + carry
            digit = new_n % 10
            node = ListNode(digit)
            node.next = self._add_two_numbers(safe_next(l1), safe_next(l2),
                                              carry=new_n // 10)
            return node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self._add_two_numbers(l1, l2)
