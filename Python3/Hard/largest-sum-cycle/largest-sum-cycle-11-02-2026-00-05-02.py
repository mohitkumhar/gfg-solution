class Solution:
    def largestSumCycle(self, edge):

        n = len(edge)
        visited = [False] * n
        path_index = [-1] * n

        ans = -1

        def dfs(node, path):
            nonlocal ans

            visited[node] = True
            path_index[node] = len(path)
            path.append(node)

            nxt = edge[node]

            if nxt != -1:

                if not visited[nxt]:
                    dfs(nxt, path)

                elif path_index[nxt] != -1:
                    cycle_start = path_index[nxt]
                    cycle_sum = sum(path[cycle_start:])
                    ans = max(ans, cycle_sum)

            path_index[node] = -1

        for i in range(n):
            if not visited[i]:
                dfs(i, [])

        return ans