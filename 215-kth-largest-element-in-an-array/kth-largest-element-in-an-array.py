import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #method 3: min heap
        #place the smallest element on the heap, can replace it from top
        #initialize a heap first, then replace
        #heapify is inplace, can't assign
        heap_ofmax = nums[0:k]
        heapq.heapify(heap_ofmax)
        if k == len(nums):
            return heap_ofmax[0]
        for i in nums[k:]:
            #现在我们想要的是 如果新的i>现在的heap 就要加入
            #跟pushpop/replace默认的 新元素更小相反
            if i > heap_ofmax[0]:
                heapq.heapreplace(heap_ofmax,i)
        return heap_ofmax[0]
        