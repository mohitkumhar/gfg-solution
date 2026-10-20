class Solution:
    def check(self, n, m, edges):
        adj = [[] for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node, count):
            if count == n:
                return True

            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True

                    if dfs(nei, count + 1):
                        return True

                    visited[nei] = False

            return False

        for start in range(n):
            visited[start] = True

            if dfs(start, 1):
                return True

            visited[start] = False

        return False