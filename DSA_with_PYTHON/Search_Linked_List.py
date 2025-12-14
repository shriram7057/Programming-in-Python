def search(self, val):
    temp = self.head
    while temp:
        if temp.data == val:
            return True
        temp = temp.next
    return False
