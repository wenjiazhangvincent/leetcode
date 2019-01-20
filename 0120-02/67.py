class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def transform(c):
            return True if c == '1' else False
        def detransform(bool):
            return '1' if bool else '0'
        
        a = map(transform, list(a))
        a.reverse()
        b = map(transform, list(b))
        b.reverse()
        if len(a) > len(b):
            tmp = a
            a = b
            b = tmp
        res = ''
        _add = False
        for i in xrange(len(a)):
            _tmp = a[i] ^ b[i] ^ _add
            _add = a[i] | b[i] if _add else a[i] & b[i]
            res += detransform(_tmp)
        for i in xrange(len(a), len(b)):
            _tmp = b[i] ^ _add
            _add = b[i] & _add
            res += detransform(_tmp)
        if _add:
            res += '1'
        res = res[::-1]
        return res
    
a = '11'
b = '1'
st = Solution()
print st.addBinary(a, b)