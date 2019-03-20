"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def findtraversal(self,root, res):
        if root:
            res.append(root.val)
            for each in root.children:
                self.findtraversal(each, res)
        
        return res
        
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = list()
        
        return self.findtraversal(root,res)
        
        
        
