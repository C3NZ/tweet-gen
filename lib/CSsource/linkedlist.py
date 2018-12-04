#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.list_length = 0

        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        return (node for node in self)

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) where n is the amount of nodes in the linked list
        in all cases because every call to this function has to iterate through the entire
        linked list"""
        # TODO: Loop through all nodes and count one for each
        length = 0

        if self.is_empty():
            return length
        else:
            current_node = self.head

            while current_node:
                length += 1
                current_node = current_node.next

            return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) because there is a fixed amount of operations occurring
        every function call"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)

        if not self.is_empty():
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = self.head

        self.list_length += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because there is a fixed amount of operations occurring every function call"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)

        if not self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = self.head

        self.list_length += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) in cases where the list is empty or the item we're looking for
        is at the beginning of the list
        TODO: Worst case running time: O(n) where the item is the last item in the list"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        if self.is_empty():
            return None
        else:
            current_node = self.head
            while not quality(current_node.data):
                if current_node.next == None:
                    return None
                else:
                    current_node = current_node.next

            return current_node.data

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) in cases where the list is empty or the item we're looking for
        is the front of the list
        TODO: Worst case running time: O(n) in cases where the item we're looking to delete is in the last
        node in the list'"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
        else:
            traversing = True
            prev_node = None
            current_node = self.head

            while traversing:
                if item == current_node.data:
                    if prev_node:
                        if self.tail == current_node:
                            prev_node.next = None
                            self.tail = prev_node
                        else:
                            prev_node.next = current_node.next
                    else:
                        if self.tail == self.head:
                            self.head = None
                            self.tail = None
                        else:
                            self.head = current_node.next

                    traversing = False
                    self.list_length -= 1
                else:
                    if current_node.next is None:
                        raise ValueError('Item not found: {}'.format(item))
                    else:
                        prev_node = current_node
                        current_node = current_node.next

            return current_node.data

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
