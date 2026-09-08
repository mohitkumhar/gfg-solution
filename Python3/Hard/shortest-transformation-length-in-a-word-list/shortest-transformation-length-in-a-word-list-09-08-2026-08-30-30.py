from collections import deque

class Solution:
    def wordLadder(self, words, s, e):
        word_set = set(words)

        if e not in word_set:
            return 0

        queue = deque([(s, 1)])


        if s in word_set:
            word_set.remove(s)

        while queue:
            word, length = queue.popleft()


            if word == e:
                return length


            for i in range(len(word)):
                original_char = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == original_char:
                        continue

                    next_word = word[: i] + ch + word[i + 1:]

                    if next_word in word_set:
                        word_set.remove(next_word)  # Mark as visited
                        queue.append((next_word, length + 1))

        return 0
