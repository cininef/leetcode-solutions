class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        #sliding window
        l = 0
        #可以no transaction 如果<=0 profit 所以保底是0
        #记住有方向 一定是r-l
        res = 0
        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l = r
            res = max(prices[r]-prices[l],res)
        return res

'''类似42 就是每个雨水container多大 取决于左右两边min(lmax rmax)
这里 最蠢的brute force 就是按照顺序俩俩对比 
-> 但是完全没必要
stock max只取决于 =  rmax - lmin
只要r取遇到的最max l取遇到的最min  一定是最优值 遇到这个就可以move 
但是这样 还是有两个东西在变化 rl都在变 ：选择method2 固定r 找lmin，因为r遍历了所有的n 所以也是找到了
#注意 这里最重要的一点是 l r相对位置 一定要对
1. 暴力是什么？
   → 枚举所有 (l, r)，O(n²)

2. 枚举所有r，固定r之后，最好的 l 能不能用一个变量记住？
   → 能（比如前面的最小值、最大值）：从左往右扫一遍，O(n)
     例：121


3. 不能的话，能不能从两端出发，每次排除一个？
   → 能：对撞指针，O(n)
     例：11、167、42 的 lmax
最好的value用一个变量被记住 然后每一次对比 历史记录还在
'''
