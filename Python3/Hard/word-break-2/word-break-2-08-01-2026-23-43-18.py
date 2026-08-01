class Solution:
    def wordBreak(self, dict, s):
        dict = set(dict)

        def backtrack(i, curr_comb):
            nonlocal result

            if i >= len(s):
                result.append(" ".join(curr_comb))
                return

            for j in range(i, len(s)):
                if s[i: j + 1] in dict:
                    curr_comb.append(s[i: j + 1])
                    backtrack(j + 1, curr_comb)
                    curr_comb.pop()


        result = []

        backtrack(0, [])

        return result
