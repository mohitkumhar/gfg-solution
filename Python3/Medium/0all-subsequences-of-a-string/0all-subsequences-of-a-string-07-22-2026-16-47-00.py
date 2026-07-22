class Solution:
	def powerSet(self, s):
		# Code here

        def solve(i: int, curr_str: str) -> None:
            if i == n:
                result.append(curr_str)
                return None

            # take
            solve(i + 1, curr_str + s[i])

            # skip
            solve(i + 1, curr_str)

        n = len(s)
        result = []

        solve(0, "")
        result.sort()

        return result
