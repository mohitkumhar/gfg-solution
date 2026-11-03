class Solution:
    def maximumWeight(self, n, edges, queries):

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return 0

            paths = size[pu] * size[pv]

            if size[pu] < size[pv]:
                pu, pv = pv, pu

            parent[pv] = pu
            size[pu] += size[pv]

            return paths

        edges.sort(key = lambda x: x[2])

        sorted_queries = sorted(
            (x, i) for i, x in enumerate(queries)
        )

        ans = [0] * len(queries)
        total = 0
        j = 0

        for x, idx in sorted_queries:

            while j < len(edges) and edges[j][2] <= x:
                u, v, w = edges[j]

                total += union(u, v)
                j += 1

            ans[idx] = total

        return ans
