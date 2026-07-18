class Solution:
    def findUnion(self, a, b):
        seen = set()
        result = []

        for num in a + b:
            if num not in seen:
                seen.add(num)
                result.append(num)

        return sorted(result)
