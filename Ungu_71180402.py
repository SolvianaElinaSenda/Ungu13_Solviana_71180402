class Node:
#constructor
    def __init__(self, data, parent):
        self._data = data
        self._parent = parent
        self._left = None
        self._right = None
#menambah data
    def insert(self, data):
        if data < self.operator():
            if self.left() is None:
                self._left = Node(data, self)
            else:
                self.left().insert(data)
        elif data > self.operator():
            if self.right() is None:
                self._right = Node(data, self)
            else:
                self.right().insert(data)
        else:
            return False 
        return True 

    #mendapatkan isi elemen
    def operator(self):
        return self._data
    #mendapatkan child sebelah kiri
    def left(self):
        return self._left
    #mendapatkan child sebelah kanan
    def right(self):
        return self._right
    #mendapatkan node parent
    def parent(self):
        return self._parent

    #mengecek apakah node merupakan root
    def isRoot(self):
        return self._parent is None

    #mengecek apakah node merupakan external/leaf
    def isExternal(self):
        return self._left is None and self._right is None

       #mengeset node left
    def setLeft(self, node):
        self._left = node
    #mengeset node right
    def setRight(self, node):
        self._right = node
    #mengeset node parent
    def setParent(self, node):
        self._parent = node

class BinaryTree:
#constructor
    def __init__(self):
        self._root = None
        self._size = 0
    #menambah data
    def add(self, data):
        if self._root is None:
            self._root = Node(data, None)
            self._size+=1
        else:
            if self._root.insert(data):
                self._size+=1

    #mendapatkan jumlah node dari tree
    def size(self):
        return self._size

    #mengecek apakah tree kosong
    def empty(self):
        return self._size == 0

    #mencetak seluruh node
    def nodes(self):
        self.inorder(self._root)
    #inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            print(node.operator(), end = ' ')
            self.inorder(node.right())
    #mencari data
    def expandExternal(self, value):
        node = self.binarySearch(self._root, value)
        if node is not None and node.isExternal():
            node.insert(node.operator()-1)
            node.insert(node.operator()+1)
            self._size+=2




tree = BinaryTree()
tree.add(5)
tree.add(4)
tree.add(3)
tree.add(9)
tree.add(8)
tree.add(6)
tree.add(7)
tree.add(11)
tree.add(10)
tree.nodes()




