
class Solution:
    def generateIp(self, s):
        ans = []
        n = len(s)

        def backtrack(idx, parts):
            if len(parts) == 4:
                if idx == n:
                    ans.append(".".join(parts))
                return

            for length in range(1, 4):
                if idx + length > n:
                    break

                segment = s[idx: idx + length]

                # Leading zeros are not allowed
                if len(segment) > 1 and segment[0] == '0':
                    continue

                # Segment must be between 0 and 255
                if int(segment) > 255:
                    continue

                backtrack(idx + length, parts + [segment])

        backtrack(0, [])
        return ans
