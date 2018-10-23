
def match(input, pattern, map=None, seen=None):
    if map is None:
        map = {}
    if not seen:
        seen = set()
    if not input and not pattern:
        return True
    if not input or not pattern:
        return False
    key = pattern[0]
    if key in map:
        val = map[key]
        if input.startswith(val):
            return match(input[len(val):], pattern[1:], map, seen)
        else:
            return False
    else:
        for i in range(1, len(input) - len(pattern) + 2):
            substring = input[:i]
            if substring in seen:
                continue
            map[key] = substring
            seen.add(substring)
            if match(input[i:], pattern[1:], map, seen):
                return True
            seen.remove(substring)
            del map[key]
        return False


if __name__ == '__main__':

    tests = [
        ('catcatgocatgo', 'aabab', True),
        ('catcatgocatgo', 'a', True),
        ('catcatgocatgo', 'ab', True),
        ('catcatgocatgo', 'b', True),
        ('catcatgocatgo', 'ababa', False),
        ('redblueyellowblueredblueblue', 'rbybrbb', True),
        ('xx', 'aa', True),
        ('xx', 'ab', False),
        ('xxyxx', 'aba', True),
        ('xxyyyyyxx', 'aba', True),
        ('xx123abzxx123', 'aba', True),
        ('', '', True),
        ('x', '', False),
        ('x', 'a', True),
    ]

    for o in tests:
        map = {}
        if match(o[0], o[1], map) != o[2]:
            print("FAIL: " + str(o))
        else:
            print("SUCCESS: " + str(o))
            print(str(map))
        print()
