class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        state = {}
        t_state = {}
        res = ""
        for i in t:
            t_state[i] = t_state.get(i,0) + 1
        for r in range(len(s)):
            #step1: always add current r into state
            state[s[r]] = state.get(s[r],0) + 1
            #step2: move l to make [l,r]valid again
            def valid():
                v = True
                for j in t_state:
                    if state.get(j,0) < t_state[j]:
                        v = False
                return v
            #valid means for every element in t, state has >=1 storage
            while valid():
                #step3: return value
                #很重要 要找的是minimum window 所以得超过历史最小才print
                if len(res)>r-l+1 or res=='' :
                    res = s[l:r+1]
                state[s[l]] -= 1
                l += 1        
        return res
'''
理解
1.s这个[l,r] window >= t的排列组合 s可以有多余元素 但一定要包括t
eg. s_state = {"a":1,"n":2,"b":1} t_state = {"a":1,"b":1}
那么关于t的这些一定要完全一致
'''