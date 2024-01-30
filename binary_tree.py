class binary_tree_node:

    def __init__(self, value, left_child, right_child):
        self.count = 1
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class binary_tree:

    def __init__(self, root_value):
        self.root = binary_tree_node(root_value)
        
    
    def insert(self, element_to_insert):
        #this implementation will keep a count of repeat values

        new_node = binary_tree_node(element_to_insert)
        current = self.root

        while current:

            if new_node.value < current.value:
                if current.left_child:
                    current = current.left_child
                else:
                    current.left_child = new_node

            elif new_node.value > current.value:
                if current.right_child:
                    current = current.right_child
                else:
                    current.right_child = new_node

            elif new_node.value == current.value:
                current.count = current.count + 1
                break
            