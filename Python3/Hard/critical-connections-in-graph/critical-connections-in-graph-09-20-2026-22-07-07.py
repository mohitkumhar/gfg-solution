import sys
sys.setrecursionlimit(10**5)

class Solution:
    def criticalConnections(self, v, adj):
        timer = 0
        visited = [False] * v
        tin = [-1] * v
        low = [-1] * v
        bridges = []

        def dfs(node, parent):
            nonlocal timer
            visited[node] = True
            tin[node] = low[node] = timer
            timer += 1

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if not visited[neighbor]:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])

                    if low[neighbor] > tin[node]:
                        bridges.append([min(node, neighbor), max(node, neighbor)])
                else:
                    low[node] = min(low[node], tin[neighbor])

        for i in range(v):
            if not visited[i]:
                dfs(i, -1)

        bridges.sort()
        return bridges