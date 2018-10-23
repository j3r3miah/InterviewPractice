class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.test(s, set(wordDict))
        
    def test(self, s, wd, memo=None):
        if memo is None:
            memo = {}

        if len(s) == 0:
            return True

        if s in memo:
            return memo[s]

        for wordlen in range(1, len(s) + 1):
            candidate = s[:wordlen]
            if candidate not in wd:
                continue
            remain = s[wordlen:]
            rv = self.test(remain, wd, memo)
            memo[remain] = rv
            if rv:
                return rv

        return False
            

if __name__ == '__main__':
    s = "leetcode"
    d = ["leet","code"]
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    # d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(Solution().wordBreak(s, d))
