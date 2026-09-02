from leetcode.heap.find_median_stream import MedianFinder


def test_find_median():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)  # arr[1, 2, 3]
    assert medianFinder.findMedian() == 2.0
