from pprint import pprint

_memo = {}

def _fibonacciModified(t1, t2, n):
    # top-down
    # fib modified: t3 = t2 ** 2 + t1
    if n == 1:
        return t1
    if n == 2:
        return t2
    if n in _memo:
        return _memo[n]
    rv = (
        _fibonacciModified(t1, t2, n-1) ** 2 +
        _fibonacciModified(t1, t2, n-2)
    )
    _memo[n] = rv
    return rv


def fibonacciModified(t1, t2, n):
    # bottom-up
    minus2 = t1
    minus1 = t2
    ti = None
    for i in range(3, n + 1):
        ti =  minus1 ** 2 + minus2
        minus2 = minus1
        minus1 = ti
    return ti


# TODO how do we return the actual coins instead of the count?
# easier with the bottom-up solution?
def _min_coins(sum, coin_values):
    if sum < min(coin_values):
        return -1
    if sum in coin_values:
        return 1
    if sum in _memo:
        return _memo[sum]

    min_count = None
    for coin in coin_values:
        count = _min_coins(sum - coin, coin_values)
        if count == -1:
            continue
        if min_count is None or count < min_count:
            min_count = count

    if min_count is None:
        _memo[sum] = -1
    else:
        _memo[sum] = min_count + 1

    return _memo[sum]


class CoinSet(dict):
    def add(self, value):
        self.setdefault(value, 0)
        self[value] += 1

    def __len__(self):
        return sum(self.values())


def min_coins(sum, coin_values):
    memo = [None] * (sum + 1)
    memo[0] = CoinSet()
    for cents in range(1, sum + 1):
        if cents < min(coin_values):
            memo[cents] = None
            continue
        min_count = None
        min_set = None
        for coin in coin_values:
            if cents < coin:
                continue
            subset = memo[cents - coin]
            if subset is None:
                continue
            if min_count is None or len(subset) < min_count:
                min_count = len(subset)
                copy = CoinSet(subset)
                copy.add(coin)
                min_set = copy 

        if min_set is None:
            memo[cents] = None
        else:
            memo[cents] = min_set

    min_set = memo[sum]
    return min_set


def coin_ways_count(total, denoms, denoms_to_use=None):
    # every way of making change that adds to `total` using any number of coins
    # with denominations given in array `denom`.
    if denoms_to_use is None:
        denoms_to_use = len(denoms)

    if total == 0:
        return 1
    if total < 0:
        return 0
    if denoms_to_use == 0:
        return 0

    key = (total, denoms_to_use)
    if key in _memo:
        return _memo[key]

    rv = (
        coin_ways_count(total, denoms, denoms_to_use - 1) +
        coin_ways_count(total - denoms[denoms_to_use - 1], denoms, denoms_to_use)
    )
    _memo[key] = rv
    return rv


def coin_ways(total, denoms, denoms_to_use=None):
    if denoms_to_use is None:
        denoms_to_use = len(denoms)

    if total == 0:
        return [[]]
    if total < 0:
        return None
    if denoms_to_use == 0:
        return None

    key = (total, denoms_to_use)
    if key in _memo:
        return _memo[key]

    ways = []

    without_max_denom = coin_ways(total, denoms, denoms_to_use - 1)
    if without_max_denom:
        for way in without_max_denom:
            ways.append(list(way))

    max_denom = denoms[denoms_to_use - 1]
    with_max_denom = coin_ways(total - max_denom, denoms, denoms_to_use)
    if with_max_denom is not None:
        for way in with_max_denom:
            cway = list(way)
            cway.append(max_denom)
            ways.append(cway)

    _memo[key] = ways
    return ways


# cleaner `coin_ways_count`
def W(A, D, di=0):
    if di == len(D):
        return 0
    if A < 0:
        return 0
    if A == 0:
        return 1
    key = (A, di)
    if key in _memo:
        return _memo[key]
    rv = W(A - D[di], D, di) + W(A, D, di + 1)
    _memo[key] = rv
    return rv


# TODO this is wrong
def M(A, D):
    if A < 0:
        return -1
    if A == 0:
        return 0
    if A in D:
        return 1
    if A in _memo:
        return _memo[A]
    minval = None
    for d in D:
        val = M(A - d, D)
        if val == -1:
            continue
        if minval is None or val > minval:
            minval = val
    rv = (1 + minval) if minval is not None else -1
    _memo[A] = rv
    return rv


def _equal_chocolates(A):
    # print(A)
    if len(set(A)) == 1:  # all items are equal
        return 0  # zero moves to equalize

    if min(A) < 0:
        return -1

    key = tuple(A)
    if key in _memo:
        return _memo[key]

    min_moves = None
    for num_chocolates in (1, 2, 5):
        for i in range(len(A)):
            next_A = list(A)
            next_A[i] -= num_chocolates
            # count the number of moves to solution from new state
            moves = _equal_chocolates(next_A)
            if moves == -1:
                continue
            if min_moves is None or moves < min_moves:
                min_moves = moves

    if min_moves is None:
        rv = -1
    else:
        rv = 1 + min_moves

    _memo[key] = rv
    return rv


def equal_chocolates(A):
    global _memo
    _memo = {}
    target = min(A)
    try1 = _equal(A, target=target)
    _memo = {}
    try2 = _equal(A, target=target - 1)
    _memo = {}
    try3 = _equal(A, target=target - 2)
    return min(try1, try2, try3)

def _equal(A, target):
    total_moves = 0
    for i in range(len(A)):
        val = A[i]
        if val in _memo:
            total_moves += _memo[val]
            continue
        moves = 0
        while val > target:
            if val - 5 >= target:
                val -= 5
            elif val - 2 >= target:
                val -= 2
            else:
                val -= 1
            moves += 1
        _memo[A[i]] = moves
        total_moves += moves
    return total_moves


def power_set(S):
    # the set of all subsets of S including empty set and S itself
    L = list(S)
    R = [set()]
    for i in range(len(L)):
        additem = L[i]
        oldlen = len(R)
        for j in range(oldlen):
            copy = set(R[j])
            copy.add(additem)
            R.append(copy)
    return R


def test_power_set():
    # subsets = power_set({8, 4, 9, 1, 7})
    subsets = power_set({'a', 'b', 'c'})
    subsets = sorted(subsets, key=lambda o: len(o))
    pprint(subsets)


def permutations(s):
    # return all permutations of string of unique chars
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    rv = []
    for i, c in enumerate(s):
        ss = s[:i] + s[i+1:]
        for sp in permutations(ss):
            rv.append(c + sp)
    return rv


def permutations_no_dupes(s):
    # return all permutations of string of non-unique chars
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    rv = []
    seen = set()
    for i, c in enumerate(s):
        if c in seen:
            continue
        ss = s[:i] + s[i+1:]
        for sp in permutations_no_dupes(ss):
            rv.append(c + sp)
        seen.add(c)
    return rv


def test_permutations_of_string():
    s = 'abaca'
    perms = permutations(s)
    pprint(perms)  # => 5! = 120
    print(len(perms))
    print()
    nodupes = permutations_no_dupes(s)
    pprint(nodupes)  # => 5!/3! = 20
    print(len(nodupes))
    assert(set(perms) == set(nodupes))


def parens(n):
    last_set = set()
    if n == 0:
        return last_set
    last_set.add('()')
    if n == 1:
        return last_set
    for i in range(2, n + 1):
        new_set = set()
        for o in last_set:
            new_set.add('(' + o + ')')
            new_set.add('()' + o)
            new_set.add(o + '()')
        last_set = new_set
    return last_set


def test_parens():
    pprint(parens(0))
    pprint(parens(1))
    pprint(parens(2))
    pprint(parens(3))
    pprint(parens(4))



def knapsack_subset_sum(aset, total, n, rv, sofar=None):
    # this is analogous to the menu items problem Airbnb asked me
    if sofar is None:
        sofar = []

    if total < 0:
        return

    if n == 0 and total > 0:
        return

    if total == 0:
        rv.append(sofar)
        return

    o = aset[n-1]
    knapsack_subset_sum(aset, total - o, n, rv, sofar + [o])
    knapsack_subset_sum(aset, total, n-1, rv, sofar)


def test_knapsack_subset_sum():
    rv = []
    aset = [3, 7, 8, 9]
    knapsack_subset_sum(aset, 22, len(aset), rv)
    pprint(sorted(rv))


if __name__ == '__main__':
    # test_knapsack_subset_sum()

    print(sorted(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]))
    print(sorted(["()()(())","()(()())","(())()()","((())())","(()(()))","()((()))","(((())))","((()()))","((()))()","()(())()","()()()()","(()()())","(()())()"]))
