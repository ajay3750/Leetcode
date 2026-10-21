class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        if list(s) == sorted(list(s)):
            return 0
            
        if n <= 2:
            return -1
            
        min_char = min(s)
        max_char = max(s)
        
        min_c = s.index(min_char)
        max_c = max(i for i, c in enumerate(s) if c == max_char)
        
        if min_c == 0 or max_c == n - 1:
            return 1
            
        if min_c == n - 1 and max_c == 0:
            return 3
            
        return 2