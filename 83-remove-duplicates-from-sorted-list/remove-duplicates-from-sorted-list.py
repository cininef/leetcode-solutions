# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        #if using dummy, dummy must be outside the return dummy.next,so not same as head.val
        dummy = ListNode(-101,head)
        #记住 任何initialize方法 prev cur都很有可能都是none
        prev,cur = dummy,head

        while cur:
            #delete one node: only need to change its prev.next
            if cur.val == prev.val:
                #delete cur，if delete prev need too many effort
                prev.next = cur.next
                
            else:
                prev = cur
            cur = cur.next
        return dummy.next