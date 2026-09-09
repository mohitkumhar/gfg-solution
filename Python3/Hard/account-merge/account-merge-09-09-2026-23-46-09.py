class Solution:
    def accMerge(self, arr: list[list[str]]) -> list[list[str]]:
        n = len(arr)

        parent = list(range(n))
        email_to_account = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                parent[b] = a

        # Merge accounts having common email
        for i in range(n):
            for email in arr[i][1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        # Store emails belonging to each group
        groups = {}

        for i in range(n):
            root = find(i)

            if root not in groups:
                groups[root] = set()

            for email in arr[i][1:]:
                groups[root].add(email)

        # Build answer
        ans = []

        for root, emails in groups.items():
            ans.append([arr[root][0]] + sorted(emails))

        return ans