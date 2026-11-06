class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        #fixed window size k
        l = 0
        res = []
        #using monotonic queue to store current window
        #monotonic queue:pop出队头过期的元素 队尾出太小的
        state = deque()
        #remember 这里r只移动一轮
        for r in range(len(nums)):
            #maintain monotic queue for state [1,2,3..]
            #还是1. 把r加入state 不管三七二十一
            #一样 这里跟2a那个题一样 不能闲加入 有总数限制 先踢出去一个再进来
            #更新l的规则：1.首先避免state-1outofrange 先确保state没全走完；2.看state这时候最大值 如果都没有r大 那明显可以把最小的踢了 留着也没用
            while state and nums[state[-1]]<=nums[r]:
                state.pop()
            state.append(r)
            #第二条：为了fixed windowsize 每次都在[l,r]fixed window size
            #这时候 说明新加入的r 让window超了 在要移动l一位
            #这里 state里面是按照顺序储存 l，r 现在应该到l+1了 但也只有l太大才会影响这个
            #state[0]就是index最小的东西 如果在上一个把l正好踢走了 也不用在pop了
            if r-l+1>k:
                if state[0] == l:
                    state.popleft()
                l += 1
            if r - l + 1 == k:
                res.append(nums[state[0]])

        return res

'''
基础语法 不管stack queue 他们都只知道 lifo fifo
按照顺序/大小/规则 都是我们自己压入元素的时候自己维护
stack：用 list
stack = []
stack.append(x)     # 压入顶部        O(1)
stack.pop()         # 弹出顶部并返回    O(1)
stack[-1]           # 看顶部，不弹出
if stack:           # 判断非空

queue：用 deque（不要用 list）
from collections import deque
q = deque()
q.append(x)         # 从队尾进        O(1)
q.popleft()         # 从队头出并返回    O(1)
q[0]                # 看队头
if q:               # 判断非空

⚠️ 不要用 list.pop(0) 当队列：它要把后面所有元素往前挪一格，是 O(n)。

deque：四个方向都行
from collections import deque
dq = deque()
dq.append(x)        # 右边进
dq.appendleft(x)    # 左边进
dq.pop()            # 右边出
dq.popleft()        # 左边出
dq[0], dq[-1]       # 看两头

四个操作全部都是 O(1)。
'''
