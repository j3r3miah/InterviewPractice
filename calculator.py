import pytest


class InvalidExpression(Exception):
    pass


def calculate(expr):
    rv = None
    op = None
    num = None

    i = 0
    while i < len(expr) + 1:
        c = expr[i] if i < len(expr) else ' '

        if c.isdigit():
            if num is None:
                num = int(c)
            else:
                num *= 10
                num += int(c)
        else:
            # finish process num
            if num is not None:
                if rv is None:
                    rv = num
                elif op == '+':
                    rv += num
                elif op == '-':
                    rv -= num
                else:
                    raise InvalidExpression()
                num = None
                op = None

            # process next char
            if c.isspace():
                pass
            elif c == '(':
                p = i + 1
                cnt = 1
                while cnt > 0:
                    if expr[p] == '(':
                        cnt += 1
                    elif expr[p] == ')':
                        cnt -= 1
                    p += 1
                num = calculate(expr[i+1:p-1])
                i = p - 1
            elif c == '+' or c == '-':
                op = c
            else:
                raise InvalidExpression()

        i += 1

    return rv


def test_calculate():
    assert(calculate('1+1') == 2)
    assert(calculate('1 + 1') == 2)
    assert(calculate('2-1 + 2') == 3)
    assert(calculate('1234 + 3210') == 4444)
    with pytest.raises(InvalidExpression):
        calculate('14 + 3 2')


if __name__ == '__main__':
    import sys
    print(calculate(' '.join(sys.argv[1:])))
