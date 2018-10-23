
def solve_hanoi(n):
    src = []
    dest = []
    buf = []

    for i in range(n, 0, -1):
        src.append(i)

    def print_stacks():
        print(src)
        print(dest)
        print(buf)
        print()

    print_stacks()
    move_disks(n, src, dest, buf, print_stacks)


def move_disks(n, src, dest, buf, print_stacks):
    if n <= 0:
        return

    move_disks(n - 1, src, buf, dest, print_stacks)
    dest.append(src.pop())
    print_stacks()
    move_disks(n - 1, buf, dest, src, print_stacks)


if __name__ == '__main__':
    solve_hanoi(8)
