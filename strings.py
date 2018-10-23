def hackerrankInString(s):
    h = 'hackerrank'
    hi = 0
    si = 0
    while hi < len(h):
        while si < len(s) and s[si] != h[hi]:
            si += 1
        if si == len(s):
            return 'NO'
        hi += 1
        si += 1
    return 'YES'


def funnyString(s):
    diffs = []
    for i in range(1, len(s)):
        diffs.append(abs(ord(s[i]) - ord(s[i-1])))
    return 'Funny' if diffs == diffs[::-1] else 'Not Funny'


def palindromeIndex(s):
    left = 0
    right = len(s) - 1
    skip = None 

    while left < right:
        print(s[:left], s[left:right+1], s[right+1:], skip)

        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            skipped_left = skip and skip[2] == skip[0]
            skipped_right = skip and skip[2] == skip[1]

            if skipped_right:
                return -1

            if skipped_left:
                left, right = skip[0], skip[1]

            if (
                not skip and
                left + 1 < right and
                s[left+1] == s[right]
            ):
                skip = (left, right, left)
                left += 2
                right -= 1
            elif (
                right - 1 > left and
                s[right - 1] == s[left]
            ):
                skip = (left, right, right)
                left += 1
                right -= 2
            else:
                return -1
        
    return skip[2] if skip else -1


def _palindromeIndex(s):
    def _helper(s, low, high, skips):
        if low >= high:
            return -2

        if s[low] == s[high]:
            return _helper(s, low + 1, high - 1, skips)
        elif not skips:
            skips.append(low)
            if _helper(s, low + 1, high, skips) == -2:
                return low
            skips[0] = high
            if _helper(s, low, high - 1, skips) == -2:
                return high

        return -1

    rv = _helper(s, 0, len(s) - 1, [])
    if rv == -2:
        rv = -1
    return rv


def _find_anagrams(s, b):
    # find all permutations of s within b, e.g.:
    #   s = 'xacxzaa'
    #   b = 'fxaazxacaaxzoecazxaxaz'
    print(s, b)
    freq_diff = [0] * 256  # assume ascii chars
    results = []
    for char in s:
        freq_diff[ord(char)] -= 1
    for i in range(0, len(b)):
        freq_diff[ord(b[i])] += 1
        print('add', b[i], sum(freq_diff))
        if i >= len(s):
            freq_diff[ord(b[i-len(s)])] -= 1
            print('remove', b[i - len(s)], sum(freq_diff))
            print('  check', b[i - len(s):i], sum(freq_diff))
            if sum(freq_diff) == 0:
                results.append(b[i - len(s):i])

    return results


def find_anagrams(s, b):
    # find all permutations of s within b, e.g.:
    #   s = 'xacxzaa'
    #   b = 'fxaazxacaaxzoecazxaxaz'
    # TODO this isn't perfect... it doesn't check the last char in b
    print(s, b)
    results = []
    s_freq = [0] * 256  # assume ascii chars
    b_freq = [0] * 256  # assume ascii chars
    for char in s:
        s_freq[ord(char)] += 1
    for i in range(0, len(b)):
        b_freq[ord(b[i])] += 1
        print('add', b[i])
        if i >= len(s) - 1:
            print('  check', b[i - len(s):i])
            if s_freq == b_freq:
                results.append(b[i - len(s):i])
            b_freq[ord(b[i-len(s)])] -= 1
            print('remove', b[i - len(s)])

    return results


if __name__ == '__main__':

    strings = [
        "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh",
    ]

    # for i, o in enumerate(strings):
    #     print(palindromeIndex(o))

    s = 'xacxzaa'
    b = 'fxaazxacaaxzoecxacxzaa'
    print(find_anagrams(s, b))
