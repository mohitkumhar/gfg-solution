class Solution:
    def isCircle(self, arr):
        indegree = [0] * 26
        outdegree = [0] * 26
        graph = [[] for _ in range(26)]

        for s in arr:
            u = ord(s[0]) - ord('a')
            v = ord(s[-1]) - ord('a')

            outdegree[u] += 1
            indegree[v] += 1

            graph[u].append(v)
            graph[v].append(u)   # for connectivity check

        # Condition 1: indegree == outdegree
        for i in range(26):
            if indegree[i] != outdegree[i]:
                return 0

        # Find a vertex that actually occurs
        start = -1
        for i in range(26):
            if indegree[i] + outdegree[i] > 0:
                start = i
                break

        if start == -1:
            return 0

        # Condition 2: connectivity
        visited = [False] * 26
        stack = [start]
        visited[start] = True

        while stack:
            u = stack.pop()

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        # Every vertex that has an edge must be reachable
        for i in range(26):
            if indegree[i] + outdegree[i] > 0:
                if not visited[i]:
                    return 0

        return 1