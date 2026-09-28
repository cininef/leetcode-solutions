class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #step1: create hashtable
        dict = {}
        #nums can be 0
        result = 0

        #step2: understand logic/if condition inside
        #更准确说step2在design hashtable 存储的key:value应该是什么最有insight
        #key要求unique+只能是value；value不应该有与查询有关 否则时间复杂度极速上升

        #dict应该[最后一个consecutive数字:已经维持的result记录]
        #最后返回大的value
        #q: 如果key=最后一个consecutive数字 很容易被人append进来 如果有一个key增长到另一个key的地方
        #key还是要写成list

        #多个list维护状态：也就是如果一个边界被expand 这个interval的所有key都要被expand
        #solution: reference的思路，不能是copy而是reference
        for i in range(len(nums)):
            cur = nums[i]
            #如果和key一样 dubplicate element
            if cur in dict:
                #pass: do nothing
                #continue: to next loop
                continue
            #不可以 cur-1 and cur+1 in dict -> 会变成none判断
            elif cur-1 in dict and cur+1 in dict:
                new = [dict[cur-1][0],dict[cur+1][1]]
                dict[dict[cur-1][0]] = new
                dict[dict[cur+1][1]] = new
                dict[cur] = new
            #cur not seen, but cur-1 exist
            elif cur-1 in dict:
                #means 2 find 1: expand
                L = dict[cur-1][0]
                R = dict[cur-1][1]
                #cur>key=cur-1, only can expand upper bound
                if cur > R:
                    dict[R][1] = cur
                #else means cur is inside [], no operation but copy
                dict[cur] = dict[R]
            elif cur+1 in dict:
                #means 2 find 3: expand
                L = dict[cur+1][0]
                R = dict[cur+1][1]
                if cur < L:
                    dict[cur+1][0] = cur
                #else means cur is inside [], no operation but copy
                dict[cur] = dict[cur+1]
            else:
                dict[cur] = [cur,cur]
        for list in dict.values():
            length = list[1]-list[0]+1
            if length > result:
                result = length
        #step3: return result if there has
        return result
        