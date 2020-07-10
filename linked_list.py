class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        # "Insert new element as the head of the LinkedList"
        if self.is_empty():
            self.head = new_element
            self.head.next = None
        else:
            second = self.head
            self.head = new_element
            self.head.next = second

    def delete_first(self):
        # "Delete the first (head) element in the LinkedList as return it"
        if self.is_empty():
            return None
        else:
            current = self.head
            temp = current.next
            self.head = temp
            return current

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        # "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        # "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()


def main():
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print(ll.head.next.next.value)
    # Should also print 3
    print(ll.get_position(3).value)

    # Test insert
    ll.insert(e4, 3)
    # Should print 4 now
    print(ll.get_position(3).value)

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print(ll.get_position(1).value)
    # Should print 4 now
    print(ll.get_position(2).value)
    # Should print 3 now
    print(ll.get_position(3).value)
    # should print 2
    print(ll.get_position(1).value)
    ll.insert_first(e1)
    # should print 1
    print(ll.get_position(1).value)
    # should print False
    print(ll.is_empty())
    ll.delete_first()
    # should print 2
    print(ll.get_position(1).value)

    stack = Stack(e1)
    print("--------------------")
    # Test stack functionality
    stack.push(e2)
    stack.push(e3)

    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    stack.push(e4)
    print(stack.pop().value)


if __name__ == '__main__':
    main()
