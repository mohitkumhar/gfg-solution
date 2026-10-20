class Solution:
    def findExpr(self, s, target):

        ans = []
        n = len(s)

        def backtrack(idx, expr, value, last):
            if idx == n:
                if value == target:
                    ans.append(expr)
                return

            for j in range(idx, n):
                # Avoid operands with leading zeros
                if j > idx and s[idx] == '0':
                    break

                num = int(s[idx: j + 1])
                part = s[idx: j + 1]

                if idx == 0:
                    backtrack(j + 1, part, num, num)
                else:
                    # Addition
                    backtrack(
                        j + 1, expr + '+' + part,
                        value + num, num
                    )

                    # Subtraction
                    backtrack(
                        j + 1, expr + '-' + part,
                        value - num, -num
                    )

                    # Multiplication: correct operator precedence
                    backtrack(
                        j + 1, expr + '*' + part,
                        value - last + last * num,
                        last * num
                    )

        backtrack(0, "", 0, 0)
        return ans
