
class Solution:
    def largestSumCycle(self, N, edge):
        visited = [False] * N
        ans = -1

        for i in range(N):
            if visited[i]:
                continue

            curr = i
            path = {}
            step = 0

            while curr != -1 and not visited[curr]:
                visited[curr] = True
                path[curr] = step
                step += 1
                curr = edge[curr]

            # A cycle exists if curr belongs to this traversal
            if curr != -1 and curr in path:
                cycle_sum = 0
                node = curr

                while True:
                    cycle_sum += node
                    node = edge[node]

                    if node == curr:
                        break

                ans = max(ans, cycle_sum)

        return ans
