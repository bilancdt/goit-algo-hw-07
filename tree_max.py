class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка елемента
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.value:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    # Пошук 
    def find_maximum(self):
        if self.root is None:
            return None  # Дерево порожнє
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

# Тест
bst = BinarySearchTree()
values = [7,20, 10, 30, 5, 15, 25, 35,47]

# Вставка
for val in values:
    bst.insert(val)

# max
print("Найбільший елемент:", bst.find_maximum())
