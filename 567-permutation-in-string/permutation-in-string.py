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
            # state = {"a":2,"c":-2,"b":0},会新加入不在permutation里面的
            #while说明r是在permutation中多余的字符 减多了 
            while state[s2[r]]<0:
                state[s2[l]]+=1
                l += 1
            #这里 所有substring长度得用rl len(state)只是unique element个数
            #③ 现在窗口合法了 → 更新答案
            #l最大可能会到 r+1 这时候length=0窗口空
            if r-l+1 == len(s1):
                return True
        return False

'''
本质区别
	2C（if）	你的 while 版
一直保持的东西	长度 ≤ len(s1)	内容：没有任何字母超量
③ 再检查	内容（全 0）	长度（== len(s1)）
新来的 r 只有两种情况

情况 1：r 不在 s1 里，比如 s1="ab"，r 是 e

减完之后 e: -1，while 一定会触发。
l 一路往右走，把 [l, r) 里所有的字母都还回去，最后把 e 自己也还掉，e 回到 0，while 结束。
这时 l = r + 1。窗口 [r+1, r] 是空的，长度 r - l + 1 = 0。

情况 2：r 在 s1 里，但已经超量了，比如窗口已经有一个 a，又来一个 a

减完之后 a: -1。l 往右走，直到把前面那个 a还回去，a 回到 0 就停。
l 停在旧的 a 后面，新的 a（r）留在窗口里。

（如果 r 在 s1 里而且没超量，while 不触发，l 不动。）
'''