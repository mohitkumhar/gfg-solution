class Solution:
	def mergeOverlap(self, arr):
		# Code here
    		
        arr.sort()
        result = []
    
        for interval in arr:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
    
        return result