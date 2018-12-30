class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in J:
            for j in S:
                if i == j:
                    count += 1
        return count
    
    
