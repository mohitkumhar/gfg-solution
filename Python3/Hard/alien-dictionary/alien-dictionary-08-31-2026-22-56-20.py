from collections import deque
class Solution:
    def findOrder(self, words: list[str]) -> str:
        # Collect all unique characters
        chars = set()

        for word in words:
            for ch in word:
                chars.add(ch)

        # Graph
        graph = {ch: [] for ch in chars}

        # Indegree
        indegree = {ch: 0 for ch in chars}

        # Compare adjacent words
        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            # Invalid case:
            # ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first different character
            for j in range(min(len(w1), len(w2))):

                if w1[j] != w2[j]:

                    u = w1[j]
                    v = w2[j]

                    # Avoid duplicate edge
                    if v not in graph[u]:
                        graph[u].append(v)
                        indegree[v] += 1

                    break

        # Topological sort
        q = deque()

        for ch in chars:
            if indegree[ch] == 0:
                q.append(ch)

        order = []

        while q:

            ch = q.popleft()
            order.append(ch)

            for neighbour in graph[ch]:

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    q.append(neighbour)

        # Cycle exists
        if len(order) != len(chars):
            return ""

        return "".join(order)