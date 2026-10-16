class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        #every sol store list of numbers[2,2,3]
        def backtrack(sol,sum_sol,p):
            if sum_sol == target:
                res.append(sol)
                return
            for idx,i in enumerate(candidates[p:]):
                #need 3 to get target, current find =<3
                if i <= target - sum_sol:
                    #避免inplace 每次新状态最好新的var
                    cur = sol.copy()+[i]
                    backtrack(cur,sum_sol+i,p+idx)            
        backtrack([],0,0)
        return res




def backtrack(state):
    if 是目标(state):          # 3. 停止条件
        记录或返回解
        return
    for choice in 所有选择(state):    # 2. 每个选择
        if 合法(state, choice):        # 剪枝：不合法就不往下走
            做选择                      #choose
            backtrack(新状态)           #explore：递归，往深处走
            撤销选择                    #unchoose：回到原来的样子
