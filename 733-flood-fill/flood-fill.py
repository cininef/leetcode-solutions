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
        rl, cl = len(image),len(image[0])
        orig = image[sr][sc]

        #思考 recursive dfs模版需要传递什么：当前位置+现在的color
        #需要用helper: image每次recursive重复，color需要重新定义
        #orig原始判断是否渲染的color
        #everystep: judge whether this block color == [sr,sc]'s original color

        def dfs(r,c):
            #1.define ending situations
                #1) out of bound
            if (min(r,c)<0 or
                r == rl or c == cl or
                #2).already visited -> being colored/not meeting condition of being colored
                image[r][c] == color or
                #3).meeting obstacles/skip condition = not meeting condition of being colored
                image[r][c] != orig):
                return
            #define path success/ending condition
            # in previous, we can verify this already equals to orig color
            #now we want to end endless recursive in grid we already colored
            # do noting, as already colored, no extra ending signal

            #what to do to this node: change the color
            image[r][c] = color
            #return the recursive of 4 direction result
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image