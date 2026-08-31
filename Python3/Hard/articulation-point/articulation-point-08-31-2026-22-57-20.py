class Solution:
    def articulationPoints(self, V: int, edges: list[list[int]]) -> list[int]:

        # Build adjacency list
        graph = [[] for _ in range(V)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V

        articulation = [False] * V

        timer = 0

        def dfs(u):

            nonlocal timer

            disc[u] = low[u] = timer
            timer += 1

            children = 0

            for v in graph[u]:

                # v is not visited
                if disc[v] == -1:

                    parent[v] = u
                    children += 1

                    dfs(v)

                    # Update low value
                    low[u] = min(low[u], low[v])

                    # u is articulation point
                    if parent[u] == -1:
                        # Root condition
                        if children > 1:
                            articulation[u] = True

                    else:
                        # Non-root condition
                        if low[v] >= disc[u]:
                            articulation[u] = True

                # Back edge
                elif v != parent[u]:

                    low[u] = min(low[u], disc[v])

        # Graph may be disconnected
        for u in range(V):
            if disc[u] == -1:
                dfs(u)

        ans = []

        for u in range(V):
            if articulation[u]:
                ans.append(u)

        if not ans:
            return [-1]

        return ans