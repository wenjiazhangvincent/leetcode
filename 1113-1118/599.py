class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dup = set(list1) & set(list2)
        res = []
        MAX = 0xFFFFFFFF
        for s in dup:
            tmp = list1.index(s) + list2.index(s)
            if tmp < MAX:
                MAX = tmp
                res = [s]
            elif tmp == MAX:
                res.append(s)
        return res  