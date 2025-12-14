def delete(root, key):
    if not root:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current
