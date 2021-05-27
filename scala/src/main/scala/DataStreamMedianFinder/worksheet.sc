import DataStreamMedianFinder._

val medianFinder = new MedianFinder()

//["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
//[[],[1],[2],[],[3],[]]

//medianFinder.findMedian()

medianFinder.addNum(1)
medianFinder.addNum(2)

val stream = medianFinder.getStream
val mid = stream.length / 2

mid
(stream(mid) + stream(mid - 1)) / 2.0
if (stream.length % 2 == 1) stream(mid)
else (stream(mid) + stream(mid - 1)) / 2

medianFinder.findMedian()