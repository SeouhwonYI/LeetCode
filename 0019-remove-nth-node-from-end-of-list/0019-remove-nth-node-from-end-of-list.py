# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [head]
        curr = head.next
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        if len(nodes) == n:
            head = head.next
        elif n == 1:
            nodes[-2].next = None
        else:
            nodes[-n-1].next = nodes[-n+1]
        
        return head

        # res = ListNode(0, head)
        # dummy = res

        # for _ in range(n):
        #     head = head.next
        
        # while head:
        #     head = head.next
        #     dummy = dummy.next
        
        # dummy.next = dummy.next.next

        # return res.next