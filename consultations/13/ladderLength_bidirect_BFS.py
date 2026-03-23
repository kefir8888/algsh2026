# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        dist_begin = {beginWord: 1}
        dist_end = {endWord: 1}
        q_begin = deque([beginWord])
        q_end = deque([endWord])
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return 0

        def biderectBFS(queue, dist, other_dist):
            print(dist)
            dist_v = dist[queue[0]]
            while queue and dist[queue[0]] == dist_v:
                v = queue.popleft()
                for idx in range(len(v)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        u = v[:idx] + c + v[idx + 1:]
                        if u in wordSet and u not in dist:
                            if u in other_dist:
                                return dist[v] + other_dist[u]
                            dist[u] = dist_v + 1
                            queue.append(u)
            return float('inf')
        
        while q_begin and q_end:
            if len(q_begin) < len(q_end):
                # BFS from wordBegin
                ans = biderectBFS(q_begin, dist_begin, dist_end)
            else:
                # BFS from wordEnd
                ans = biderectBFS(q_end, dist_end, dist_begin)
            if ans != float('inf'):
                return ans
        return 0
            