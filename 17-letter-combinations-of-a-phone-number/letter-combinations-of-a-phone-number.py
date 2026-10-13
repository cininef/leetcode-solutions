class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        res = []
        #remember key in dict must be immutable, int is immutable
        dmap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def backtrack(n,sol):
            if len(sol) == len(digits):
                res.append(sol)
                return
            #digits[n] is at number 2 digit n(layer)
            for i in dmap[digits[n]]:
                s = sol+i
                backtrack(n+1,s)

        backtrack(0,"")  

        return res
