class Solution:
	def getLPSLength(self, s):

        n = len(s)
        LPS = [0] * n
        LPS[0] = 0

        length_idx = 0

        i = 1

        while i < n:
            if s[i] == s[length_idx]:
                length_idx += 1
                LPS[i] = length_idx

                i+=1

            else:
                if length_idx > 0:
                    length_idx = LPS[length_idx - 1]
                else:
                    i += 1
        return LPS[n - 1]
