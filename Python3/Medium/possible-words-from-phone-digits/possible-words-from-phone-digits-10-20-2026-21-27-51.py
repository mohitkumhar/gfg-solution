
class Solution:
    def possibleWords(self, arr):
        keypad = [
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]

        ans = []
        path = []

        def backtrack(idx):
            if idx == len(arr):
                ans.append("".join(path))
                return

            digit = arr[idx]

            if digit == 0 or digit == 1:
                backtrack(idx + 1)
                return

            for char in keypad[digit]:
                path.append(char)
                backtrack(idx + 1)
                path.pop()

        backtrack(0)
        return ans
