class Solution:
    def rabinKarp(self, text, pattern):

        n = len(text)
        m = len(pattern)

        LPS = [0] * m
        LPS[0] = 0

        length_idx = 0

        i = 1

        while i < m:
            if pattern[i] == pattern[length_idx]:
                length_idx += 1
                LPS[i] = length_idx
                i+=1

            else:
                if length_idx > 0:
                    length_idx = LPS[length_idx - 1]
                else:
                    LPS[i] = 0
                    i += 1

        result = []

        i = 0
        j = 0

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

                if j >= m:
                    result.append(i - m)
                    j = LPS[j - 1]

            else:
                if j > 0:
                    j = LPS[j - 1]
                else:
                    i += 1

        return result
