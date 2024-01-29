class binary_tree_node:

    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class binary_tree:

    def __init__(self, root_value):
        self.root = binary_tree_node(root_value)
        
    
    def insert(self, element_to_insert):
        new_node = binary_tree_node(element_to_insert)
        current = self.root
        while current is not None:
            