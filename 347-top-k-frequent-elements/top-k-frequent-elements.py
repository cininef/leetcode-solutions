class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        f = {}
        #count the freq first > to table
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        # f[value:freq]
        # then use maxheap to maintain top k
        #first initialize h with size k
        # h = freq value
        # h这时候很难创建 就在for loop遍历的时候一起弄h = list(f.values())[0:k]
        h = []
        # store num,freq tuple need to use items
        for num,freq in f.items():
            heapq.heappush(h,(freq,num))
            if len(h)>k:
                heapq.heappop(h)
                # new elements already>heaptop, pushpop = poppush
                # replace=poppush may fail when k=1

        #res should return the value, not freq
        res = [heapq.heappop(h)[1] for r in range(k)]

        return res
            
        