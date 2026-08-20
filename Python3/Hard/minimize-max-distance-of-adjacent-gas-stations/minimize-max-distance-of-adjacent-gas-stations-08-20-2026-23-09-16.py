import heapq

class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)

        if n <= 1:
            return 0.0

        heap = []

        for i in range(n - 1):
            gap = stations[i + 1] - stations[i]
            heapq.heappush(heap, (-gap, i, 1))

        for _ in range(k):
            currGap, index, count = heapq.heappop(heap)

            count += 1

            originalGap = stations[index + 1] - stations[index]

            newGap = originalGap / (count)

            heapq.heappush(heap, (-newGap, index, count))

        maxDist, _, _ = heap[0]

        return - maxDist
