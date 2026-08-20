import heapq

class Solution:
    def minMaxDist(self, stations, k):

        n = len(stations)

        if n <= 1:
            return 0.00

        pq = []

        for i in range(n - 1):
            gas = stations[i + 1] - stations[i]
            heapq.heappush(pq, (-gas, i, 0))

        for _ in range(k):
            currGap, index, count = heapq.heappop(pq)

            count += 1

            originalGap = stations[index + 1] - stations[index]

            newGap = originalGap / (count + 1)

            heapq.heappush(pq, (-newGap, index, count))

        maxGap, _, _ = pq[0]

        return - maxGap
