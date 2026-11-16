# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        prev, cur = None, head
        while cur is not None:
            if cur.val == val:
                if prev is not None:
                    prev.next = cur.next  # 删中间/尾部节点：prev 保持不动，跳过 cur
                else:
                    head = cur.next       # 删头节点：直接把 head 往后移，prev 依然是 None
            else:
                prev = cur                # 没删节点：prev 才正常跟进到 cur
            
            cur = cur.next                # 无论删没删，cur 都要往后走一步
            
        return head