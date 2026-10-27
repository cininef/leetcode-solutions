class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 重要特点；binarysearch要求要sorted 无论decreasing/increasing
        # two pointer不需要 只用有规律能够update指针
        # 学习twosum 需要sorted不然那两个pointer没有移动规则
        # fix on the first point, let other two be the two pointers
        #这里 因为数组不是sorted 移动指针毫无效率
        # 应该先sorted
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            #这里单写i==i-1不够对比
            #要限制 如果只有3个元素 i只会查找自己作为第一个元素是否work
            #这时候不应该收到numscheck是否相等的限制 就应该全部加试试看
            if i>0  and nums[i] == nums[i-1]:
                continue
            #1.如何去重i：i一重复所有都没用 ilr必须保证有两个不重复 这样第三个绝对不重复
            while l<r:
                cur = nums[i]+nums[l]+nums[r]
                #记录当前之外 其实还是要继续查找
                if cur == 0:
                    #如何去重2 分析 对于i现在不动 如果l/r再跟之前的一样 那就绝对会重复 所以l/r动一个 就绝对不会出现重复
                    res.append([nums[i],nums[l],nums[r]])
                    r = r-1
                    #只对r检查去重,这样r就会返回一个比之前小的value迫使l右移动
                    '''l右边移动：1.跟原来一样：cur<0,要求l再右移动->没问题 不会让r回到原位重复之前的
                    2.比原来大: cur<=>0都不好说; 但是只要r不会右移就不会有这个问题'''
                    while l<r and nums[r] == nums[r+1]:
                        r = r-1
                if cur > 0:
                    r = r-1
                if cur < 0:
                    l = l+1
        return res
                
            



