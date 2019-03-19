"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def check(self,node, value):
        if not node:
            return True
        elif node.val != value:
            return False
        elif node.val == value:
            return self.check(node.left, value) and self.check(node.right, value)
        
        
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        unival = root.val
        return self.check(root, unival)
