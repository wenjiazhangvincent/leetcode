# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, sum, visited):
            if not root:
                return 0
#             visited.append(root.val)
            visited = visited + [root.val]
            found, cur_sum = 0, 0
            for x in visited[::-1]:
                cur_sum += x
                if cur_sum == sum:
                    found += 1
            return found + dfs(root.left, sum, visited) + dfs(root.right, sum, visited)
        
        return dfs(root, sum, [])