class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for c in moves:
            if c == 'L':
                x -= 1
            elif c == 'R':
                x += 1
            elif c == 'U':
                y += 1
            else:
                y -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False