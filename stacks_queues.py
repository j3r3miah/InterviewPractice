
class Stack:
    s = None

    def __init__(self):
        self.s = list()

    def push(self, data):
        self.s.append(data)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]

    @property
    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.s)
        


class LameQueue:
    pushstack = None
    popstack = None

    def __init__(self):
        self.pushstack = Stack()
        self.popstack = Stack()

    def add(self, data):
        LameQueue._shift(self.popstack, self.pushstack)
        self.pushstack.push(data)

    def remove(self):
        LameQueue._shift(self.pushstack, self.popstack)
        return self.popstack.pop()

    def __len__(self):
        return len(self.pushstack) + len(self.popstack)

    @staticmethod
    def _shift(src, dest):
        while not src.empty:
            dest.push(src.pop())


if __name__ == '__main__':
    q = LameQueue()
    q.add(5)
    q.add(1)
    print(q.remove())
    q.add(3)
    q.add(1)
    # print(q.remove())
    q.add(9)
    q.add(1)
    # print(q.remove())
    q.add(2)

    while len(q):
        print(q.remove())
