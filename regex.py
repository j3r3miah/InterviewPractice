class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        si = pi = 0
        while pi < len(p):
            if pi+1 < len(p) and p[pi+1] == '*':
                while si < len(s) and (p[pi] == '.' or s[si] == p[pi]):
                    if self.isMatch(s[si:], p[pi+2:]):
                        break
                    si += 1
                pi += 1  # skip the '*'
            else:
                if si < len(s) and (p[pi] == '.' or s[si] == p[pi]):
                    si += 1
                else:
                    return False
            pi += 1

        return pi == len(p) and si == len(s)

        
if __name__ == '__main__':
    sol = Solution()
    for s, p, m in [
        ('aa', 'a', False),
        ('aa', 'a*', True),
        ('ab', '.*', True),
        ('aab', 'c*a*b', True),
        ('mississippi', 'mis*is*p*.', False),
        ('aaa', 'a*a', True),
        ('a', 'ab*', True),
        ('', 'b*', True),
        ('jeremiah', 'j.r.mia*z*h', True),
    ]:
        assert sol.isMatch(s, p) == m
