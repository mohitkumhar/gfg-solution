class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:

        reserved = set(arr)
        next_suffix = {}
        result = []

        for name in arr:
            if name not in result:
                result.append(name)
            else:
                suffix = next_suffix.get(name, 1)

                while name + str(suffix) in reserved:
                    suffix += 1

                new_name = name + str(suffix)

                result.append(new_name)
                reserved.add(new_name)
                next_suffix[name] = suffix + 1

        return result
