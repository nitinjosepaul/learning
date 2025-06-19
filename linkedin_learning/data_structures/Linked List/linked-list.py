from node import SLLNode, DLLNode


class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL object | Head : [{}]".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        current_size = 0
        current_node = self.head
        while current_node:
            current_size += 1
            current_node = current_node.get_next()
        return current_size

    def search(self, data):
        if self.is_empty():
            print("Linked list is empty!")
            return False

        current_node = self.head
        while current_node:
            if current_node.get_data() == data:
                print("{} is present in linked list".format(data))
                return True
            current_node = current_node.get_next()
        else:
            print("{} is not present in linked list".format(data))
            return False

    def add_front(self, new_data):
        new_node = SLLNode(new_data)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, data):
        if self.is_empty():
            print("Linked list is empty!")
            return False

        current = self.head
        previous = None
        while current:
            if current.get_data() == data:
                if current == self.head:
                    self.head = current.get_next()
                    print("Removed node from beginning of linked list")
                else:
                    previous.set_next(current.get_next())
                    print("Removed node other than beginning")
                return True
            else:
                previous = current
                current = current.get_next()
        else:
            print("Node to be removed not present!")
            return False


class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "DLL object | Head : [{}]".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        current_size = 0
        current_node = self.head
        while current_node:
            current_size += 1
            current_node = current_node.get_next()
        return current_size

    def search(self, data):
        if self.is_empty():
            print("Linked list is empty!")
            return False

        current_node = self.head
        while current_node:
            if current_node.get_data() == data:
                print("{} is present in linked list".format(data))
                return True
            current_node = current_node.get_next()
        else:
            print("{} is not present in linked list".format(data))
            return False

    def add_front(self, new_data):
        new_node = DLLNode(new_data)
        if self.head:
            self.head.set_prev(new_node)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, data):
        if self.is_empty():
            print("Linked list is empty!")
            return False

        current = self.head
        previous = None
        while current:
            if current.get_data() == data:
                if current == self.head:
                    self.head = current.get_next()
                    self.head.set_prev(None)
                    print("Removed node from beginning of linked list")

                else:
                    previous.set_next(current.get_next())
                    current.get_next().set_prev(previous)
                    print("Removed node other than beginning")
                return True
            else:
                previous = current
                current = current.get_next()
        else:
            print("Node to be removed not present!")
            return False
