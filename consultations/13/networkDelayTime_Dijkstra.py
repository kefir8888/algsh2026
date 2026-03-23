# https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf') for _ in range(n + 1)]
        dist[k] = 0
        dist[0] = -1
        adj = [[] for _ in range(n + 1)]
        # print(adj)
        for u, v, w in times:
            adj[u].append((w, v))
        h = [(0, k)]
        while h:
            d, v = heapq.heappop(h)
            if d != dist[v]:
                continue
            # dist[A] = 3
            # (3, A), (10, A), (30, A)
            for w, u in adj[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    heapq.heappush(h, (dist[u], u))
        ans = max(dist)
        if ans == float('inf'):
            return -1
        return ans
                