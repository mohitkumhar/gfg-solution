import sys
sys.setrecursionlimit(200005)

class Solution:
    def tarjans(self, V: int, adj: list[list[int]]) -> list[list[int]]:
        timer = 0
        tin = [-1] * V
        low = [-1] * V
        in_stack = [False] * V
        stack = []
        sccs = []

        def dfs(u):
            nonlocal timer
            tin[u] = low[u] = timer
            timer += 1
            stack.append(u)
            in_stack[u] = True

            for v in adj[u]:
                if tin[v] == -1:
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif in_stack[v]:
                    low[u] = min(low[u], tin[v])

            if low[u] == tin[u]:
                component = []
                while True:
                    v = stack.pop()
                    in_stack[v] = False
                    component.append(v)
                    if u == v:
                        break
                component.sort()
                sccs.append(component)

        for i in range(V):
            if tin[i] == -1:
                dfs(i)

        sccs.sort()
        return sccs