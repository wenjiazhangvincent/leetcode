class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        count = 0
        tmp = []
        for s in ops:
            if s == 'D':
                tmp.append(2 * tmp[-1])
            elif s == 'C':
                del(tmp[-1])
            elif s == '+':
                tmp.append(tmp[-2]+tmp[-1])
            else:
                tmp.append(int(s))
        for x in tmp:
            count += x
            
        return count
    
    
st = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print (st.calPoints(ops))