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


if __name__ == '__main__':
    # pprint(permutations2('abc'))
    pprint(permutations_words(['this', 'that', 'other']))
