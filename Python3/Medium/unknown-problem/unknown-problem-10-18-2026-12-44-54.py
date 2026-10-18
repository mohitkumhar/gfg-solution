class Solution:
    def firstNegInt(self, arr, k):

        n = len(arr)

        i = 0
        j = 0

        queue = []
        result = []

        while j < n:

            if arr[j] < 0:
                queue.append(arr[j])

            if (j - i + 1) < k:
                j += 1

            elif (j - i + 1) == k:
                if queue:
                    result.append(queue[0])
                else:
                    result.append(0)

                if queue and arr[i] == queue[0]:
                    queue.pop(0)

                i += 1
                j += 1

        return result
