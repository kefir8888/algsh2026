# https://leetcode.com/problems/path-with-minimum-effort/
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        X, Y = len(heights), len(heights[0])
        min_effort = [[float('inf')] * Y for _ in range(X)]
        min_effort[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            effort, x, y = heapq.heappop(h)
            if effort != min_effort[x][y]:
                continue
            if x == X - 1 and y == Y - 1:
                return effort
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < X and 0 <= ny < Y:
                    # effort is effort to reach (x, y) from (0, 0)
                    # path from (0, 0) => (x, y) => (nx, ny)
                    n_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    if n_effort < min_effort[nx][ny]:
                        min_effort[nx][ny] = n_effort
                        heapq.heappush(h, (n_effort, nx, ny))
