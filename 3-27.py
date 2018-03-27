import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left, self.right = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.left) == 0 or num < -self.left[0]:
            heapq.heappush(self.left, -num)
            if len(self.left) > len(self.right) + 1:
                heapq.heappush(self.right, -heapq.heappop(self.left))
        else:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left):
                heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2
