class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l1 = []
        l2 = []
        for i in range(len(A)):
            if (i%2)^(A[i]%2) != 0:
                if i%2 == 0:
                    l1.append(i)
                else:
                    l2.append(i)
        for i in range(len(l1)):
            tmp = A[l1[i]]
            A[l1[i]] = A[l2[i]]
            A[l2[i]] = tmp
        return A
            