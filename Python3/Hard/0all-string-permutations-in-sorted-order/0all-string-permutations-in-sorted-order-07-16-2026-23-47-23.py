class Solution:
    def permutation(self, s):
        visited = set()

        def backtrack(temp):
            if len(temp) == n:
                result.append(''.join(temp[:]))
                return

            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    temp.append(s[i])

                    backtrack(temp)

                    visited.remove(i)
                    temp.pop()

        n = len(s)
        result = []
        backtrack([])

        return sorted(result)
