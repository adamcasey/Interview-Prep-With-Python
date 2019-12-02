'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Input:
[5,4,8,11,null,13,4,7,2,null,null,null,1]
22
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = []
        self.dfs(root, sum, res)
        return any(res)

    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)


# DFS with stack
def hasPathSum2(self, root, sum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right:
            if val == sum:
                return True
        if curr.right:
            stack.append((curr.right, val+curr.right.val))
        if curr.left:
            stack.append((curr.left, val+curr.left.val))
    return False
    
# BFS with queue
def hasPathSum(self, root, sum):
    if not root:
        return False
    queue = [(root, sum-root.val)]
    while queue:
        curr, val = queue.pop(0)
        if not curr.left and not curr.right:
            if val == 0:
                return True
        if curr.left:
            queue.append((curr.left, val-curr.left.val))
        if curr.right:
            queue.append((curr.right, val-curr.right.val))
    return False
