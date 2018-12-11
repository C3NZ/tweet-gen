from CSsource.linkedlist import LinkedList

class Queue(LinkedList):
    def __init__(self, items=None):
        super(Queue, self).__init__(items)

    def enqueue(self, item):
        '''
            enqueue items into our queue.
            Assumes that item is a piece of data that you'd like to store into the queue
        '''
        self.append(item)

    def enqueue_multiple(self, items):
       '''
            enqueue multiple items at a time into our queue
            assumes items is a list of items trying to be inserted into our queue
       '''
       for item in items:
           self.append(item)

    def dequeue(self):
        '''
            dequeue items from our queue in a FIFO manner.
            Returns the item at the front of the list
        '''
        return self.delete(self.head.data)

    def iterate(self, times=1):
        '''
            iterate through all items of the queue and remove them in order.
            yields a single item per iteration
        '''
        output_list = []
        for i in range(0, times):
            output_list.append(self.delete(self.head.data))
        return output_list

def test_queue():
    items = ['a', 'b', 'c', 'd', 'e']

    # assert that we can properly enqueu items
    queue = Queue(items)
    assert queue.list_length == 5
    print(queue.list_length)

    # Assert that we can dequeu an item 
    item = queue.dequeue()
    assert queue.list_length == 4
    assert item == 'a'
    print(queue.list_length)

    # Prove that our queue is iterable
    for item in queue.iterate():
        print(item)


if __name__ == '__main__':
    test_queue()
