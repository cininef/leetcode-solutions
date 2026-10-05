class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # still connected component problem
        # use bfs+queue

        rl,cl = len(grid),len(grid[0])
        visit = set()
        queue = deque()
        
        res = 0

        # start at where??
        for sr in range(rl):
            for sc in range(cl):
                if grid[sr][sc] == "1" and (sr,sc) not in visit:
                    queue.append((sr,sc))
                    visit.add((sr,sc))
                    res += 1

                    # here: we only expand center cell=1, otherwise not expanding and just return
                    # step1: traversal all the elements in queue
                    while queue:
                        for i in range(len(queue)): # 按层处理：求最短时间/距离时才需要，否则可以删
                            r,c = queue.popleft()
                            # a. check current is the ending/success or not
                                # -> 有终点：if 【终点】: return 步数
                                # -> 走遍型：直接skip不写
                            
                            # b. check the 4 directions
                            neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                            for dr, dc in neighbors:
                                # c. consider the stopping condition -> skip this pos (BFS 判断的是"邻居")
                                    # c1: out of bound [r<0/c<0] [r==rl/c==cl]
                                if (min(r+dr,c+dc)<0 or r+dr == rl or c+dc == cl or
                                    # c2: already visit
                                    (r+dr, c+dc) in visit or
                                    # c3: meeting obstacles : here when cell = 0 stop expanding
                                    grid[r+dr][c+dc] == "0"):
                                    # skip these
                                    continue
                                # d. what to do on the 4 directions neighbors
                                visit.add((r+dr,c+dc))
                                queue.append((r+dr,c+dc))
        
        return res

                