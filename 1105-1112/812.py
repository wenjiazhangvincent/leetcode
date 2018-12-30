class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0 
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
#                     S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
                    tmp = abs((points[i][0]*points[j][1]+points[j][0]*points[k][1]+points[k][0]*points[i][1]\
                               -points[i][0]*points[k][1]-points[j][0]*points[i][1]-points[k][0]*points[j][1])) / 2.0
                    res = max(res,tmp)
        return res