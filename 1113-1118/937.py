class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        digits = []
        for log in logs:
            tmp = log.split()[1]
            if tmp.isalpha():
                letters.append(log)
            else:
                digits.append(log)
        letters.sort(key = lambda x:' '.join(x.split()[1:]))
        return letters + digits