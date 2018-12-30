class Solution(object):
    def __init__(self):
        self.m = {
            5:0,
            10:0
            }
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return True
        for x in bills:
            if x == 5:
                self.m[5] += 1
            elif x == 10:
                if self.m[5]:
                    self.m[5] -= 1
                    self.m[10] += 1
                else:
                    return False
            else:
                if self.m[5] and self.m[10]:
                    self.m[5] -= 1
                    self.m[10] -= 1
                elif self.m[5] >= 3:
                    self.m[5] -= 3
                else:
                    return False
        return True

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
st = Solution()
print st.lemonadeChange(bills)