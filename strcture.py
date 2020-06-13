# 这个文件试图创建一个类，包含各种常用的数据结构

# 栈: Last In First Out
class Stack:
    def __init__(self):
        self.items = []

    # 把数据压入栈
    def push(self, item):   # 将栈底选为左端，所以push, pop的时间复杂度位O(1)
        self.items.append(item)

    # 从栈顶弹出数据
    def pop(self):
        if not self.items:
            return self.items.pop()
        else:
            raise IndexError('pop from empty stack')

    # 查看栈顶的数据
    def peek(self):
        if not self.items:
            return self.items[-1]
        else:
            raise IndexError('peek from empty stack')

    # 判断栈是否为空
    def is_empty(self):
        return bool(not self.items)

    # 返回栈内元素的个数
    def size(self):
        return len(self.items)


# 队列: First In First Out
class Queue:
    def __init__(self):
        self.items = []

    # 向队列添加数据
    def enqueue(self, item):
        self.items.insert(0, item)    # 左端作为队尾，所以enqueue的复杂度为O(n)，dequeue的复杂度为O(1)

    # 从队列中弹出数据
    def dequeue(self):
        if not self.items:
            return self.items.pop()
        else:
            raise IndexError('dequeue from empty queue')

    # 判断队列是否为空
    def is_empty(self):
        return not self.items

    # 返回队列中元素的个数
    def size(self):
        return len(self.items)


# 双端队列
class Deque:
    def __init__(self):
        self.items = []

    # 从首端添加元素
    def add_front(self, item):
        self.items.append(item)    # 以右端作为双端队列的首部

    # 从尾端添加元素
    def add_rear(self, item):
        self.items.insert(0, item)

    # 判断队列是否为空
    def is_empty(self):
        return not self.items

    # 从首端弹出元素
    def remove_front(self):
        if not self.items:
            return self.items.pop()

    # 从尾端弹出元素
    def remove_rear(self):
        if not self.items:
            return self.items.pop(0)

    # 返回队列中元素的个数
    def size(self):
        return len(self.items)


# 节点
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    # 返回当前节点的数据
    def get_data(self):
        return self.data

    # 返回下一个节点的数据
    def get_next(self):
        return self.next

    # 设置下一个节点的数据
    def set_next(self, next_data):
        self.next = next_data

    # 设置当前节点的数据
    def set_data(self, new_data):
        self.data = new_data


# 无序列表(链表)
class UnorderedList:
    def __init__(self):
        self.head = None

    # 将链表中的元素装进一个列表中，打印链表对象是可以直接输出链表中的所有元素
    def __str__(self):
        print_list = []
        current = self.head
        while current is not None:
            print_list.append(current.get_data())
            current = current.get_next()
        return str(print_list)

    # 判断链表是否为空
    def is_empty(self):
        return self.head is None

    # 在链表头部插入元素
    def add(self, value):
        temp = Node(value)
        temp.set_next(self.head)    # 在链表头部插入
        self.head = temp

    # 返回链表中元素的个数
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # 查询链表中的元素
    def search(self, item):
        current = self.head
        found = False
        while (current is not None) and (not found):
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    # 移除链表中的元素
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current is None:
                raise ValueError('{} is not in the UnorderedList' .format(str(item)))
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:    # 考虑要删除的节点是第一个的情况
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # 在链表尾部插入元素
    def append(self, item):
        temp = Node(item)
        current = self.head

        if current is None:
            self.head = temp
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(temp)

    # 查询元素的索引(从0开始)
    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.get_data() == item:
                return count
            current = current.getNext()
            count += 1
        raise ValueError('{} is not in the UnorderedList' .format(str(item)))

    # 删除尾部元素，三种情况
    def pop(self, index=None):
        previous = None
        current = self.head
        if index is None:     # 默认删除尾部的元素并返回
            index = self.size() - 1
        if index < 0 or index >= (self.size()):    # index不能小于0 或者 超出链表的大小
            raise IndexError
        while self.index(current.get_data()) != index:    # 判断当前节点对应的索引是否等于index
            previous = current
            current = current.get_next()
        data = current.get_data()

        # 和remove方法类似
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(None)
        return data

    # 在index位置插入元素
    def insert(self, index, item):
        node = Node(item)
        if index == 0:
            node.set_next(self.head)
            self.head = node
        else:
            if index < 0 or (index >= self.size()):
                raise IndexError

            current = self.head
            previous = None
            while self.index(current.get_data()) != index:
                previous = current
                current = current.get_next()
                if current is None:
                    break
            previous.set_next(node)
            node.set_next(current)

    # 链表反向排序
    def reversed(self):
        previous = None
        temp = None
        current = self.head
        while current is not None:
            temp = current.get_next()
            current.set_next(previous)
            previous = current    # 将current和previous节点向链表的前方移动
            current = temp
            if previous != self.head:
                self.add(previous.get_data())
        return self

if __name__ == '__main__':
    # my_list = UnorderedList()
    # my_list.add(12)
    # my_list.add(143)
    # my_list.add(712)
    pass
