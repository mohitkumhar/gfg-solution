class Solution:
    def findPermutation(self, s):

        n = len(s)
        def backtrack(temp):
            if len(temp) == n:
                result.append(''.join(temp[:]))
                return

            for i in range(n):
                if i in visited:
                    continue
                visited.add(i)
                temp.append(s[i])

                backtrack(temp)

                temp.pop()
                visited.remove(i)

        visited = set()
        result = []
        backtrack([])

        return list(set(result))
