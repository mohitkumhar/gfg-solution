class Solution:
    def median(self, mat):
    	m = len(mat)
    	n = len(mat[0])

    	left = min(row[0] for row in mat)
    	right = max(row[n - 1] for row in mat)

    	required = (m * n) // 2

    	while left <= right:
    	    mid = left + (right - left) // 2
    	    count = 0
    	    for row in mat:
    	        count += bisect_right(row, mid)

    	    if count <= required:
    	        left = mid + 1

    	    else:
    	        right = mid - 1

        return left
