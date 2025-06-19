from colorama import Fore


def rightRotate(root):
    pivot = root.left
    reattach_node = pivot.right
    pivot.right = root
    root.left = reattach_node
    return pivot


def leftRotate(root):
    pivot = root.right
    reattach_node = pivot.left
    pivot.left = root
    root.right = reattach_node
    return pivot


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, data):
        if data == self.data:
            return self
        if self.right and data > self.data:
            return self.right.search(data)
        if self.left and data < self.data:
            return self.left.search(data)

    def traversePreOrder(self):
        print(self.data)
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data)
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data)

    def height(self):
        left_height = right_height = 0
        if self.left:
            left_height = 1 + self.left.height()
        if self.right:
            right_height = 1 + self.right.height()
        return max(left_height, right_height)

    def isBalanced(self):
        left_height = self.left.height() + 1 if self.left else 0
        right_height = self.right.height() + 1 if self.right else 0
        return abs(left_height - right_height) < 2

    def getLeftRightHeightDifference(self):
        left_height = self.left.height() + 1 if self.left else 0
        right_height = self.right.height() + 1 if self.right else 0
        return left_height - right_height

    def fixImbalanceIfExists(self):
        if self.getLeftRightHeightDifference() > 1:
            if self.left.getLeftRightHeightDifference() > 0:
                return rightRotate(self)                       # LEFT-LEFT Imbalance
            else:
                self.left = leftRotate(self.left)              # LEFT-RIGHT Imbalance
                return rightRotate(self)
        elif self.getLeftRightHeightDifference() < -1:
            if self.right.getLeftRightHeightDifference() < 0:
                return leftRotate(self)                        # RIGHT-RIGHT Imbalance
            else:
                self.right = rightRotate(self.right)           # RIGHT-LEFT Imbalance
                return leftRotate(self)
        return self

    def rebalance(self):
        if self.left:
            self.left.rebalance()
            self.left = self.left.fixImbalanceIfExists()
        if self.right:
            self.right.rebalance()
            self.right = self.right.fixImbalanceIfExists()

    def getNodesAtDepth(self, depth, current_depth=0, depth_nodes=None):
        depth_nodes = [] if depth_nodes is None else depth_nodes
        if current_depth == 0:
            if self.height() < depth:
                print("There are no nodes at depth {} in the tree".format(depth))
                return []

        if current_depth == depth:
            depth_nodes.append(self)
        elif current_depth < depth:
            if self.left:
                self.left.getNodesAtDepth(depth, current_depth + 1, depth_nodes)
            else:
                depth_nodes.extend([None] * 2 ** (depth - current_depth - 1))
            if self.right:
                self.right.getNodesAtDepth(depth, current_depth + 1, depth_nodes)
            else:
                depth_nodes.extend([None] * 2 ** (depth - current_depth - 1))
        return depth_nodes

    def add(self, data):
        if self.data == data:
            print("Node {} is already present".format(data))
        elif data < self.data:
            if self.left:
                self.left.add(data)
                self.left = self.left.fixImbalanceIfExists()
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
                self.right = self.right.fixImbalanceIfExists()
            else:
                self.right = Node(data)

    def findMinimum(self):
        if self.left:
            return self.left.findMinimum()
        return self.data

    def delete(self, data):
        if self.data == data:
            if self.left and self.right:
                min_data = self.right.findMinimum()
                self.data = min_data
                self.right = self.right.delete(min_data)
                if self.right:
                    self.right = self.right.fixImbalanceIfExists()
                return self
            else:
                return self.left or self.right

        elif self.right and data > self.data:
            self.right = self.right.delete(data)
            if self.right:
                self.right = self.right.fixImbalanceIfExists()
        elif self.left and data < self.data:
            self.left = self.left.delete(data)
            if self.left:
                self.left = self.left.fixImbalanceIfExists()
        return self


class Tree:
    def __init__(self, data, name=''):
        self.root = Node(data)
        self.name = name

    def search(self, data):
        return self.root.search(data)

    def traversePreOrder(self):
        self.root.traversePreOrder()

    def traverseInOrder(self):
        self.root.traverseInOrder()

    def traversePostOrder(self):
        self.root.traversePostOrder()

    def height(self):
        return self.root.height()

    def isBalanced(self):
        return self.root.isBalanced()

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def add(self, data):
        if isinstance(data, list):
            for item in data:
                self.add(item)
        else:
            if self.root:
                self.root.add(data)
                self.root = self.root.fixImbalanceIfExists()
            else:
                self.root = Node(data)

    def delete(self, data):
        self.root = self.root.delete(data)
        self.root = self.root.fixImbalanceIfExists()

    def rebalance(self):
        self.root.rebalance()
        self.root = self.root.fixImbalanceIfExists()

    def print(self, label=''):
        print(self.name + ' - ' + label if label else self.name)
        print('-' * 40)

        if self.root:
            height = self.root.height()
            spacing = 3
            width = int((2 ** height - 1) * (spacing + 1) + 1)
            offset = int((width-1)/2)

            def formatNode(node, space):
                if node is None:
                    return '_' + (' ' * space)
                else:
                    space = space - len(str(node.data)) + 1
                    data = Fore.GREEN + str(node.data) if node.isBalanced() else Fore.RED + str(node.data)
                    data += Fore.RESET
                    return data + (' ' * space)

            for depth in range(0, height + 1):
                if depth > 0:
                    print(' '*(offset + 1) + (' ' * (spacing + 2)).join(['/' + (' ' * (spacing - 2)) +
                                                                         '\\']*(2**(depth-1))))
                row_nodes = self.root.getNodesAtDepth(depth)
                print((' ' * offset) + ''.join([formatNode(node, spacing) for node in row_nodes]))
                spacing = offset + 1
                offset = int(offset/2) - 1
        print('')


# tree = Tree(Node(50), 'Basic Tree')
# tree.root.left = Node(25)
# tree.root.right = Node(75)
# tree.root.left.left = Node(10)
# tree.root.left.right = Node(35)
# tree.root.left.left.left = Node(5)
# tree.root.left.left.right = Node(13)
# tree.root.left.right.left = Node(30)
# tree.root.left.right.right = Node(42)
#
# print("PreOrder")
# tree.traversePreOrder()
#
# print("InOrder")
# tree.traverseInOrder()
#
# print("PostOrder")
# tree.traversePostOrder()
#
# print("Height")
# print(tree.height())
#
# print("Get Nodes at depth")
# print(tree.getNodesAtDepth(3))
#
# tree.add(76)
# tree.add(75)
#
# print(tree.root.findMinimum())
#
# tree.print()
# tree.delete(50)
# tree.print()
#
# tree.print()
# print(tree.isBalanced())
# print(tree.root.left.isBalanced())

# ull = Tree(30, "Unbalanced Left Left")
# ull.add([31, 20, 21, 10, 11, 9])
# ull.print("Before rotate")
# ull.root = rightRotate(ull.root)
# ull.print("After rotate")
#
# urr = Tree(10, "Unbalanced Right Right")
# urr.add([9, 20, 19, 30, 29, 31])
# urr.print("Before rotate")
# urr.root = leftRotate(urr.root)
# urr.print("After rotate")
#
# ulr = Tree(30, "Unbalanced Left Right")
# ulr.add([10,31,9,20,19,21])
# ulr.print("Before rotate")
# ulr.root.left = leftRotate(ulr.root.left)
# ulr.print("After left rotate")
# ulr.root = rightRotate(ulr.root)
# ulr.print("After right rotate")
#
# url = Tree(10, "Unbalanced Right Left")
# url.add([9,30,19,31,15,21])
# url.print("Before rotate")
# url.root.right = rightRotate(url.root.right)
# url.print("After right rotate")
# url.root = leftRotate(url.root)
# url.print("After left rotate")
#
# tree = Tree(30, "Unbalanced Tree")
# tree.add([20, 10, 21])
# tree.print("Before Balancing")
# tree.rebalance()
# tree.print("After Balancing")

tree = Tree(30, "Self-Balancing Tree")
tree.add([21, 35, 20, 24, 37, 15])
tree.print()
tree.delete(37)
tree.print()
# tree.add(24)
# tree.print("Added 24")
# tree.delete(10)
# tree.print("Deleted 10")
