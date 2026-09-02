class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):

            a = find(a)
            b = find(b)

            if a == b:
                return 0

            if size[a] < size[b]:
                a, b = b, a

            # Number of new paths created
            new_paths = size[a] * size[b]

            parent[b] = a
            size[a] += size[b]

            return new_paths

        # Sort edges according to weight
        edges.sort(key=lambda x: x[2])

        # Store query with its original index
        queries_with_index = sorted(
            [(x, i) for i, x in enumerate(queries)]
        )

        ans = [0] * len(queries)

        edge_index = 0
        total = 0

        for x, index in queries_with_index:

            # Add all edges having weight <= x
            while edge_index < len(edges) and edges[edge_index][2] <= x:

                u, v, w = edges[edge_index]

                total += union(u, v)

                edge_index += 1

            ans[index] = total

        return ans