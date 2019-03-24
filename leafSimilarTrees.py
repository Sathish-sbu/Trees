"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def findChildren(self, node, res):
        if not node:
            return True
        if node.left is None and node.right is None:
            res.append(node.val)
            return res
        else:
            self.findChildren(node.left, res) and self.findChildren(node.right,res)
            return res

        
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res = list()
        res1 = list()
        children1 = self.findChildren(root1, res)
        children2 = self.findChildren(root2, res1)
        return children1 == children2

