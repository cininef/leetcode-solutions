# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        #定义一个val=0 next=head的node
        #不用担心head被删除要迁移head 就可以把head当做一个普通节点进行操作
        #同时 prev也不用担心none
        dummy = ListNode(0,head)
        prev,cur = dummy,head
        while cur:
            #是否==val只是影响prev的指向 整体cur最后还是要平移
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            #整体cur最后还是要平移
            cur = cur.next
        return dummy.next
#consider initially prev is None, there's no prev
''''仔细分析 删除一个节点 实际上是三个节点的事情 prev cur next
1.prev:直接把prev.next换成next
2.cur:这个完全舍弃 为了能继续能loop换成next
3.next:完全不用动'''
'''不删除节点：prev cur都往下挪一位
'''


'''Linkedlist基础理解
1.想找到第 3 个节点，只能从 head 开始，顺着箭头一个一个走，不能用下标跳
2.写法	                改了什么
cur = cur.next	   只挪手指，链表本身不变
cur.next = 某节点	改箭头，链表的结构变了
3.trick: dummy 如果head也可能被删除
dummy：给头节点也找一个"前一个"
如果 head 本身要被删，它前面没有节点。解决办法是在最前面加一个假节点：
dummy = ListNode(0, head)     # dummy → head → ...
dummy → [6] → [1] → [6] → None
现在每个真节点都有前一个节点了，删除头节点和删除中间节点的写法完全一样。
-最后返回 dummy.next，因为原来的 head 可能已经被删掉了。
'''