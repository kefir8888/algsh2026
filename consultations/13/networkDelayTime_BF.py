# https://leetcode.com/problems/network-delay-time/description/
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf') for _ in range(n + 1)]
        dist[k] = 0
        dist[0] = -1
        for _ in range(n - 1):
            updated = False
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
        ans = max(dist)
        return -1 if ans == float('inf') else ans