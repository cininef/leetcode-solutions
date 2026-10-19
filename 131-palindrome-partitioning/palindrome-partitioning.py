class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def backtrack(sol,p):
            if p==len(s):
                res.append(sol.copy())
                return
            for i in range(p,len(s)):
                cur = s[p:i+1]
                if cur == cur[::-1]:
                    sol.append(cur)
                    backtrack(sol,i+1)
                    sol.pop()
        backtrack([],0)
        return res
'''
其实还是backtrack的底子 增加palindrome的判断 记住对于一个str
s==s[::-1] time complexity:O(k),O(k)的判断方法
对于backtrack思考几件事情：
1.什么时候是backtrack的终点 算一个solution结束？
->这里应该是 切到最后一个str的屁股 
2.每一次for loop当前所有的choice
->
3.剪枝pruning:判断做这个choice是合法，不然不合法的都不走下去
->这里就是 你如果决定在p切 那么所有p左边就是切好的都要复合palindrome 右边算没切还在等待backtrack
4.在合法的choice底下再次backtrack下一个state的参数

def solve(nums):
    res = []
    sol = []                               # 当前路径（想记录的东西）
    # 额外的状态全都是为了剪枝 / 去重：used、start、k、remain、open/close……

    def backtrack(STATE):                  # STATE = 旋钮①：用什么参数定位“我在哪”
        # ── 1. 记录时机（旋钮②）──
        if 该记录(STATE):                   # 每个节点都收 / 走满才收 / 满足 target 才收
            res.append(sol[:])             # 一定要拷贝
            if 到底了: return              # 子集类不 return，其余类 return
        if 死路(STATE): return             # 提前剪枝：remain<0、越界……

        # ── 2. 选项来源（旋钮③）──
        for choice in 选项(STATE):          # 第k位候选 / nums[start:] / 全集-used
            if not 合法(STATE, choice):     # 剪枝：used、括号数、去重……
                continue
            做选择(choice)                  # sol.append + 更新额外状态
            backtrack(下一状态)             # 旋钮④：k+1 / i+1 / i
            撤销选择(choice)                # sol.pop  + 还原额外状态

    backtrack(初始状态)
    return res
'''