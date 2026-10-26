class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        #already sorted
        l,r = 0,len(numbers)-1
        while l<r:
            cur = numbers[l]+numbers[r]
            #因为已经说了 只有一种sol 不会存在numbers>target
            if cur==target:
                return [l+1,r+1]
            #剩下都是需要loop的 并且l会小于target
            elif cur>target:
                r = r-1
            else:
                l = l+1