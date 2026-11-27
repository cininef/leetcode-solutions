# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        def reversenodes(l,r):
            #r.next None 让他有终止条件
            prev,cur = l,l.next
            while cur:
                #reverse核心 每次只变动上下游两个node关系 2 3 -> 3 2
                #只需要知道 prev cur next这三个存好了 不然到时候call找不到下一个
                nxt = cur.next
                cur.next = prev
                #为下次更新准备 移动到 3 4
                prev = cur
                cur = nxt
        # 1 2 3 4 5 8 -> 1 5 4 3 2 8 两个端点左右的不变
        #lp:store the before start
        dummy = ListNode(0,head)
        cur,lp,r = dummy,None,None
        i = 0
        while cur:
            #记住i是当前的layer 不能i+1==left会错过判断第一个当前是否是left
            if i == left-1:
                lp = cur
            if i == right:
                r = cur
            cur = cur.next
            i += 1
        #early exit
        if left==right:
            return head
        #根据条件1 <= left <= right <= n；n is len(linkedlist)
        #lp,r 一定是valid
        rn = r.next
        l = lp.next
        r.next = None
        #记住 现在核心就是 不要先更改 lp rn已经存好了两头copy
        reversenodes(lp.next,r)
        lp.next = r
        l.next = rn
        return dummy.next