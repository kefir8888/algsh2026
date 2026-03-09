# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0"
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if (0 <= nr < R) and (0 <= nc < C) and grid[nr][nc] == "1":
                    dfs(nr, nc)
        
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
        return ans