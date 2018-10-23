def num1bits(n):
    ones = 0
    while n > 0:
        if n % 2 == 1:
            ones += 1
        n >>= 1
    return ones


if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    print(bin(n), '->', num1bits(n))
