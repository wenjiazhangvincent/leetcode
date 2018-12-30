class Solution(object):
    def delete(self,s):
        for i in range(len(s)):
            if s[i] == '+':
                s = s[0:i]
                break
        ss = []
        start = 0
        for i in range(len(s)):
            if s[i] == '.':
                ss.append(s[start:i])
                start = i + 1
        ss.append(s[start:len(s)])
        s = ''.join(ss)    
        return s
        
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = []
        for email in emails:
            for i in range(len(email)):
                if email[i] == '@':
                    tmp1 = self.delete(email[0:i])
                    tmp2 = email[i+1:len(email)-4]
                    tmp = ('%s@%s.com' %(tmp1,tmp2))
                    if tmp in result:
                        break
                    else:
                        result.append(tmp)
                        break
        return len(result)
                    
st = Solution()
s = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(st.numUniqueEmails(s))