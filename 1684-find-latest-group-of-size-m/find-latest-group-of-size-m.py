class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        last_step = -1
        d = {}
        countm = 0
        #every step, with one more location shows 1
        #only need to check in each step if there's one fulfill m
        for idx,i in enumerate(arr):
            #i+1 in d -> expand left bound +1
            #i-1 in d -> expand right bound +1
            #else: write this new node into dict
            left = d.get(i-1,0)
            right = d.get(i+1,0)
            ms = left + right + 1
            #update the latest consecutive 1
            d[i] = ms
            d[i-left] = ms
            d[i+right] = ms
            #only need to check in each step if there's one fulfill m
            #more steps will increase the original no. of consecutive 1: 
            #but only affect the interval has m, other will not be affected

            #c2: has m before, need to check whether ms break m
            if left == m:
                countm -= 1
            if right == m:
                countm -= 1

            #c1: no m before, largest < m
            if ms == m:
                countm += 1
            
            if countm > 0:
                last_step = idx+1

        return last_step


        