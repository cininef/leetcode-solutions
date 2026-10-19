class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.append([])
        def backtrack(sol,p,count):
            #step1: stop condition,压根就不用count 因为走到后面都无路可走 有限次数
            if count==len(nums):
                res.append(sol)
                return
            #all options next stage
            for idx,i in enumerate(nums[p:]):
                #valid options
                if i==[]:
                    backtrack(sol,idx+p,count+1)
                else:
                    backtrack(sol+[i],idx+p+1,count+1)

        backtrack([],0,1)
        return res
        