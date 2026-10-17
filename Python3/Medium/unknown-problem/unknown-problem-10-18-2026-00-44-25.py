class Solution:
    def search(self, pat, txt):
        counter = {}

        for char in pat:
            counter[char] = counter.get(char, 0) + 1

        i = 0
        j = 0
        k = len(pat)
        pat_set = set(pat)
        ans = 0
        n = len(txt)

        while j < n:
            if txt[j] in counter:
                counter[txt[j]] -= 1

                if counter[txt[j]] == 0:
                    del counter[txt[j]]

            elif txt[j] in pat_set:
                counter[txt[j]] = -1

            if j - i + 1 == k:
                if not counter:
                    ans += 1

                if txt[i] in pat_set:
                    counter[txt[i]] = counter.get(txt[i], 0) + 1
                    if counter[txt[i]] == 0:
                        del counter[txt[i]]

                i += 1

            j += 1

        return ans