class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        #anagrams = permutation of the characters
        #initialization left pointer
        l = 0
        #since p may have duplicates, using dict to remember the occurence of char
        state = {}
        res = []
        for i in p:
            state[i] = state.get(i,0)+1
        #state = {"a":1,"b":1} is the counter of p

        for r in range(len(s)):
            # ① r 进来：一定加，不挑
            state[s[r]] = state.get(s[r],0) - 1
            # ② 2A/2C：不合法 → l 不断移除，直到合法
            #case1: r is in p -> state[s[r]]=-1/0/1,2.... <=p里面r的个数,可能是正好，也可能减多了 
            #case2: r is not in p -> state[s[r]]=-1
            #>=0都是valid state 说明window只有p里面的元素 只可能没有够数量 但没有额外元素
            #都通过剔除l 让[l,r]重新合法
            while state[s[r]]<0:
                #把现在的l从窗口剔除
                state[s[l]] += 1
                l += 1
            # ③ 窗口合法 → 记答案
            if r-l+1 == len(p):
                res.append(l)
        return res