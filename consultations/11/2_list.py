# https://leetcode.com/problems/binary-tree-level-order-traversal/
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
        l = [root]
        ans = [[root]]
        while True:
            prev_layer = ans[-1]
            new_layer = []
            for v in prev_layer:
                if v.left is not None:
                    new_layer.append(v.left)
                if v.right is not None:
                    new_layer.append(v.right)
            if len(new_layer) == 0:
                break
            else:
                ans.append(new_layer)
        for l in ans:
            for idx in range(len(l)):
                l[idx] = l[idx].val
        return ans
