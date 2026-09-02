import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:

        max_val = None if len(self.max_heap) == 0 else self.max_heap[0]
        min_val = None if len(self.min_heap) == 0 else self.min_heap[0]

        if len(self.min_heap) == len(self.max_heap):
            if max_val is None or num < max_val:
                heapq.heappush_max(self.max_heap, num)
                return
            heapq.heappush(self.min_heap, num)
            return

        if len(self.max_heap) < len(self.min_heap):
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, max(min_val, num))
            heapq.heappush_max(self.max_heap, min(min_val, num))
            return

        max_val = heapq.heappop_max(self.max_heap)
        heapq.heappush(self.min_heap, max(max_val, num))
        heapq.heappush_max(self.max_heap, min(max_val, num))
        return

    def findMedian(self) -> float | None:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            return None

        max_val = None if len(self.max_heap) == 0 else self.max_heap[0]
        min_val = None if len(self.min_heap) == 0 else self.min_heap[0]

        if min_val is None:
            return max_val

        if max_val is None:
            return min_val

        if len(self.min_heap) == len(self.max_heap):
            return min_val + (max_val - min_val) / 2

        if len(self.min_heap) < len(self.max_heap):
            return max_val

        return min_val


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
