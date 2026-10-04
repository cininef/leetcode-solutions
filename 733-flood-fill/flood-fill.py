class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        #属于找联通块 bfs/dfs traversal完全部 进行inplace modify就行
        # using bfs+queue
        rl, cl = len(image),len(image[0])
        orig = image[sr][sc]
    
        queue = deque()
        #remember current node
        queue.append((sr,sc))
        # paint to self
        image[sr][sc] = color


        #step1: traversal all the elements in queue
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                # a.check current is the ending/success or not
                # equals to c2 c3
                
                # b. check the 4 directions
                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in neighbors:
                    # c. consider the stopping condition -> skip this pos
                        #c1: out of bound [r<-1/c<-1] [r>=rl/c>=cl]
                    if (min(r+dr,c+dc)<0 or r+dr == rl or c+dc == cl or
                        #c2: already visit = 
                        # 1)already poscolor=newcolor 
                        image[r+dr][c+dc] == color or
                        # 2) poscolor != orig -> same as c3
                        #c3: meeting obstacles/can't color
                        image[r+dr][c+dc] != orig):

                        continue
                    # d.none stop, conduct operation on current vertice
                    image[r+dr][c+dc] = color
                    # other basic operation to maintain queue
                    # this r+dr,c+dc pos ,must a legal element in queue
                    queue.append((r+dr,c+dc))

        return image


                



