# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        ans = 0
        for start_r in range(R):
            for start_c in range(C):
                if grid[start_r][start_c] == "1":
                    ans += 1
                    stack = [(start_r, start_c)]
                    while stack:
                        r, c = stack.pop()
                        grid[r][c] = "0"
                        for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                            if (0 <= nr < R) and (0 <= nc < C) and grid[nr][nc] == "1":
                                stack.append((nr, nc))

        return ans