class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']
        tmp = list(s)
        p, q = 0, len(tmp)-1
        while p < q:
            while p < len(tmp) and tmp[p] not in vowels:
                p += 1
            while q > 0 and tmp[q] not in vowels:
                q -= 1
            if p < q:
                c = tmp[p]
                tmp[p] = tmp[q]
                tmp[q] = c
                p += 1
                q -= 1
        return ''.join(tmp) 