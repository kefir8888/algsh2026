# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_subtree(node, l, r):
            if node is None:
                return True
            return (l < node.val < r) and check_subtree(node.left, l, node.val) and check_subtree(node.right, node.val, r)
        return check_subtree(root, float('-inf'), float('inf'))
