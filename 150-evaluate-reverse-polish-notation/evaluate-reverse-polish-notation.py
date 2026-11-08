class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        #conduct inplace inside stack
        stack = []
        operators = {"+","-","*","/"}
        cur = tokens[0]
        # 1.永远是遍历现在list所有元素
        for i in tokens:
            #2.思考这个元素如何分流 i 只有两种可能
            #1)数字 那就直接push进去 等着operator出现
            #2)operator 就要push出来前两个东西 等着操作了
            if i not in operators:
                stack.append(i)
            else:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                if i == '+':
                    cur = n2 + n1
                elif i == '-':
                    cur = n2 - n1
                elif i == '*':
                    cur = n2 * n1
                elif i == '/':
                    cur = n2 / n1
                stack.append(cur)
        return int(cur)
        

'''S2 计算 / 嵌套（150, 394）
stack = []
for x in tokens:
    if x 是"数据":
        stack.append(x)               # 先存着
    else:                             # x 是"操作"
        b = stack.pop()               # 取出最近的
        a = stack.pop()
        stack.append(计算(a, b))       # 结果压回去，留给后面用
return stack[-1]
'''