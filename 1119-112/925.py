class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name and not typed:
            return True
        if not (name and typed) or len(name) > len(typed):
            return False
        p = q = 0
        while p < len(name) and q < len(typed):
            if name[p] != typed[q]:
                if typed[q] == name[p-1]:
                    q += 1
                    continue
                else:
                    return False
            else:
                p += 1
                q += 1 
        if p == len(name) and q == len(typed):
            return True
        elif p < len(name):
            return False
        else:
            for c in typed[q:len(typed)]:
                if c != name[-1]:
                    return False
            return True
            
name = "vtkgn"
typed = "vttkgnn"
st = Solution()
print st.isLongPressedName(name, typed)