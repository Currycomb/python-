# 这个文件试图创建一个类，包含各种常用的数据结构


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):   # 将栈底选为左端，所以push, pop的时间复杂度位O(1)
        self.items.append(item)

    def pop(self):
        if not self.items:
            return self.items.pop()
        else:
            raise IndexError('pop from empty stack')

    def peek(self):
        if not self.items:
            return self.items[-1]
        else:
            raise IndexError('peek from empty stack')

    def is_empty(self):
        return bool(not self.items)

    def size(self):
        return len(self.items)


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)    # 左端作为队尾，所以enqueue的复杂度为O(n)，dequeue的复杂度为O(1)

    def dequeue(self):
        if not self.items:
            return self.items.pop()
        else:
            raise IndexError('dequeue from empty queue')

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


class Deque(obiect):
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def is_empty(self):
        return not self.items

    def remove_front(self):
        if not self.items:
            return self.items.pop()

    def remove_rear(self):
        if not

    def size(self):
