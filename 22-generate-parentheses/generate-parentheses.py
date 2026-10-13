class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        pdict = {"(":n-1,")":n}
        def backtrack(sol):
            if len(sol) == 2*n:
                res.append(sol)
                return 
            for p in pdict:
                if pdict[")"] >= pdict["("] and pdict[p]>0:
                    cur = sol+p
                    pdict[p] -= 1
                    backtrack(cur)
                    # return to previous level
                    pdict[p] += 1
        backtrack("(")
        return res