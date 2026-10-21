class Solution:
    def findMin(self, nums: list[int]) -> int:
        # no duplicate: unique
        # 现在target一定会在nums里面 不需要len=n
        #binary search的核心：1.找到fftttt从f变成t的分界点 而不只是找到这个target
        #2.l和h的作用 就是最后挪动 都归一到一个位置
        l,h = 0,len(nums)-1
        if nums[l]<= nums[h]:
            return nums[l]
        while l<h:
            m = (l+h)//2
            #这里 不要用l h表示
            if nums[m]<=nums[h]:
                h = m
            else: 
                l = m+1
        return nums[l]
'''m一共就两种情况
    1.在l的increasing 那么 m>=l>=h，m往右走
    2.在h的increasing 那么 m<=h<=l, 那m得往左走
'''