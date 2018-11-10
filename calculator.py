import pytest


class InvalidExpression(Exception):
    pass


def calculate(expr, cursor=None):
    if cursor is None:
        cursor = {'value': 0}

    rv = op = num = None

    def do_operation():
        nonlocal num, rv, op
        if num is None:
            return
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

    i = cursor['value']
    while i < len(expr) + 1:
        c = expr[i] if i < len(expr) else ' '

        if c.isdigit():
            if num is None:
                num = int(c)
            else:
                num *= 10
                num += int(c)
        else:
            do_operation()

            if c.isspace():
                pass
            elif c == '(':
                cursor['value'] = i + 1
                num = calculate(expr, cursor)
                i = cursor['value']
            elif c == ')':
                do_operation()
                break
            elif c == '+' or c == '-':
                op = c
            else:
                raise InvalidExpression()

        i += 1

    cursor['value'] = i
    return rv


def test_calculate():
    assert(calculate('1+1') == 2)
    assert(calculate('1 + 1') == 2)
    assert(calculate('2-1 + 2') == 3)
    assert(calculate('1234 + 3210') == 4444)
    with pytest.raises(InvalidExpression):
        calculate('14 + 3 2')
    assert(calculate('(1+(4+5+2)-3)+(6+8)') == 23)


def evalRPN(tokens):
    stack = []

    op = {
        '+': lambda n1, n2: n1 + n2,
        '-': lambda n1, n2: n1 - n2,
        '*': lambda n1, n2: n1 * n2,
        '/': lambda n1, n2: int(float(n1) / n2)
    }

    for tok in tokens:
        if tok in op:
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(op[tok](n1, n2))
        else:
            stack.append(int(tok))

    return stack[0]


if __name__ == '__main__':
    import sys
    # print(calculate(' '.join(sys.argv[1:])))
    # print(evalRPN(["2", "1", "+", "3", "*"]))
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
