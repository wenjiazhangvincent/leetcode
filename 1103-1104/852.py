class Solution(object):
    def check(self,A,left,right):
        i = (left+right)/2
        if A[i]>A[i-1] and A[i]>A[i+1]:
            return i
        elif A[i]<A[i+1]:
            return(self.check(A,i+1,right))
        else:
            return(self.check(A,left,i-1))
            
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return self.check(A,0,len(A)-1)
    
st = Solution()
s = [3,4,5,1]
print(st.peakIndexInMountainArray(s))