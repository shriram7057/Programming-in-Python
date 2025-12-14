def insert_end(self, data):
    node = Node(data)
    if not self.head:
        self.head = node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = node
