class Solution:
    def findSequences(self, words, s, e):
        word_set = set(words)

        if e not in word_set:
            return []

        q = [s]
        visited = {s}
        parent = {s: []}

        while q:
            next_level = set()

            for word in q:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word not in word_set:
                            continue

                        if new_word not in visited:
                            if new_word not in next_level:
                                next_level.add(new_word)
                                parent[new_word] = []

                            parent[new_word].append(word)

                        elif new_word in next_level:
                            parent[new_word].append(word)

            if e in next_level:
                break

            visited.update(next_level)
            q = list(next_level)

        if e not in parent:
            return []

        ans = []

        def dfs(word, path):
            if word == s:
                ans.append(path[::-1])
                return

            for p in parent[word]:
                dfs(p, path + [p])

        dfs(e, [e])

        return ans