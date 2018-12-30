class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for cpd in cpdomains:
            count = 0
            for i in range(len(cpd)):
                if cpd[i] == '.':
                    count += 1
            x = int(cpd.split(' ')[0])
            t = str(cpd.split(' ')[1])
            print(t)
            if t in d:
                d[t] += x
            else:
                d[t] = x
            for i in range(count):
                s = t.split('.',i+1)[i+1]
                print(s)
                if s in d:
                    d[s] += x
                else:
                    d[s] = x
        
        res = []
        for key in d:
            res.append('%s %s' %(d[key],key))
        return res
    
st = Solution()
s = ["9001 discuss.leetcode.com"]
print(st.subdomainVisits(s))