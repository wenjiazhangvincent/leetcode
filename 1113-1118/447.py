# class Solution(object):
#     def numberOfBoomerangs(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         res = 0
#         if len(points) < 3:
#             return 0
#         for j in xrange(len(points)):
#             for i in xrange(len(points)):
#                 if i == j:
#                     continue
#                 for k in xrange(i+1, len(points)):
#                     if k == j:
#                         continue
#                     if (points[j][0]-points[i][0])**2 + (points[j][1]-points[i][1])**2 \
#                         == (points[j][0]-points[k][0])**2 + (points[j][1]-points[k][1])**2:
#                         res += 1
#         return res*2
    
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        if len(points) < 3:
            return 0
        for j in xrange(len(points)):
            dict = {}
            for i in xrange(len(points)):
                tmp = (points[j][0]-points[i][0])**2 + (points[j][1]-points[i][1])**2
                if tmp in dict:
                    dict[tmp] += 1
                else:
                    dict[tmp] = 1
            for dst in dict.values():
                if dst > 1:
                    res += dst * (dst-1)
        return res
    
points = [[0,0],[1,0],[2,0]]
st = Solution()
print st.numberOfBoomerangs(points)