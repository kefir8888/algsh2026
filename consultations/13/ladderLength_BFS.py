# https://leetcode.com/problems/word-ladder/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        dist = {beginWord: 1}
        q = deque([beginWord])
        while q:
            v = q.popleft()
            if v == endWord:
                return dist[v]
            # 5000
            # 10 * 25 << 5000
            for idx in range(len(v)):
                # s = "01234"
                # s[:2] = "01"
                for c in "abcdefghijklmnopqrstuvwxyz":
                    u = v[:idx] + c + v[idx + 1:]
                    if u in wordSet and u not in dist:
                        dist[u] = 1 + dist[v]
                        q.append(u)
        return 0