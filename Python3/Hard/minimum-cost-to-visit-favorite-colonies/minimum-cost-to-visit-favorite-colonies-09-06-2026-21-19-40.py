import sys

# Set recursion depth limit for tree size up to 10^5
sys.setrecursionlimit(200000)

class Solution:
    def minCostToVisit(self, roads, favorites):
        # Determine total number of colonies n
        n = len(roads) + 1

        # Build adjacency list: node -> list of (neighbor, weight)
        adj = [[] for _ in range(n + 1)]
        for u, v in roads:
            weight = abs(u - v)
            adj[u].append((v, weight))
            adj[v].append((u, weight))

        # Fast lookup for favorite colonies
        is_favorite = [False] * (n + 1)
        for fav in favorites:
            is_favorite[fav] = True

        total_cost = 0

        # DFS returns True if the subtree rooted at 'u' contains at least one favorite node
        def dfs(u, parent):
            nonlocal total_cost
            has_favorite = is_favorite[u]

            for v, weight in adj[u]:
                if v != parent:
                    if dfs(v, u):
                        total_cost += weight
                        has_favorite = True

            return has_favorite

        # Root the DFS at the first favorite node
        root = favorites[0]
        dfs(root, -1)

        return total_cost