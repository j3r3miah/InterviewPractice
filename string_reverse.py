

def reverse(s):
    # s = 'foo'
    # n = 3; range(0, 1)
    # i = 0: tmp = s[0] = 'f'; s[0] = s[3-1-0] = s[2] = 'o'; s[2] = 'f'
    #
    # s = 'heyo'
    # n = 4; range(0, 2)
    # i = 0: tmp = 'h'; s[0] = s[3] = 'o'; s[3] = 'h'
    # i = 1: tmp = 'e'; s[1] = s[2] = 'y'; s[2] = 'e'
    #
    n = len(s)
    s = list(s)
    for i in range(0, int(n/2)):
        tmp = s[i]
        s[i] = s[n-1-i]
        s[n-1-i] = tmp
    return ''.join(s)


def reverse2(s):
    # s = 'lovebeer'
    # n = 8, range(0, 4, 2): 0, 2
    # i = 0:
    #   tmp = s[0:2] = 'lo'
    #   s[0] = s[6] = 'e'
    #   s[1] = s[7] = 'r'
    #   s[6] = 'l'
    #   s[7] = 'o'
    #   s = 'ervebelo'
    s = list(s)
    n = len(s)
    assert(n % 2 == 0)
    for i in range(0, int(n/2), 2):
        tmp = s[i:i+2]
        s[i] = s[n-2-i]
        s[i+1] = s[n-1-i]
        s[n-2-i] = tmp[0]
        s[n-1-i] = tmp[1]
    return ''.join(s)



if __name__ == '__main__':
    import sys
    input = sys.argv[1]
    print('{} => {}'.format(input, reverse(input)))
    print('{} => {}'.format(input, reverse2(input)))
