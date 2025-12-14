def delete(self, val):
    temp = self.head
    if temp and temp.data == val:
        self.head = temp.next
        return
    while temp and temp.next:
        if temp.next.data == val:
            temp.next = temp.next.next
            return
        temp = temp.next
