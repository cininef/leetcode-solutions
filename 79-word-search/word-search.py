class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(k, r, c):
            # 1. 停止条件：当前格子已匹配 word[k]，如果是最后一个字符就成功了
            if k == len(word) - 1:
                return True

            tmp = board[r][c]
            board[r][c] = '#'                        # choose：标记已访问
            for dr, dc in DIRS:                      # 所有选择
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n      # 合法：在界内
                        and board[nr][nc] == word[k + 1]):  # 字符匹配（'#' 不会匹配）
                    if backtrack(k + 1, nr, nc):     # explore
                        board[r][c] = tmp
                        return True                  # 短路：找到就停
            board[r][c] = tmp                        # unchoose
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and backtrack(0, r, c):
                    return True
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
