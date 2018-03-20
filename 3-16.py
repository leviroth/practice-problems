from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.contents = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.contents.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        extra = deque()
        while len(self.contents) > 1:
            extra.append(self.contents.popleft())
        result = self.contents.popleft()
        self.contents = extra
        return result

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        extra = deque()
        while len(self.contents) > 1:
            extra.append(self.contents.popleft())
        result = self.contents.popleft()
        extra.append(result)
        self.contents = extra
        return result

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.contents) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
