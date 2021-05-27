'''
https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''
from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = [] # Max heap
        self.right = [] # Min heap

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 or num <= -self.left[0]:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        
        # Balance heaps
        if len(self.left) < len(self.right):
            min_right = heappop(self.right)
            heappush(self.left, -min_right)
        elif len(self.left) - len(self.right) > 1:
            max_left = -heappop(self.left)
            heappush(self.right, max_left)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        else:
            return -self.left[0]