class Solution:
    def search(self, pat, txt):

        n = len(txt)
        m = len(pat)

        LPS = [0] * m
        LPS[0] = 0
        length_idx = 0

        i = 1

        while i < m:
            if pat[i] == pat[length_idx]:
                length_idx += 1
                LPS[i] = length_idx
                i += 1
            else:
                if length_idx == 0:
                    LPS[length_idx] = 0
                    i += 1
                else:
                    length_idx = LPS[length_idx - 1]

        result = []

        i = 0
        j = 0

        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    result.append(i - m)
                    j = LPS[j - 1]

            else:
                if j != 0:
                    j = LPS[j - 1]
                else:
                    i += 1

        return result
