# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = [(root, float('-inf'), float('inf'))]
        while s:
            v, l, r = s.pop()
            # not l < v.val < r
            if v.val >= r or v.val <= l:
                return False
            # l < v.val < r
            if v.left is not None:
                # l < v.left < v.val
                s.append((v.left, l, v.val))
            if v.right is not None:
                # v.val < v.right < r
                s.append((v.right, v.val, r))
        return True
