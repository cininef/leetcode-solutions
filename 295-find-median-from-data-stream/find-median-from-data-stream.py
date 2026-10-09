class MedianFinder(object):

    def __init__(self):
        self.arr = []
        #minh存小半边数字 maxheap heaptop=最大元素
        self.minh = []
        #maxh存大半边 维持minheap heaptop=最小元素
        self.maxh = []
# elements are plugin one by one: heap is enough, no need extra arrays
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minh) == 0:
            heapq.heappush(self.minh,-num)
        elif num <= -self.minh[0]:
            heapq.heappush(self.minh,-num)
        else: 
            #num > maxh[0]:
            heapq.heappush(self.maxh,num)
        if len(self.minh)<len(self.maxh):
            e = heapq.heappop(self.maxh)
            heapq.heappush(self.minh,-e)
        elif len(self.minh)>len(self.maxh)+1:
            e = -heapq.heappop(self.minh)
            heapq.heappush(self.maxh,e)
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minh) == len(self.maxh):
            return (-self.minh[0]+self.maxh[0])/2
        else:
            return -self.minh[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# question notes: 有分odd/even
#看着就感觉是double heap
#基础heap的原理是返回topkelements

