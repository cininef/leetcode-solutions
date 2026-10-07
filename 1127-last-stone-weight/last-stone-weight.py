class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #heap：对于top k个最大的 效果好/对整体heapify再对topk操作的
        h = [-s for s in stones]
        heapq.heapify(h)
        while True:
            if len(h) == 1:
                return -h[0]
            if len(h) == 0:
                return 0
            # return the top1 of maxheap -s
            t1 = heapq.heappop(h)
            t2 = heapq.heappop(h)
            if t1==t2:
                continue
            else:
                new = t1-t2
                heapq.heappush(h,new)
            

        