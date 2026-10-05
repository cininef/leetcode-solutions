class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # still connected component problem
        # use dfs first

        rl,cl = len(grid),len(grid[0])
        visit = set()

        #明确dfs就是起到遍历的效果 只是为了不重复的访问在边界的点+记录visited 不参与任何计数
        def dfs(r,c):
            #a. consider the stopping condition of current node
            # a1: out of bound [r<0/c<0] [r==rl/c==cl]
            if (min(r,c)< 0 or r == rl or c == cl or
            # a2: already visit
                (r,c) in visit or
            # a3: meeting obstacles / can't do -> means=0 can't expand need to find next node can expand 当前就是障碍 无法返回
                grid[r][c]== "0"):
                
                return 
            #b.consider the success condition of ending,already find allof them
            # mean cell = 1
            #c.do to current node -> can expand
            visit.add((r,c))

            # d. check the 4 directions -> recursion   
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        count = 0
        #for loop为了多起点 避免dfs任意起点开始 直接被stuck住 遇到0不走
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == "1" and (r,c) not in visit:
                    count += 1
                    dfs(r,c)
       
        return count
        