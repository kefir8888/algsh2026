# https://leetcode.com/problems/binary-tree-level-order-traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            n = len(q)
            cur_layer = []
            for _ in range(n):
                v = q.popleft()
                cur_layer.append(v.val)
                if v.left is not None:
                    q.append(v.left)
                if v.right is not None:
                    q.append(v.right)
            ans.append(cur_layer)
        return ans