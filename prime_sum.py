
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        sieve = [True] * A
        sieve[0] = False
        sieve[1] = False
        x = 2
        while x < len(sieve):
            m = x + x
            while m < len(sieve):
                sieve[m] = False
                m += x
            x += 1
            while x < len(sieve) and sieve[x] is False:
                x += 1

        x = 2
        while x < len(sieve) // 2 + 1:
            if sieve[A-x] is not False:
                return [x, A-x]

            x += 1
            while x < len(sieve) and sieve[x] is False:
                x += 1



if __name__ == '__main__':
    s = Solution()
    print(s.primesum(16777214))
