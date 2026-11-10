class MinStack:

    def __init__(self):
        #stack LIFO 原始的数据结构都是把最后加入的放在-1
        #但现在要求把最小的弄出来
        #[这次的元素，当前最小]
        self.stack = []

    def push(self, value: int) -> None:
        #inplace 要动结构
        #假装现在已经stack value比最小值还小
        #才需要更新最小值
        if not self.stack or value < self.stack[-1][1]:
            self.stack.append((value,value))
        else:
            self.stack.append((value,self.stack[-1][1]))

    def pop(self) -> None:
        #inplace 要动结构
        #只需要latest
        #一样 如果把stack 最小value弄出来了 得填补这个之前的
        return self.stack.pop()[0]

    def top(self) -> int:
        #get方法 只用查看
        #需要记录最晚进入的元素 latest
        return self.stack[-1][0]

    def getMin(self) -> int:
        #get方法 只用查看latest最新更新的最小值
        #需要记录最小，跟lifo无关 而是每次维护
        return self.stack[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()