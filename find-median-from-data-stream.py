'''
    https://leetcode.com/problems/find-median-from-data-stream/
'''

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
            [1, 3, 4]  [7, 13, 20]
            max_heap will maintain left order [-4, -3, -1]
            min_heap will maintain right order [7, 13, 20]
        """
        self.max_heap = []
        self.min_heap = []
        
        
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            # check with max_heap (left order) first
            max_num_from_left_order = -heapq.heappushpop(self.max_heap, -num)
            # then check with right order
            heapq.heappush(self.min_heap, max_num_from_left_order)
        else:
            max_num_from_right_order = heapq.heappushpop(self.min_heap, num)
            heapq.heappush(self.max_heap, -max_num_from_right_order)
    

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()