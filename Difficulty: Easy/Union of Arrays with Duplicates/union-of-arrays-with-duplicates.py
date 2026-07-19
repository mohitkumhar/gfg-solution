class Solution:    
    def findUnion(self, a, b):
        seen = set()
        
        result = []
        
        for num in a + b:
            if num in seen:
                continue
            seen.add(num)
            result.append(num)
        
        return result