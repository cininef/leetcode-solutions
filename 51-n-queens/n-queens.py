class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        sol = []
        board = []
        
        # 用集合来记录已经被占用的列和对角线 (O(1) 的查找时间)
        cols = set()       # 记录列
        pos_diag = set()   # 记录主对角线 (行 - 列)
        neg_diag = set()   # 记录副对角线 (行 + 列)

        def search(r):
            # r 代表当前正在放置第 r 行的皇后
            if r == n:
                sol.append(list(board))  # 必须用 list() 复制一份当前的解
                return
            
            for c in range(n):
                # O(1) 判断当前位置是否合法
                if c in cols or (r - c) in pos_diag or (r + c) in neg_diag:
                    continue
                
                # 做出选择：把皇后放在当前列 c，并记录占用的状态
                cols.add(c)
                pos_diag.add(r - c)
                neg_diag.add(r + c)
                board.append(c)
                
                # 递归搜索下一行
                search(r + 1)
                
                # 撤销选择（回溯）：把刚才放的皇后拿走，尝试下一列
                cols.remove(c)
                pos_diag.remove(r - c)
                neg_diag.remove(r + c)
                board.pop()

        def format(sols):
            res = []
            for j in sols:
                s = []
                for i in j:
                    row = "." * i + "Q" + "." * (n - i - 1)
                    s.append(row)
                res.append(s)
            return res

        # 从第 0 行开始搜索
        search(0)
        return format(sol)