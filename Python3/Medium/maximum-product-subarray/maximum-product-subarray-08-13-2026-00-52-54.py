class Solution:
	def maxProduct(self, arr):
	    n = len(arr)

        leftProduct = 1
        rightProduct = 1

        maxProduct = arr[0]

        for i in range(n):
            leftProduct *= arr[i]
            rightProduct *= arr[n - i - 1]

            maxProduct = max(maxProduct, leftProduct, rightProduct)

            leftProduct = leftProduct if leftProduct != 0 else 1
            rightProduct = rightProduct if rightProduct != 0 else 1

        return maxProduct
