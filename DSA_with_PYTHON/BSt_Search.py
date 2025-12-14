def search(root, key):
    if not root or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
