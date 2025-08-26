class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def find_lca(root, p, q):
    # Base case 1: If we reach end of tree
    if not root:
        return None
    
    # Base case 2: If current node is one of our target nodes
    if root.val == p or root.val == q:
        return root
    
    # Recursive case: Search left and right subtrees
    left_result = find_lca(root.left, p, q)
    right_result = find_lca(root.right, p, q)
    
    # Decision logic:
    if left_result and right_result:
        # Found one node in left, one in right
        # So current node is the LCA
        return root
    elif left_result:
        # Only found something in left subtree
        return left_result
    else:
        # Only found something in right subtree (or nothing)
        return right_result

# Build test tree:
#     1
#    / \
#   2   3
#  / \
# 4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Tree:")
print("    1")
print("   / \\")
print("  2   3")
print(" / \\")
print("4   5")
print()

# Test cases
print("Test 1: LCA of 4 and 5")
result = find_lca(root, 4, 5)
print(f"Result: {result.val if result else None}")
print("Expected: 2 (both are children of 2)")
print()

print("Test 2: LCA of 4 and 3")
result = find_lca(root, 4, 3)
print(f"Result: {result.val if result else None}")
print("Expected: 1 (4 is in left subtree, 3 is in right subtree)")
print()

print("Test 3: LCA of 2 and 5")
result = find_lca(root, 2, 5)
print(f"Result: {result.val if result else None}")
print("Expected: 2 (2 is ancestor of 5)")
print()

print("HOW IT WORKS:")
print("1. Start from root, search both left and right")
print("2. If found target in both sides → current node is LCA")
print("3. If found in only one side → return that result")
print("4. Base cases: reached end OR found target node")
