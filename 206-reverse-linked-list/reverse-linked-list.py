# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        #这个题目要一个inplace的修改

        prev, cur = None, head
        while cur:
            nxt = cur.next         # ① 先存下一个，不然改完就找不到了
            cur.next = prev        # ② 掉头
            prev = cur             # ③ prev 往前
            cur = nxt              # ④ cur 往前
        return prev                # 新的头