"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:
Return its postorder traversal as: [5,6,3,2,4,1].

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def findtraversal(self,root,res):
        if root:
            for each in root.children:
                self.findtraversal(each, res)
            res.append(root.val)
            
        return res
        
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = list()
        
        return self.findtraversal(root,res)
