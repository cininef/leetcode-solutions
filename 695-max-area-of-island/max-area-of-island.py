class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 属于connected components
        # 用 grid[r][c] =0 取代visited set
        # using dfs + recursion
        rl, cl = len(grid), len(grid[0])
        #visit = set() here we change this to 0, to replace visited -> save time and space for hash
        res = 0
        # step1: define dfs(r, c), only carry the changing params r, c
        def dfs(r, c):
            # a. consider the stopping condition -> 判断的是"自己"
                # c1: out of bound [r<0/c<0] [r==rl/c==cl]
            if (min(r, c) < 0 or r == rl or c == cl or
                # c2: already visit
                # c3: meeting obstacles
                grid[r][c]==0):

                return 0 # 有返回值的题：return 0 / False

            # b. check current is the ending/success or not
            # -> 有终点：if 【终点】: return 1 / True
            # -> 走遍型：(none)

            # c. none stop, conduct operation on current vertex, already not 0
            grid[r][c] = 0          # mark visit
            area = 1                   # 涂色 / 计数 / 改值，没有就不写

            # d. check the 4 directions -> recursion
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            # 有返回值的题：res = dfs(...) + dfs(...) + ...（面积要再 + 1）
            return area

            # e. backtrack or not
            # -> 枚举所有路径：visit.remove((r, c))
            # -> 连通块 / 走遍型：不写

        # step2: 【外层】决定起点
        # -> 给了起点：直接 dfs(sr, sc)，不需要 for
        # -> 从边界出发（130/417）：只对四条边上的格子调用 dfs
        # -> 没给起点：双重 for，每找到一个新起点就 dfs 一次
        for sr in range(rl):
            for sc in range(cl):
                if grid[sr][sc]==0:
                    continue
                cur = dfs(sr, sc)
                if cur > res:
                    res = cur         # 这一次 dfs 跑完 = 一整块走完
                 #【一块结束后要做的事】  例如 200：count += 1；695：res = max(res, dfs(sr, sc))

        return res
        