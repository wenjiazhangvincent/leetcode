class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        tmp = S.split(' ')
        res = []
        for i in range(len(tmp)):
            if tmp[i][0] == 'a' or tmp[i][0] == 'e' or tmp[i][0] == 'i' or tmp[i][0] == 'o' or tmp[i][0] == 'u' \
                or tmp[i][0] == 'A' or tmp[i][0] == 'E' or tmp[i][0] == 'I' or tmp[i][0] == 'O' or tmp[i][0] == 'U':
                s = tmp[i] + 'ma' + 'a' * (i+1)
            else:
                s = tmp[i][1:] + tmp[i][:1] + 'ma' + 'a' * (i+1)
            res.append(s)
        return ' '.join(res)
            