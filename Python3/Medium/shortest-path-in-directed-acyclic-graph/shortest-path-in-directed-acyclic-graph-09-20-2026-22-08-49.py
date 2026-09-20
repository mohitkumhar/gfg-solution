import sys
sys.setrecursionlimit(10**5)

class Solution:
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]
        for u, v, wt in edges:
            adj[u].append((v, wt))

        visited = [False] * V
        stack = []

        def dfs(node):
            visited[node] = True
            for v, wt in adj[node]:
                if not visited[v]:
                    dfs(v)
            stack.append(node)

        for i in range(V):
            if not visited[i]:
                dfs(i)

        dist = [float('inf')] * V
        dist[0] = 0

        while stack:
            node = stack.pop()
            if dist[node] != float('inf'):
                for v, wt in adj[node]:
                    if dist[node] + wt < dist[v]:
                        dist[v] = dist[node] + wt

        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist