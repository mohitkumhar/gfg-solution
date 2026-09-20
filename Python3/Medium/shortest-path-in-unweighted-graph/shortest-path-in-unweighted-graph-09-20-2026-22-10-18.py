from collections import deque

class Solution:
    def shortestPath(self, V, edges, src, dest):
        if src == dest:
            return 0

        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V
        visited[src] = True

        q = deque([(src, 0)])

        while q:
            node, dist = q.popleft()

            if node == dest:
                return dist

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, dist + 1))

        return -1