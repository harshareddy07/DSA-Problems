class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Clean BST validation
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

# Test 1: Valid BST
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(5)

print("Test 1 - Valid BST:")
print("    3")
print("   / \\")  
print("  1   5")
print(f"Result: {is_valid_bst(root1)}")
print()

# Test 2: 4 as left child of 1 (Invalid)
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(7)
root2.left.left = TreeNode(1)
root2.left.left.left = TreeNode(4)  # Wrong!

print("Test 2 - 4 as LEFT child of 1:")
print("      5")
print("     / \\")
print("    3   7")
print("   /")
print("  1")
print(" /")
print("4")
print(f"Result: {is_valid_bst(root2)}")
print("Why: 4 gets bounds (-∞, 1), but 4 > 1")
print()

# Test 3: 4 as right child of 1 (Still Invalid)
root3 = TreeNode(5)
root3.left = TreeNode(3)
root3.right = TreeNode(7)
root3.left.left = TreeNode(1)
root3.left.left.right = TreeNode(4)  # Still wrong!

print("Test 3 - 4 as RIGHT child of 1:")
print("      5")
print("     / \\")
print("    3   7")
print("   /")
print("  1")
print("   \\")
print("    4")
print(f"Result: {is_valid_bst(root3)}")
print("Why: 4 gets bounds (1, 3), but 4 > 3")
print()

# Test 4: 4 in correct position (Valid)
root4 = TreeNode(5)
root4.left = TreeNode(3)
root4.right = TreeNode(7)
root4.left.left = TreeNode(1)
root4.left.right = TreeNode(4)  # Correct!

print("Test 4 - 4 as RIGHT child of 3:")
print("      5")
print("     / \\")
print("    3   7")
print("   / \\")
print("  1   4")
print(f"Result: {is_valid_bst(root4)}")
print("Why: 4 gets bounds (3, 5), and 3 < 4 < 5 ✓")
