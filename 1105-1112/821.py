class Solution(object):
    def tra(self,lst):
        newList = lst[::]
        if lst[0]!=0 and lst[0]==lst[1]:
            newList[0] += 1
        if lst[-1]!=0 and lst[-1]==lst[-2]:
            newList[-1] += 1
        for i in range(len(lst)-2):
            if lst[i+1] != 0 and lst[i+1]==lst[i] and lst[i+1]==lst[i+2]:
                newList[i+1] += 1
        return newList
            
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        t1 = []
        for c in S:
            if c == C:
                t1.append(0)
            else:
                t1.append(1)
        t2 = self.tra(t1)
        while t2 != t1:
            tmp = t1
            t1 = t2
            t2 = self.tra(t1)
        return t2
            
        
st = Solution()
S = "loveleetcode"
C = 'e'
print (st.shortestToChar(S, C))