# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        sol = [[root.val]]
        queue = []
        cnt = 0
        if root.left:
            queue.append(root.left)
            cnt += 1
        if root.right:
            queue.append(root.right)
            cnt += 1

        new_cnt = 0
        lst = []
        while queue:
            curr = queue.pop(0)
            lst.append(curr.val)
            if curr.left:
                queue.append(curr.left)
                new_cnt += 1
            if curr.right:
                queue.append(curr.right)
                new_cnt += 1
            cnt -= 1
            if cnt == 0:
                cnt = new_cnt
                new_cnt = 0
                sol.append(lst)
                lst = []

        return sol[::-1]
