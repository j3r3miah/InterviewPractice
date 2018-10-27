import math
from pprint import pprint


def cut_sticks(arr):
    arr.sort(reverse=True)
    rv = []
    while len(arr):
        rv.append(len(arr))
        i = len(arr) - 1
        minval = arr[i]
        while i >= 0 and arr[i] == minval:
            i -= 1
        del arr[(i + 1):]
    return rv


def swap(a, b):
    a = b - a
    b = b - a
    a = a + b
    return a, b


def swap2(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a, b


def highest_population(data):
    # data: list of birth/death year pairs
    # assume all years in range [1900, 2000]
    A = [0] * 101
    for pair in data:
        birth = pair[0]
        death = pair[1]
        A[birth - 1900] += 1
        A[death + 1 - 1900] -= 1
    pop = 0
    maxpop = 0
    maxyear = None
    for i, diff in enumerate(A):
        pop += diff
        if pop > maxpop:
            maxpop = pop
            maxyear = 1900 + i
    return maxyear, maxpop

def test_highest_population():
    print(highest_population([
        (1900, 1904),
        (1901, 1903),
        (1900, 1902)
    ]))


def factors(n):
    rv = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            rv.append(i)
            if i != math.sqrt(n):
                rv.append(int(n / i))
    return sorted(rv)


def test_factors():
    for i in {9, 12, 60}:
        print(i, factors(i))


def permutations(s):
    if len(s) == 0:
        return [[]]
    rv = []
    for i, c in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for o in permutations(remaining):
            rv.append([c] + o)
    return rv


def permutations2(s, prefix=''):
    if len(s) == 0:
        return [prefix]
    rv = []
    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        rv.append(
            permutations2(remaining, prefix + s[i])
        )
    return rv


def permutations_words(words, prefix=None):
    if prefix is None:
        prefix = []
    if len(words) == 0:
        return prefix
    rv = []
    for i, w in enumerate(words):
        rv.append(permutations_words(
            words[:i] + words[i+1:],
            prefix + [words[i]]
        ))
    return rv


def three_sum(nums):
    rv = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j, k = i+1, len(nums)-1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                rv.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
            elif sum < 0:
                j += 1
            else:
                k -= 1

    return rv

def threeSumSmaller(nums, target):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        j = i+1
        k = len(nums) - 1
        
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < target:
                count += (k - j)
                for z in range(j+1, k+1):
                    print(nums[i], nums[j], nums[k])
                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
            else:
                k -= 1
                
    return count


def triangleOrNot(a, b, c):
    rv = []
    for a, b, c in zip(a, b, c):
        if a + b > c and b + c > a and a + c > b:
            rv.append('Yes')
        else:
            rv.append('No')
    return rv


def consecutive_sum_(S):
    l = 0
    h = 1
    total = 1
    count = 0
    while h <= (S // 2 + 1):
        if total == S:
            count += 1
            # r = range(l, h+1)
            # print(list(r), '->', sum(r))
        if l == h or total <= S:
            h += 1
            total += h
        else:
            total -= l
            l += 1
    return count


def consecutive_sum(S):
    count = 0
    n = 2
    while True:
        i = float(2*S - n*n + n) / float(2*n)
        if i <= 0:
            break
        if i % 1 == 0:
            count += 1
            # r = range(int(i), int(i)+n)
            # print(list(r), '->', sum(r))
        n += 1
    return count


def jumping_jack(n, k):
    # print('n', n, 'k', k)
    max_steps = (n*n + n)/2

    # solve gauss's equation, starting at 1, for a sum equal to k:
    #    (n^2 + n ) / 2 = k
    x = int(math.sqrt(2*k))
    if x/2 * (x + 1) == k:
        # the sum of integers from 1..x = k, so we would hit bad step
        # skip first step so we avoid the bad step
        max_steps -= 1

    return int(max_steps)



def usernameDisparity(inputs):
    rv = []
    for s in inputs:
        count = len(s)
        for x in range(1, len(s)):
            pi = x
            si = 0
            while pi < len(s) and s[pi] == s[si]:
                pi += 1
                si += 1
            count += si
        rv.append(count)
    return rv



import sys
from pprint import pprint

def interpolate_mercury(measurements):
    for i, v in enumerate(measurements):
        if v is not None:
            continue
        sum = 0
        count = 0
        # get prev value
        x = i - 1
        while x > 0 and measurements[x] is None:
            x -= 1
        if x > 0:
            sum += measurements[x]
            count += 1
        # get next value
        x = i + 1
        while x < len(measurements) and measurements[x] is None:
            x += 1
        if x < len(measurements):
            sum += measurements[x]
            count += 1

        avg = sum / count
        # print(v, avg)
        print(avg)


def read_input():
    input = sys.stdin.readlines()[1:]
    measurements = [
        line.split('\t')[-1].rstrip() for line in input
    ]
    return [
        None if o.startswith('Missing') else float(o) for o in measurements
    ]


def _numberOfPaths(a, i=0, j=0, memo=None):
    # this hits recursion limit in 1000x1000 matrix
    if memo is None:
        memo = {}

    n = len(a)
    m = len(a[0])

    if i >= n or j >= m or a[i][j] == 0:
        return 0
    if i == n - 1 and j == m - 1:
        return 1

    if (i, j) not in memo:
        memo[(i, j)] = (
            _numberOfPaths(a, i+1, j, memo) +
            _numberOfPaths(a, i, j+1, memo)
        ) % (10**9 + 7)

    return memo[(i, j)]


def numberOfPaths(a):
    # bottom-up dynamic programming / tabulation
    n = len(a)
    m = len(a[0])
    memo = [[None] * m for _ in range(n)]
    memo[n-1][m-1] = 1

    for i in reversed(range(0, n)):
        for j in reversed(range(0, m)):
            if a[i][j] == 0:
                memo[i][j] = 0
            elif i == n - 1 and j == m - 1:
                memo[i][j] = 1
            else:
                sum = 0
                if i + 1 < n:
                    sum += memo[i+1][j]
                if j + 1 < m:
                    sum += memo[i][j+1]
                memo[i][j] = sum % (10**9 + 7)

    return memo[0][0]


if __name__ == '__main__':
    # pprint(permutations2('abc'))
    # pprint(permutations_words(['this', 'that', 'other']))
    # print(three_sum([0, 0, 0]))
    # print(three_sum([-1, 0, 1, 2, -1, -4]))
    # assert(three_sum([-1, 0, 1, 2, -1, -4]) == {{-1, 0, 1}, {-1, -1, 2}})
    # print(threeSumSmaller([3,1,0,-2], 4))
    # print(triangleOrNot([7, 10, 7], [2, 3, 4], [2, 7, 4]))
    # S = 10**4 + 67834
    # S = 21
    # print(consecutive_sum(S))
    # print(consecutive_sum_(S))
    # import sys
    # print(jumping_jack(int(sys.argv[1]), int(sys.argv[2])))

    # print(usernameDisparity([
    #     1000 * ('ababaababaababaababaababaababaababaababa'
    #             'ababaababaababaababaababaababaababaababa'
    #             'ababaababaababaababa')
    # ]))

    # interpolate_mercury(read_input())

    import random
    weight = 92
    A = [
        [1 if random.randint(0, 100) < weight else 0 for _ in range(200)]
        for __ in range(200)
    ]
    rv = numberOfPaths(A)
    print(rv)
    assert(_numberOfPaths(A) == rv)

    # print(numberOfPaths2([
    #     [1, 1, 1, 1],
    #     [1, 1, 1, 0],
    #     [1, 1, 1, 1],
    #     [1, 1, 0, 1],
    #     [1, 1, 1, 1],
    # ]))

    # print(numberOfPaths2([
    #     [1, 1],
    #     [1, 1],
    # ]))
