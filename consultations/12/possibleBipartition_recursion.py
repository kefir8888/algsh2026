# https://leetcode.com/problems/possible-bipartition/
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in dislikes:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)
        # 0 -- red, 1 -- blue, -1 -- not yet decided
        group = [-1 for _ in range(n)]

        def dfs(v):
            # dfs from vertex v
            # Returns False if cannot bipartite
            for nei in adj[v]:
                if group[nei] == -1:
                    group[nei] = 1 - group[v] # 1 -> 0, 0 -> 1
                    if dfs(nei) == False:
                        return False
                else:
                    if group[nei] == group[v]:
                        return False
            return True
        
        for start in range(n):
            if group[start] != -1:
                continue
            group[start] = 1
            if dfs(start) == False:
                return False
        return True