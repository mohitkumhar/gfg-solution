import heapq
class Solution:
    def minComputation(self, files):
        # code here


        heapq.heapify(files)
        cost = 0

        while len(files) > 1:
            first = heapq.heappop(files)
            second = heapq.heappop(files)

            merged = first + second
            cost += merged

            heapq.heappush(files, merged)

        return cost
