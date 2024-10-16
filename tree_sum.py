class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка 
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

    # Рекурс. функція для суми
    def find_sum(self, node):
        if node is None:
            return 0
        return node.value + self.find_sum(node.left) + self.find_sum(node.right)

    # Виклик функції від кореня дерева
    def sum_of_all_nodes(self):
        return self.find_sum(self.root)

# Тест
bst = BinarySearchTree()
values = [34,17,35,3,101,77,84,50,33,66]

# Вставка
for val in values:
    bst.insert(val)

print("Сума всіх елементів :", bst.sum_of_all_nodes())
