class TimeMap:

    def __init__(self):
        self.d = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        #{foo:{1:bar,2:bar2}}
        if key in self.d:
            self.d[key].append([timestamp,value])
        else:
            self.d[key] = [[timestamp,value]]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: 
            return ""
        l,h = 0,len(self.d[key])
        while l<h:
            m = (l+h)//2
            if timestamp <= self.d[key][m][0]:
                h = m
            else:
                l = m+1
        if l == len(self.d[key]):
            return self.d[key][l-1][1]
        elif self.d[key][l][0]!=timestamp and l!=0:
            return self.d[key][l-1][1]
        elif l==0 and self.d[key][l][0]!=timestamp:
            return ""
        else:
            return self.d[key][l][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)