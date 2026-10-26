class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] <= 0:
                return 0
            
            val = grid[r][c]
            grid[r][c] = 0
            
            total = val
            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)
            
            return total

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)
                    if island_sum % k == 0:
                        count += 1
                        
        return count