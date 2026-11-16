# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        prev,cur = None,head
        while cur is not None:
            #consider initially prev is None, there's no prev
            ''''仔细分析 删除一个节点 实际上是三个节点的事情 prev cur next
            1.prev:直接把prev.next换成next
            2.cur:这个完全舍弃 为了能继续能loop换成next
            3.next:完全不用动'''
            '''不删除节点：prev cur都往下挪一位
            '''
            if cur.val == val:
                #if head就已经=val 要换head
                if not prev:
                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head