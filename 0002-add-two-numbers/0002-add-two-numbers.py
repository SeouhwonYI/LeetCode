# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = l1.val, l2.val
        sol = ListNode(val = (a+b)%10)
        result = sol
        up = (a+b)//10
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            a = l1.val
            b = l2.val
            val = a+b+up
            sol.next = ListNode(val % 10)
            sol = sol.next
            up = val // 10
        while l1.next:
            l1 = l1.next
            a = l1.val
            val = a+up
            sol.next = ListNode(val % 10)
            sol = sol.next
            up = val // 10
        while l2.next:
            l2 = l2.next
            a = l2.val
            val = a+up
            sol.next = ListNode(val % 10)
            sol = sol.next
            up = val // 10
        if up:
            sol.next = ListNode(1)
        return result
        