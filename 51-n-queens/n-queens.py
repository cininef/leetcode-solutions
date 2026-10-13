class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        sol = []
        board = []
        #backtracking
        #try to return all the pos first [1,3,0,2]
        #valid() is flexible, only check the current one
        def valid(board):
            for r1 in range(len(board)):
                for r2 in range(r1+1,len(board)):
                    samecol = (board[r1] == board[r2])
                    samediag = (abs(r2-r1) == abs(board[r1]-board[r2]))
                    if samecol or samediag:
                        return False
            return True

        def search(board):
            #target to stop
            if len(board) == n:
                sol.append(board)
                return
            for i in range(n):
                cur = board + [i]
                if valid(cur):
                    search(cur)
        
        def format(sols):
            res = []
            for j in sols:
                s = []
                for i in j:
                    row = "."*i+"Q"+"."*(n-i-1)
                    s.append(row)
                res.append(s)
            return res
        
        search(board)
        return format(sol)
