class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Clean BST - Insert function
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    
    return root

# Build BST from array
def build_bst_from_array(arr):
    root = None
    for val in arr:
        root = insert_bst(root, val)
    return root

# Simple tree printer
def print_tree(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Test with same array
array = [1, 2, 3, 4, 5, 6, 7]
bst = build_bst_from_array(array)

print(f"Array: {array}")
print("BST Tree:")
print_tree(bst)

print("\nBST Rule:")
print("- Left child < Parent < Right child")
print("- Tree structure depends on insertion order")
print("- This creates a sorted tree")

# Show different order creates different tree
array2 = [4, 2, 6, 1, 3, 5, 7]
bst2 = build_bst_from_array(array2)

print(f"\nSame values, different order: {array2}")
print("BST Tree:")
print_tree(bst2)
