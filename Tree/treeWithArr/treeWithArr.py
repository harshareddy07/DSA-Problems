class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Clean version - Array to Tree
def build_from_array(arr):
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        print_tree(root)
        node = queue.pop(0)
        print("pop", node.val)
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Right child  
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Simple tree printer
def print_tree(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Test it
array = [1, 2, 3, 4, 5, 6, 7]
tree = build_from_array(array)

print(f"Array: {array}")
print("Tree:")
print_tree(tree)
