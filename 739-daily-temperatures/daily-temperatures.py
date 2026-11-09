class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        #monotonic+LIFO[stack]
        stack = []
        res = [0]*len(temperatures)
        #理解题目 就是如果你新来的temp比前一个高 那前面就可以一直pop出去
        #monotonic规则:都是新来的把队尾/栈顶比它小的踢掉。单调队列就是单调栈 + 尾部前面过期弹出(从尾部)。
        #也就是 我这里希望increasing 如果遇到decreasing一下的就需要stack进去了
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]: 
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
        return res

'''S4 单调栈（739, 853, 84）⭐ 重点：和 239 的单调队列几乎一样，只是不需要弹队头：
记住这里必须存index而不是value在stack里面 这样会导致算不出来现在的相差多少
stack = []                            # 存下标
ans = [0] * len(nums)
for i in range(len(nums)):            # i 相当于 r
    # ① 检查 i 和栈顶：i 能"解决"栈顶吗？能就一直弹
    while stack and nums[stack[-1]] < nums[i]:
        j = stack.pop()
        ans[j] = i - j                # ② 栈顶 j 等到了答案（比如右边第一个更大的数）
    # ③ i 自己还没等到答案，压进去
    stack.append(i)
return ans

🔧 要换的格子：

比较方向：< 找右边第一个更大的数，> 找右边第一个更小的数。
弹出时记什么：距离 i - j，或者值 nums[i]，或者面积（84）。
'''