class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #lr快慢指针 slidingwindow 同向
        l = 0
        #state储存这个substring的搭配 有字母字数限制 
        #set不行 这里s1可能存在重复元素
        #permutation核心：只用记住每个字母出现的次数
        state = {}
        for c in s1:
            state[c] = state.get(c, 0) + 1
        #true：只要有一个连续的 能让所有state变成空 就是true
        #false：loop完所有位置的r 往前的l [l,r]都不能让它空
        for r in range(len(s2)):
            #同向-2：检查 r → l 一直动，滑动窗口
            #2c:属于fixed window size s1的长度固定 所以不需要while一直移动l
            #什么叫做legally在state里减去这个r什么时候是valid r 
            #① r 进来：更新 state（一定加，不挑）第一件事情 永远把r加入现在最新的state里
            state[s2[r]] = state.get(s2[r],0)-1
            #② 判断 [l, r] 合不合法 → 不合法 决定 l 怎么动 让他合法（if 或 while，同时还回 state）
            #核心就是 r不能被移除state 你通过移除l让他重新合法 然后
            #这里不合法是有duplicate
            while state[s2[r]]<0:
                state[s2[l]]+=1
                l += 1
            #这里 所有substring长度得用rl len(state)只是unique element个数
            #③ 现在窗口合法了 → 更新答案
            if r-l+1 == len(s1):
                return True
        return False
'''
'''
            
            
