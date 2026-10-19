class Solution:
    #分析 这是一个决定有的时候可以空 不从list获取类型的题
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        #p代表现在在的nums位置
        #p一直合法index range 因为都在nums里面
        def backtrack(sol,p):
            #step1: stop condition,num already out of range
            if p==len(nums):
                res.append(sol)
                return
            #直接把[]加来这里的loop 这样sol+[]就不会无解了
            #每个layer决定 num开还是[]开
            for i in ([nums[p]],[]):
                backtrack(sol+i,p+1)
        
        backtrack([],0)
        return res

