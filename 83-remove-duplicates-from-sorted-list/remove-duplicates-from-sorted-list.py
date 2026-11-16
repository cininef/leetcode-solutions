# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-101,head)
        prev,cur = dummy,head

        while cur:
            #delete one node: only need to change its prev.next
            if cur.val == prev.val:
                #delete cur
                prev.next = cur.next
                
            else:
                prev = cur
            cur = cur.next
        return dummy.next