# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        #这个题目要一个inplace的修改
        prev, cur = None, head
        #判断当前的不是none就可以了 next是none也可以继续loop
        #反转核心：每次 1 2 -> 2 1就可以 345保持顺序 存着不要动
        #原始 prev.next = cur
        #现在 cur.next = prev 只改了这里
        #相对顺序是完全没变的 也就是cur=2 下一个要处理的next还是3
        while cur:
            #最好不要 a,b = b,c 容易出问题 是先打包右边所有的 再update左边
            #分析 其实每次都是在 a->b->c prev->cur c->b->a next cur->prev
            nxt = cur.next         # ① 先存下一个，不然改完就找不到了 也就是原顺序下一个要处理的节点
            cur.next = prev        # ② 掉头
            prev = cur             # ③ prev 往前
            cur = nxt              # ④ cur 往前
        return prev                # 新的头