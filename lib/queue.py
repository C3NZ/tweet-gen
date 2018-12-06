from CSsource.linkedlist import LinkedList

class Queue(LinkedList):
    def __init__(self, items=None):
        super(Queue, self).__init__(items)

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.delete(self.head.data)

    def iterate(self):
        while not self.is_empty():
            return self.delete(self.head)

def test_queue():
    items = ['a', 'b', 'c', 'd', 'e']
    queue = Queue(items)
    assert queue.list_length == 5
    print(queue.list_length)
    item = queue.dequeue()
    assert queue.list_length == 4
    assert item == 'a'
    print(queue.list_length)


if __name__ == '__main__':
    test_queue()
