from collections import deque

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:

        n = len(adj)

        def bfs(start):
            dist = [-1] * n
            dist[start] = 0

            q = deque([start])
            farthest = start

            while q:
                node = q.popleft()

                for neighbor in adj[node]:
                    neighbor -= 1   # convert 1-indexed house to 0-indexed

                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[node] + 1
                        q.append(neighbor)

                        if dist[neighbor] > dist[farthest]:
                            farthest = neighbor

            return farthest, dist[farthest]

        # 1. Find one endpoint of the diameter
        farthest_node, _ = bfs(0)

        # 2. Find the diameter
        _, diameter = bfs(farthest_node)

        # 3. Minimum maximum distance = ceil(diameter / 2)
        return (diameter + 1) // 2