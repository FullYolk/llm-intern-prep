# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        p = head
        head1 = None
        q = head1
        while p != None:
            stack.append(p.val)
            p = p.next
        while stack != []:
            p = stack.pop()
            if head1 == None:
                new_node = ListNode(p)
                head1 = new_node
                q = head1
            else:
                q.next = ListNode(p)
                q = q.next
        return head1
## 以上为暴力法 空间复杂度O（N）

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            prev = None
            while curr != None:
                 nxt = curr.next
                 curr.next = prev
                 prev = curr
                 curr = nxt
            return prev
## 双指针法