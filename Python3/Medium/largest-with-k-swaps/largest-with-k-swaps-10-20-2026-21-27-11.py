
class Solution:
    def findMaximumNum(self, s, k):
        self.ans = s

        def solve(s, k):
            if k == 0:
                return

            n = len(s)

            for i in range(n - 1):
                max_digit = max(s[i + 1:])

                if max_digit <= s[i]:
                    continue

                for j in range(n - 1, i, -1):
                    if s[j] == max_digit:
                        temp = list(s)
                        temp[i], temp[j] = temp[j], temp[i]
                        new_s = "".join(temp)

                        if new_s > self.ans:
                            self.ans = new_s

                        solve(new_s, k - 1)

        solve(s, k)
        return self.ans
