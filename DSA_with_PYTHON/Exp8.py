class Node:
    def __init__(self, key):
        """
        Initializes a new node with the given key and sets left/right children to None.
        """
        self.key, self.left, self.right = key, None, None

class BST:
    def insert(self, root, key):
        """
        Inserts a new key into the BST and returns the new root.
        """
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        """
        Searches for a key in the BST. Returns the node if found, otherwise None.
        """
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        """
        Performs Inorder Traversal (Left, Root, Right) and returns a list of keys.
        """
        if not root:
            return []
        else:
            return self.inorder(root.left) + [root.key] + self.inorder(root.right)

    def preorder(self, root):
        """
        Performs Preorder Traversal (Root, Left, Right) and returns a list of keys.
        """
        if not root:
            return []
        else:
            return [root.key] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        """
        Performs Postorder Traversal (Left, Right, Root) and returns a list of keys.
        """
        if not root:
            return []
        else:
            return self.postorder(root.left) + self.postorder(root.right) + [root.key]

    def minvalueNode(self, node):
        """
        Finds the node with the minimum key value in a given subtree (the inorder successor).
        """
        while node.left is not None:
            node = node.left
        return node

    def delete(self, root, key):
        """
        Deletes a key from the BST and returns the new root of the subtree.
        """
        if root is None:
            return root

        # 1. Recurse down the tree to find the node to delete
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # 2. Key is found (root is the node to be deleted)

            # Case 1 & 2: Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node with two children
            # Get the inorder successor (smallest in the right subtree)
            temp = self.minvalueNode(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.key)

        return root

# --- Execution Code ---

# Create an instance of the BST class
bst = BST()
root = None

# Keys to insert: [50, 30, 20, 40, 70, 60, 80]
insertion_keys = [50, 30, 20, 40, 70, 60, 80]
for key in insertion_keys:
    root = bst.insert(root, key)

# Print initial traversals
print("Inorder Traversal :", bst.inorder(root))
print("Preorder Traversal :", bst.preorder(root))
print("Postorder Traversal :", bst.postorder(root))

# Search for 40
search_result = bst.search(root, 40)
if search_result:
    print("Search 40: Found")
else:
    # Based on the sample output, this case should be 'Found' for 40
    print("Search 40: Not found")

# Delete 20
root = bst.delete(root, 20)

# Print Inorder Traversal after deletion
print("After deleting 20 (Inorder):", bst.inorder(root))