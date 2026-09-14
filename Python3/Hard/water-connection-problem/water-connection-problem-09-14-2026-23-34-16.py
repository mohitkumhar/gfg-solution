class Solution:
    def solve(self, n, p, a, b, d):
        # next_house[x] = house connected by outgoing pipe from x
        next_house = [0] * (n + 1)

        # diameter[x] = diameter of pipe going out from x
        diameter = [0] * (n + 1)

        # incoming[x] = whether x has an incoming pipe
        incoming = [False] * (n + 1)

        # Build the graph
        for i in range(p):
            u = a[i]
            v = b[i]
            dia = d[i]

            next_house[u] = v
            diameter[u] = dia
            incoming[v] = True

        ans = []

        # A tank has outgoing pipe but no incoming pipe
        for house in range(1, n + 1):

            if next_house[house] != 0 and not incoming[house]:

                tank = house
                curr = house
                min_dia = float('inf')

                # Follow the chain until tap
                while next_house[curr] != 0:
                    min_dia = min(min_dia, diameter[curr])
                    curr = next_house[curr]

                tap = curr

                ans.append([tank, tap, min_dia])

        return ans