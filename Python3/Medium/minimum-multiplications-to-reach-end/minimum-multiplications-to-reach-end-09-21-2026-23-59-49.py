from collections import deque

class Solution:
    def minSteps(self, arr, start, end):
        if start == end:
            return 0

        dist = [-1] * 1000
        dist[start] = 0

        q = deque([start])

        while q:
            curr = q.popleft()

            for num in arr:
                nxt = (curr * num) % 1000

                if dist[nxt] == -1:
                    dist[nxt] = dist[curr] + 1

                    if nxt == end:
                        return dist[nxt]

                    q.append(nxt)

        return -1