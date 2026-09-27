class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #step 1: establish hashtable
        dict = {}
        result = []
        for i in range(len(strs)):
            #trick：如何检查两个字母组成一样但顺序不一样的str
            #sorted("eat") -> ['a', 'e', 't']
            #"".join['a', 'e', 't'] -> "aet"
            word = "".join(sorted(strs[i]))
            #step2:探讨在table中seen/unseen不同操作！一定记得else是否必须
            
            #if the entered new word already appear in current table, include in result
            #current word strs[i]; in group "word"
            if word in dict.keys():
                idx = dict[word]
                result[idx].append(strs[i])
            #if current node not in result, haven't seen
            #show in both dict, and create new list in result for this combination
            else:
                dict[word] = len(result)
                result.append([strs[i]])
        #step3:一定记得检查是否有返回值
        return result


        