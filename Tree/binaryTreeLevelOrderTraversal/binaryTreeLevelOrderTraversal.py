class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Level Order Traversal - Simple version
def level_order_simple(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)  # Take first node from queue
        result.append(node.val)  # Visit it
        
        # Add children to queue (left first, then right)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Level Order Traversal - With levels separated
def level_order_by_levels(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)  # How many nodes in current level
        current_level = []
        
        # Process all nodes in current level
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Build test tree
#       3
#      / \
#     9   20
#        /  \
#       15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Test both versions
print("Tree structure:")
print("       3")
print("      / \\")
print("     9   20")
print("        /  \\")
print("       15   7")
print()

simple_result = level_order_simple(root)
print(f"Simple level order: {simple_result}")

levels_result = level_order_by_levels(root)
print(f"Level by level: {levels_result}")

print("\nHow it works:")
print("1. Start with root in queue: [3]")
print("2. Process 3, add its children: queue = [9, 20]")
print("3. Process 9 (no children), process 20, add its children: queue = [15, 7]")
print("4. Process 15 and 7 (no children), queue empty = done!")
