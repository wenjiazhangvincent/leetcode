class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        dis_list = []
        tmp = 0
        flag = False
        for i, seat in enumerate(seats):
            if seat == 1:
                if flag:
                    dis_list.append(tmp)
                else:
                    dis_list.append(2 * tmp) 
                    flag = True
                tmp = 1
            else:
                tmp += 1
        if seats[-1] == 0:
            dis_list.append(2 * (tmp-1))
        res = max(dis_list) // 2
        return res
                
            