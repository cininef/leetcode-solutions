class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(p,cx,cy):
            #already touch the end return
            if p==len(word):
                return True
            if cx<0 or cx>=len(board) or cy<0 or cy>=len(board[0]):
                return False
            if board[cx][cy]==word[p]:
                #小bug 这个grid不允许重复走 从哪个方向来不能回去
                board[cx][cy] = ''
                xl=backtrack(p+1,cx-1,cy)
                xr=backtrack(p+1,cx+1,cy)
                yu=backtrack(p+1,cx,cy+1)
                yd=backtrack(p+1,cx,cy-1)
                board[cx][cy] = word[p]
                if xl or xr or yu or yd:
                    return True
                else:
                    return False
            else:
                return False
        #define current state
        rl,cl = len(board),len(board[0])
        check = False
        for r in range(rl):
            for c in range(cl):
                if board[r][c] == word[0]:
                    cur = backtrack(0,r,c)
                    if cur == True:
                        return True
                else:
                    continue
        return False

'''
def solve(nums):
    res = []
    sol = []                               # 当前路径（想记录的东西）
    # 额外的状态全都是为了剪枝 / 去重：used、start、k、remain、open/close……

    def backtrack(STATE):                  # STATE = 旋钮①：用什么参数定位“我在哪”
        # ── 1. 记录时机（旋钮②）──
        if 该记录(STATE):                   # 每个节点都收 / 走满才收 / 满足 target 才收
            res.append(sol.copy())             # 一定要拷贝
            return  #到底了:             # 子集类不 return，其余类 return
        if 死路(STATE): return             # 提前剪枝：remain<0、越界……

        # ── 2. 选项来源（旋钮③）──
        for choice in 选项(STATE):          # 第k位候选 / nums[start:] / 全集-used
            if not 合法(STATE, choice):     # 剪枝：used、括号数、去重……
                continue
            做选择(choice)                  # sol.append + 更新额外状态
            backtrack(下一状态)             # 旋钮④：k+1 / i+1 / i
            撤销选择(choice)                # sol.pop  + 还原额外状态

    backtrack(初始状态)
    return res'''
