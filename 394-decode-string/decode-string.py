class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        #还是记住 就是进来的到底有什么类别的东西
        #1)数字 3 2 继续stack进去 等着[]出来才pop
        #2）[]遇到[ stack进去 但是]就得立马pop出来然后inplace push进去
        #3）abc alphabeta
        #核心就是 ] 立马把之前2[a]这种pattern计算好 纯alpha之后再push进去
        #step1 always loop the whole str/list first
        for i in range(len(s)):
            #step2:跟之前一样 找到出发pop的条件
            if s[i] == ']':
                a = stack.pop()
                #第一个环节 把[]内部的完全提取出来
                while stack and stack[-1].isalpha():
                    a = stack.pop() + a
                #while之后 说明cur已经是[了
                #再多pop一次 把[ pop出来
                stack.pop()
                num = stack.pop()
                #第二个环节 把[]前的数字完全提取出来
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                res = num * a
                #step3:所有处理结束之后add back
                stack.append(res)
            else:
                stack.append(s[i])
        return "".join(stack)

'''
stack = []                         # 还没被用掉的数字
for x in tokens:
    if x not in "+-*/":            # 🔧 数据：要等运算符
        stack.append(int(x))       # 注意 token 是字符串，要转 int
    else:                          # 操作：现在就能算
        b = stack.pop()            # 先弹出的是右边的数
        a = stack.pop()            # 后弹出的是左边的数
        stack.append(计算(a, x, b)) # 🔧 结果压回去
return stack[-1]                   # 最后只剩答案
'''
'''
s.isalpha()   # 纯字母          "a" "bc" "ABC" ✅   "a1" "[" "2" ❌  394 判断字母
s.isdigit()   # 纯数字          "3" "100" ✅        "-3" "3a" "]" ❌  394 判断重复次数 k（注意负数是 ❌）
s.isalnum()   # 字母或数字       "a" "3" "a2b" ✅    "[" "+" " " ❌    125 回文串，过滤标点和空格
s.islower()   # 字母全是小写     "bc" "a" "a1" ✅    "B" "1" ❌     大小写转换 / 统计
s.isupper()   # 字母全是大写     "BC" "A" "A1" ✅    "b" "1" ❌      大小写转换 / 统计
'''
            